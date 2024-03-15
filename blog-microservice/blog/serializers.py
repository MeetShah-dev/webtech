import json

from rest_framework import serializers
from django.utils import timezone

from .models import Blog, File, User, Category, Magazine


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(format='hex_verbose')
    
    class Meta:
        model = File
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    reader_ids = serializers.ListField(child=serializers.CharField(), required=False)
    keywords = serializers.ListField(child=serializers.CharField(), required=False)
    files = FileSerializer(many=True, read_only=True)
    
    def to_internal_value(self, data: dict) -> dict:
        """
        Override this method to support deserialization, for write operations. 
            This is as keywords and reader_ids are lists sent by the client as strings.

        Parameters:
            data (dict): data before serialization.

        Returns:
            dict: deserialized validated data to be stored in the DB.
        """
        keywords        = data.get('keywords', False)
        reader_ids      = data.get('reader_ids', False)
        validated_data  = super(BlogSerializer, self).to_internal_value(data)

        if keywords and type(keywords) is not list: 
            keywords_list = json.loads(keywords)
            validated_data['keywords'] = keywords_list

        if reader_ids and type(reader_ids) is not list: 
            reader_ids_list = json.loads(reader_ids)
            validated_data['reader_ids'] = reader_ids_list

        return validated_data

    def create(self, validated_data: dict) -> Blog:
        """
        Override this method to support saving instances. This is as 
            both date_created and is_approved fields must be handle by the server.

        Parameters: 
            validated_data (dict): The validated data to create a new instance.

        Returns:
            Blog: A blog instance created with the validated data.
        """
        validated_data['date_created'] = timezone.now()
        validated_data['is_approved'] = False 
        return Blog.objects.create(**validated_data)

    class Meta:
        model = Blog
        fields = [
            'id', 
            'user', 
            'magazine', 
            'category', 
            'title', 
            'content', 
            'is_approved',
            'is_draft', 
            'reader_ids', 
            'keywords', 
            'files'
        ]
