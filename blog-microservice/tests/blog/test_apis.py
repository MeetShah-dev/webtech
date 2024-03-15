import json
import time
import pytest

from rest_framework.test import APIClient
from django.utils import timezone

from tests.factories import FileFactory, BlogFactory, DraftFactory, UserFactory, DataGenerator, fake
from blog.utils import ApiResponse
from blog.models import Blog, File

pytestmark = pytest.mark.django_db


class TestReadFeedApi:

    endpoint = '/blog/magazine-feed/'

    def test_feed_get(self, api_client, file_factory: FileFactory) -> None:
        """
        Tests the retrieval of blogs on the feed through the API to ensure it is successful. 

        Parameters:
            api_client (APIClient): The library used to make requests.
            file_factory (FileFactory): Used to create files associated to blogs in one go.
        """
        file_factory.create_batch(2)
        response = api_client().get(self.endpoint)

        assert response.status_code == 200

    def test_feed_next_get(self, api_client, blog_factory: BlogFactory) -> None:
        """
        Tests the retrieval of blogs on the feed's next page through the API to ensure it is successful. 
        
        Parameters:
            api_client (APIClient): The library used to make requests.
            blog_factory (BlogFactory): Used to create blogs.
        """
        blog_factory.create_batch(20)
        response = api_client().get(self.endpoint)

        assert response.status_code == 200

        blogs = response.json()
        response = api_client().get(blogs['next'])

        assert response.status_code == 200


class TestReadDraftsApi: 

    endpoint = '/blog/read-drafts/'

    def test_drafts_get(self, api_client: APIClient, user_factory: UserFactory,  draft_factory: DraftFactory) -> None:
        """
        Tests the retrieval of the user's drafts through the API to ensure it is successful. 

        Parameters:
            api_client (APIClient): The library used to make requests.
            user_factory (UserFactory): Used to create users.
            draft_factory (DraftFactory): Used to create drafts.
        """
        user = user_factory()
        client = api_client()

        draft_factory.create_batch(8, user=user)

        data = {'user' : user.id}

        response = client.generic(
            method="GET", 
            path=self.endpoint, 
            data=json.dumps(data), 
            content_type='application/json'
        )

        drafts = response.json()

        assert response.status_code == 200
        assert drafts['count'] == 8


class TestReadBlogApi: 

    endpoint = '/blog/read-blog/'

    def test_blog_get(self, api_client: APIClient, blog_factory: BlogFactory) -> None:
        """
        Tests the retrieval of a single blog through the API to ensure it is successful. 

        Parameters:
            api_client (APIClient): The library used to make requests.
            blog_factory (BlogFactory): Used to create blogs.
        """
        client = api_client()
        blog = blog_factory()

        data = {'id' : blog.id}

        response = client.generic(
            method="GET", 
            path=self.endpoint, 
            data=json.dumps(data), 
            content_type='application/json'
        )

        assert response.status_code == 200


class TestReadUserBlogsApi: 

    endpoint = '/blog/read-user-blogs/'

    def test_user_blogs_get(self, api_client: APIClient, user_factory: UserFactory,  blog_factory: BlogFactory) -> None:
        """
        Tests the retrieval of the user's blogs through the API to ensure it is successful. 

        Parameters:
            api_client (APIClient): The library used to make requests.
            user_factory (UserFactory): Used to create users.
            blog_factory (BlogFactory): Used to create blogs.
        """
        user = user_factory()
        client = api_client()

        blog_factory.create_batch(5, user=user)

        data = {'user' : user.id}

        response = client.generic(
            method="GET", 
            path=self.endpoint, 
            data=json.dumps(data), 
            content_type='application/json'
        )

        drafts = response.json()

        assert response.status_code == 200
        assert drafts['count'] == 5


class TestCreateBlogApi: 

    endpoint = '/blog/create-blog/'

    def test_blog_text_post(self, api_client: APIClient, blog_factory: BlogFactory) -> None:
        """
        Tests the creation of blogs through the API with text only to ensure it is successful. 

        Parameters:
            api_client (APIClient): The library used to make requests.
            blog_factory (BlogFactory): Used to create blogs.
        """
        blog    = blog_factory()
        client  = api_client()

        data = DataGenerator.data_text(blog)

        response = client.post(self.endpoint, data=data, format='multipart')

        assert response.status_code == 201
        assert response.json() == ApiResponse.BLOG_POST_TEXT_SUCCESS

    def test_blog_files_post(self, api_client: APIClient, blog_factory: BlogFactory) -> None:
        """
        Tests the creation of blogs through the API with text and files to ensure it is successful. 

        Parameters:
            api_client (APIClient): The library used to make requests.
            blog_factory (BlogFactory): Used to create blogs.

        """
        blog    = blog_factory()
        client  = api_client()

        data = DataGenerator.data_with_files(blog)

        response = client.post(self.endpoint, data=data, format='multipart')

        assert response.status_code == 201
        assert response.json() == ApiResponse.BLOG_POST_FILES_SUCCESS


class TestUpdateBlogApi:
    
    endpoint = '/blog/update-blog/'

    def test_blog_text_put(self, api_client: APIClient, blog_factory: BlogFactory) -> None:
        """
        Tests the update of blogs with text through the API to ensure it is successful. 

        Parameters:
            api_client (APIClient): The library used to make requests.
            blog_factory (BlogFactory): Used to create blogs.
        """
        client = api_client()

        blog_initial_data = blog_factory(
            title=fake.sentence(), 
            content=fake.paragraph(), 
            date_created=self.__generate_random_datetime()
        )
        blog_updated_data = blog_factory(
            title=fake.sentence(), 
            content=fake.paragraph(),
            date_created=timezone.now()
        )

        blog = self.__initial_blog(blog_initial_data)

        data = {
            'id': blog.pk,
            'user': blog.user.pk,
            'magazine': blog.magazine.pk,
            'category': blog.category.pk,
            'title': blog_updated_data.title,
            'content': blog_updated_data.content,
            'date_created': blog_updated_data.date_created,
            'is_draft': False,
        }

        response = client.put(self.endpoint, data=data, format='multipart')

        assert response.status_code           == 201
        assert response.json()                == ApiResponse.BLOG_PUT_TEXT_SUCCESS
        assert blog_updated_data.title        != blog_initial_data.title
        assert blog_updated_data.content      != blog_initial_data.content
        assert blog_updated_data.date_created != blog_initial_data.date_created

    def test_blog_files_put(self, api_client: APIClient, blog_factory: BlogFactory) -> None:
        """
        Tests the update of blogs with files through the API to ensure it is successful. 

        Parameters:
            api_client (APIClient): The library used to make requests.
            blog_factory (BlogFactory): Used to create blogs.
        """
        client = api_client()

        blog_initial_data = blog_factory(
            title=fake.sentence(), 
            content=fake.paragraph(), 
            date_created=self.__generate_random_datetime()
        )
        blog_updated_data = blog_factory(
            title=fake.sentence(), 
            content=fake.paragraph(),
            date_created=timezone.now()
        )

        blog = self.__initial_blog(blog_initial_data)

        data = DataGenerator.data_with_files(blog_updated_data)

        data['id'] = blog.pk
        data['user'] = blog.user.pk
        data['magazine'] = blog.magazine.pk
        data['category'] = blog.category.pk

        response = client.put(self.endpoint, data=data, format='multipart')

        assert response.status_code           == 201
        assert response.json()                == ApiResponse.BLOG_PUT_FILES_SUCCESS
        assert blog_updated_data.title        != blog_initial_data.title
        assert blog_updated_data.content      != blog_initial_data.content
        assert blog_updated_data.date_created != blog_initial_data.date_created

    def __initial_blog(self, blog_initial_data: BlogFactory) -> Blog:
        """
        Helper method to create new blogs and store them the database.

        Parameters:
            blog_initial_data (BlogFactory): The source of the data.

        Returns:
            Blog: A Blog instance.
        """
        blog = Blog.objects.create(
            title        = blog_initial_data.title,
            content      = blog_initial_data.content,
            is_approved  = blog_initial_data.is_approved,
            is_draft     = blog_initial_data.is_draft,
            date_created = blog_initial_data.date_created,
            keywords     = blog_initial_data.keywords,
            user         = blog_initial_data.user,
            magazine     = blog_initial_data.magazine,
            category     = blog_initial_data.category
        )
        return blog
    
    def __generate_random_datetime(self) -> str:
        """
        Helper function to generate random time formatted suitably for the database.
        """
        random_date_time = fake.date_time_this_month()
        formatted_date_time = random_date_time.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_date_time


class TestDeleteBlogApi: 

    endpoint = '/blog/delete-blog/'

    def test_blog_delete(self, api_client: APIClient, blog_factory: FileFactory) -> None:
        """
        Tests the deletion of blogs through the API to ensure it is successful. 
        
        Parameters:
            api_client (APIClient): The library used to make requests.
            blog_factory (BlogFactory): Used to create blogs.
        """
        blog    = blog_factory()
        client  = api_client()

        data = {'id': blog.id}

        assert Blog.objects.filter(pk=blog.id).exists()

        client.delete(self.endpoint, data=data, format='json')

        assert not Blog.objects.filter(pk=blog.id).exists()


class TestDeleteFileApi: 

    endpoint = '/blog/delete-file/'

    def test_delete_file(self, api_client: APIClient, file_factory: FileFactory) -> None:
        """
        Tests the deletion of files and their placeholder in the
            blog's text through the API to ensure it is successful. 
        
        Parameters:
            api_client (APIClient): The library used to make requests.
            file_factory (FileFactory): Used to create files associated to blogs in one go.
        """
        file    = file_factory()
        client  = api_client()

        file_id      = file.id
        file_uid     = str(file.uid)
        blog         = file.blog
        blog_id      = blog.id
        blog_content = blog.content
        
        assert file_uid in blog_content

        data = {'id': file_id}

        client.delete(self.endpoint, data=data, format='json')

        updated_blog = Blog.objects.get(pk=blog_id)
        updated_content = updated_blog.content

        assert file_uid not in updated_content
        assert not File.objects.filter(pk=file_id).exists()