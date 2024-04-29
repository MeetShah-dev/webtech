import httpx

from urllib.parse import parse_qs
from django.conf import settings

from .models import User


class WebsocketAuthMiddleware:
    """
    Custom middleware that checks that the client is authenticated.
    """

    def __init__(self, app):
        """
        Constructor is called upon the server's start. It stores the ASGI asgi app and 
            initialises the authentication service url, and the existing channel paths 
            for later use.
        """
        self.app = app
        self.auth_api = settings.USER_AUTH_API
        self.EVENT_CHANNEL = '/ws/event/'
        self.NOTIFICATION_CHANNEL = '/ws/notification/'

    async def __call__(self, scope, receive, send):
        """
        The __call__ method is called before establishing a websocket connection. This method validates 
            the access token issued by the authentication service, and stores the authentication status 
            in the scope dictionary to be used in the notification and event consumer. Thereby, security 
            is enhanced by rejecting unauthenticated/unauthorized connections.
        """
        scope['user_auth'] = False 
        query_string = parse_qs(
            scope['query_string'].decode()
        )
        if 'Authorization' in query_string.keys():
            is_authenticated = await self.is_authenticated(
                query_string['Authorization'][0],
                scope
            )
            if is_authenticated:
                scope['user_auth'] = True
        return await self.app(scope, receive, send)
    
    async def is_authenticated(self, token: str, scope: dict) -> bool:
        """
        Sends a request to the authentication service in order to validate the token 
            sent by the client. In the event of a successful authentication the path
            of the websocket that the user is attempting to connect to, is compared
            to the existing app channels. If the paths match, the connection is made.

        Parameters:
            token (str): The access token generated by the authentication service.
            scope (dict): Meta data and information about the websocket connection.
        Returns:
            bool: True or False depending on whether the authentication is validated.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=self.auth_api + token
            )
            data = response.json()
            path = scope['path']
            if not 'error' in data.keys():
                if data['verified_email']:
                    user = await self.get_user(data['email'])
                    if user:
                        if path == self.EVENT_CHANNEL:
                            return await self.authorize_event_channel(scope, user)
                        if self.NOTIFICATION_CHANNEL in path:
                            return await self.authorize_notification_channel(path, user)
            return False
        
    async def authorize_notification_channel(self, path: str, user: User): 
        """
        Checks that the path of the websocket that the user is trying to connect to
            matches their assigned websocket path. This ensures that each user can 
            only access their designated channel.

        Parameters:
            path (str): The path of the websocket the user is trying to connect to.
            user (User): The user instance.
        Returns:
            bool: True if the user is connecting to their channel, or False otherwise.
        """
        user_designated_channel = self.NOTIFICATION_CHANNEL + str(user.pk) + '/'
        if path == user_designated_channel:
            return True
        return False

    async def authorize_event_channel(self, scope: dict, user: User) -> bool:
        """
        Subscribes the authenticated user to the event channel. No further checks are made as
            authentication is enough. This channel serves as a general platform to notify all
            users about general events. The user first name and id are passed to the consumer
            through the scope dictionary for convenience.

        Parameters:
            scope (dict): Meta data and information about the websocket connection.
            user (User): The user instance.
        Returns:
            bool: True as the user authentication is sufficient to subscribe to this channel.
        """
        scope['user_id'] = user.pk
        scope['user_first_name'] = f'{user.first_name}'
        return True
    
    @staticmethod
    async def get_user(email: str) -> User | None:
        """
        Database query to retrieve a user object based on the verified email address. 

        Parameters:
            email (str): The email address of the authenticated user.
        Returns:
            User: The user instance.
            None: The user queried is not registered in the database.
        """
        try:
            user = await User.objects.aget(email=email)
            return user
        except User.DoesNotExist:
            return None