from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from .models import Blog, File
from .serializers import BlogSerializer
from .utils import delete_file_placeholder, BlogProcessor, ApiResponse, latest_magazine_querydict

from django.db import transaction, IntegrityError
from django.db.models import Subquery


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def magazine_feed(request: Request) -> Response:
    """
    API view to read blogs. Implements a 10 blog pagination and fetches 
        associated files for each blog. Only approved non-draft blogs are displayed.

    Parameters:
        request (Request): User request handled by the framework.
    Returns:
        Response: JSON object containing count, blogs, and next url.
    """
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        blogs = Blog.objects.defer(
            'keywords',
            'reader_ids'
        ).filter(
            is_draft=False, 
            is_approved=True,
            magazine_id=Subquery(latest_magazine_querydict()) 
        ).prefetch_related('files').all() 
        result_page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def archived_magazine(request: Request) -> Response: 
    """
    API view to read blogs of an archived magazine. Implements a 10 blog pagination and 
        fetches associated files for each blog. Only approved non-draft blogs are displayed.

    Parameters:
        request (Request): User request handled by the framework.
    Returns:
        Response: JSON object containing count, blogs, and next url.
    """
    if request.method == 'GET':
        magazine_id = request.data['id'] 
        paginator = PageNumberPagination()
        paginator.page_size = 10
        blogs = Blog.objects.defer(
            'keywords',
            'reader_ids'
        ).filter(
            is_draft=False, 
            is_approved=True,
            magazine_id=magazine_id
        ).prefetch_related('files').all() 
        result_page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def user_blogs(request: Request) -> Response:
    """
    API view to read a user's blogs. Implements a 10 blog pagination and fetches 
        associated files for each blog. Only approved non-draft blogs are displayed.

    Parameters:
        request (Request): User request handled by the framework.
    Returns:
        Response: JSON object containing count, blogs, and next url.
    """
    if request.method == 'GET':
        user_id = request.data['id']
        paginator = PageNumberPagination()
        paginator.page_size = 10
        blogs = Blog.objects.defer(
            'keywords',
            'reader_ids'
        ).filter(
            user_id=user_id,
            is_draft=False, 
            is_approved=True
        ).prefetch_related('files').all() 
        result_page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@renderer_classes([JSONRenderer]) 
def user_drafts(request: Request) -> Response:
    """
    API view to read the current user's drafts. Implements a 10 
        draft pagination and fetches associated files for each draft. 

    Parameters:
        request (Request): User request handled by the framework.
    Returns:
        Response: JSON object containing count, blogs, and next url.
    """
    if request.method == 'GET':
        user_id = request.data['id']
        paginator = PageNumberPagination()
        paginator.page_size = 10
        drafts = Blog.objects.defer(
            'keywords',
            'reader_ids'
        ).filter(
            user_id=user_id,
            is_draft=True, 
        ).prefetch_related('files').all() 
        result_page = paginator.paginate_queryset(drafts, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
            

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def read_blog(request: Request) -> Response:
    """
    API view to read a single blog.

    Parameters:
        pk (int): Blog's author primary key/id.
        request (Request): User request handled by the framework.
    Returns:
        Response: JSON object containing all the blog's fields.
    """
    if request.method == 'GET':
        blog_id = request.data['id']
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response(ApiResponse.NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST']) 
@renderer_classes([JSONRenderer]) 
def create_blog(request: Request) -> Response:
    """
    API view to create blogs. The API handles text, images, videos, and stores the files' respective 
        uids in the DB to keep the layout of the blog consistent. Works for both drafting and posting.

    Parameters:
        request (Request): User request handled by the framework.
    Returns:
        Response: A response object indicating the status of the operation.
    """
    if request.method == 'POST':
        data       = request.data
        files      = request.FILES
        serializer = BlogSerializer(data=data)
        try:
            with transaction.atomic():
                response = BlogProcessor.process_blog_data(
                    "POST", 
                    serializer, 
                    data, 
                    files
                )
                return response
        except IntegrityError:
            return Response(ApiResponse.SERIALIZER_ERROR, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
@renderer_classes([JSONRenderer])
def update_blog(request: Request) -> Response:
    """
    API view to update blogs. This view is very similar to the blog creation as the only aspect where both 
        APIs differ is that we need to fetch an existing blog in this view. Works for updating drafts and blogs.

    Parameters:
        request (Request): User request handled by the framework.
    Returns:
        Response: A response object indicating the status of the operation.
    """
    if request.method == 'PUT':
        data = request.data
        try:
            blog = Blog.objects.get(pk=data['id'])
        except Blog.DoesNotExist:
            return Response(ApiResponse.NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        files = request.FILES
        serializer = BlogSerializer(blog, data=data)
        try:
            with transaction.atomic():
                response = BlogProcessor.process_blog_data(
                    "PUT", 
                    serializer, 
                    data, 
                    files
                )
                return response
        except IntegrityError:
            return Response(ApiResponse.SERIALIZER_ERROR, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_blog(request: Request) -> Response:
    """
    API view to delete a blog. 

    Parameters:
        request (Request): User request handled by the framework.
    Returns:
        Response: A response object indicating the status of the operation.
    """
    if request.method == 'DELETE':
        blog_id = request.data['id']
        try: 
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response(ApiResponse.NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def delete_file(request: Request) -> Response:
    """
    API view to delete a file in a blog. This api can be called to delete a specific file in 
        a blog and it also deletes the file uid used as a placeholder for the image in the text.

    Parameters:
        request (Request): User request handled by the framework.
    Returns:
        Response: A response object indicating the status of the operation.
    """
    if request.method == 'DELETE':
        file_id = request.data['id']
        try: 
            file = File.objects.get(pk=file_id)
        except Blog.DoesNotExist:
            return Response(ApiResponse.NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        try:
            with transaction.atomic():
                blog = file.blog
                blog.content = delete_file_placeholder(
                    blog.content, 
                    file.uid
                )
                blog.save()
                file.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except IntegrityError:
            return Response(ApiResponse.FILE_DELETE_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)