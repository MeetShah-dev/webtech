from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from moderatorAdmin.models import Blog, User, Magazine, Category, Comment, Role
from moderatorAdmin.serializer import  CategorySerializerA,ManyCategorySerializer, CommentSerializer, RoleSerializer,UserRoleSerializer,BlogSerializer, UserSerializer, MagazineSerializer,CategorySerializer,UserSerializerB,CategorySerializer,FeedbackSerializerUp
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils import timezone
from rest_framework.renderers import JSONRenderer

    

#----------------------------------------#Post Feedback oldu ama notificationı düşün ------------------------------------------
@csrf_exempt
@api_view(['POST'])

def postFeedback(request):
    
    # List all code snippets, or create a new snippet.
  
    if request.method == 'POST':
        serializer = FeedbackSerializerUp(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            snippet_listPOST(request)
           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#---------------------------ADD COMMENT-------------------------------------------------
@csrf_exempt
@api_view(['POST'])
def addComment(request):
    
    # List all code snippets, or create a new snippet.
    request.data['timestamp'] = timezone.now()
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
          
           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 #----------------------------------------#GET COMMENTS AVERALL ------------------------------------------

@csrf_exempt
@api_view(['GET'])
def getComments(request):
    if request.method == 'GET':
        category = Comment.objects.all()
        serializer = CommentSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   
    


 #----------------------------------------#DELETE COMMENT  ------------------------------------------

@csrf_exempt
@api_view(['DELETE'])
def deleteComment(request):
    pk = request.data.get('id')  # Get pk from request data
    if pk is None:
        return Response({'error': 'Primary key (pk) not provided in the request body'}, status=400)
    
    try:
        instance = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({'error': 'Object does not exist'}, status=404)

    serializer = CommentSerializer(instance)
    instance.delete()
    return Response(serializer.data, status=204)
  
#----------------------------------------#ADD CATEGORY FOR MODERATOR (to the category table) ------------------------------------------
@csrf_exempt
@api_view(['POST'])
def addCategory(request):
    
    # List all code snippets, or create a new snippet.
  
    if request.method == 'POST':
        serializer = CategorySerializerA(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
          
           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#----------------------------------------#ADD more than 1 CATEGORIES AVERALL (to the category table) ------------------------------------------
    
@csrf_exempt
@api_view(['POST'])
def postManyCategories(request):
    if request.method == 'POST':
        data = request.data
        serializer = CategorySerializerA(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#----------------------------------------#GET CATEGORIES AVERALL (to the category table) ------------------------------------------
@csrf_exempt
@api_view(['GET'])
def getReadyPosts(request):
    if request.method == 'GET':
        blog = Blog.objects.filter(is_approved="False", is_ready="True")
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def get_all_categories(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#----------------------------------------#GET ALL USERS ------------------------------------------
@csrf_exempt
@api_view(['GET'])
def getAllUsers(request):
    if request.method == 'GET':
        category = User.objects.all()
        serializer = UserSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#-------------------------------DELETE CATEGORY-------------------"
    
@api_view(['DELETE'])
def deleteCategory(request):
    pk = request.data.get('id')  # Get pk from request data
    if pk is None:
        return Response({'error': 'Primary key (pk) not provided in the request body'}, status=400)
    
    try:
        instance = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Object does not exist'}, status=404)

    serializer = CategorySerializer(instance)
    instance.delete()
    return Response(serializer.data, status=204)



#----------------------------------------#Change schedule of magazine-----------------------------------------
#{   example data: id dediğimiz blogun idsi gelcek, bu body ile
    # "id":1,
    # "planned_date_released":"2025-03-13 15:30:00.000 +0000"
    # }
@csrf_exempt
@api_view(['PUT'])
def changeScheduleOfMagazine(request):
    pk = request.data.get('id')
    if not pk:
        return Response({"error": "Primary key (pk) is required in the request body."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        instance =Magazine.objects.get(pk=pk)
    except Magazine.DoesNotExist:
        return Response({"error": "Instance with the provided primary key does not exist."}, status=status.HTTP_404_NOT_FOUND)

    serializer =MagazineSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#------------------------BAN USER-------------------------------{
#     "id":5,
#     "banned":"True"
# }

@csrf_exempt
@api_view(['PUT'])

def banUser(request):
    pk = request.data.get('id')
    if not pk:
        return Response({"error": "Primary key (pk) is required in the request body."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        instance = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "Instance with the provided primary key does not exist."}, status=status.HTTP_404_NOT_FOUND)

    serializer =UserSerializerB(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)
                    
                    ####
#------------------------------------------------REMOVE THE MODERATOR--------------------



#------------------------------------------------CHANGE THE ROLE--------------------

@csrf_exempt
@api_view(['PUT'])
def changeRole(request):
    pk = request.data.get('id')
    if not pk:
        return Response({"error": "Primary key (pk) is required in the request body."}, status=status.HTTP_400_BAD_REQUEST)
   
    try:
        instance = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "Instance with the provided primary key does not exist."}, status=status.HTTP_404_NOT_FOUND)
    new_role_id = request.data.get('role_id')
    if new_role_id is None:
            return Response({"message": "Role ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
            new_role_id = int(new_role_id)
    except ValueError:
            return Response({"message": "Invalid role ID"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
            instance.role_id = new_role_id
            instance.save()
            serializer = UserSerializer(instance)
            return Response(serializer.data)
    except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer =UserRoleSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#----------------------------------------#Update Blog/Reject-Approve oldu-----------------------------------------




#{   example data: id dediğimiz blogun idsi gelcek, bu body ile
    # "id":1,
    # "is_approved":false
    # }
@api_view(['PUT'])
def approvePost(request):
    pk = request.data.get('id')
    if not pk:
        return Response({"error": "Primary key (pk) is required in the request body."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        instance = Blog.objects.get(pk=pk)
        instance.is_approved=True
        instance.is_rejected=False
    except Blog.DoesNotExist:
        return Response({"error": "Instance with the provided primary key does not exist."}, status=status.HTTP_404_NOT_FOUND)

    serializer =BlogSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def deletePost(request):
    pk = request.data.get('id')  # Get pk from request data
    if pk is None:
        return Response({'error': 'Primary key (pk) not provided in the request body'}, status=400)
    
    try:
        instance = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({'error': 'Object does not exist'}, status=404)

    serializer = BlogSerializer(instance)
    instance.delete()
    return Response(serializer.data, status=204)

def deletePostX(requests):
    url = 'http://127.0.0.1:8081/deletePost'  # Replace this with the actual API endpoint
   # headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}  # If required, replace this with your authorization header
    params = {'id': 1, }  # If required, add any parameters
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        # Process the data or return it as it is
        return Response(data)
    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        return Response({'error': str(e)}, status=500)


@api_view(['PUT'])
def rejectPost(request):
    pk = request.data.get('id')
    if not pk:
        return Response({"error": "Primary key (pk) is required in the request body."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        instance = Blog.objects.get(pk=pk)
 
        if(instance.rejection_number>1):
           
            print("")#call Rayan's API 
            
        else : 
            instance.is_approved=False
            instance.is_rejected=True
            instance.ready=False
            instance.rejection_number= instance.rejection_number+1
        
    except Blog.DoesNotExist:
        return Response({"error": "DELETED"})

    serializer =BlogSerializer(instance, data=request.data)
    if serializer.is_valid():
        if(instance.rejection_number<=1):
            serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


     
#----------------------------------------#Admin add user------------------------------------------
@csrf_exempt
@api_view(['POST'])
def adminAddUser(request):
    
  if request.method == 'POST':
        request.data['date_created'] = timezone.now().date()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
          
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            snippet_listPOST(request)
            #return render(request, 'moderator.html', {'model_instance': model_instance})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


     
#----------------------------------------#Admin delete user------------------------------------------
  
@api_view(['DELETE'])
def deleteUser(request):
    pk = request.data.get('id')  # Get pk from request data
    if pk is None:
        return Response({'error': 'Primary key (pk) not provided in the request body'}, status=400)
    
    try:
        instance = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'Object does not exist'}, status=404)

    serializer = UserSerializer(instance)
    instance.delete()
    return Response(serializer.data, status=204)



@csrf_exempt
@api_view(['GET'])
def test_api(request):

    return JsonResponse("aaaaaa====test", safe=False)
