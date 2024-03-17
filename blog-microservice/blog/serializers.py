import json

from rest_framework import serializers
from django.utils import timezone

from .models import Blog, File


class FileSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(format='hex_verbose')
    
    class Meta:
        model = File
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(required=False)
    reader_ids   = serializers.ListField(child=serializers.CharField(), required=False)
    keywords     = serializers.ListField(child=serializers.CharField(), required=False)
    files        = FileSerializer(many=True, read_only=True)
    
    def to_internal_value(self, data: dict) -> dict:
        """
        Overrides to_internal_value to support deserialization, for write operations. This is as both 
            keywords and reader_ids are lists sent by the client as strings that should be treated as python objects.

        Parameters:
            data (dict): input data from the client request.

        Returns:
            dict: deserialized validated data to be stored in the DB.
        """
        keywords        = data.get('keywords', False)
        reader_ids      = data.get('reader_ids', False)
        validated_data  = super(BlogSerializer, self).to_internal_value(data)

        if keywords and type(keywords) is not list: 
            try:
                keywords_list = json.loads(keywords)
                validated_data['keywords'] = keywords_list
            except json.JSONDecodeError:
                raise serializers.ValidationError({
                    'keywords': 'Must be a valid JSON list string.'
                })

        if reader_ids and type(reader_ids) is not list: 
            try:
                reader_ids_list = json.loads(reader_ids)
                validated_data['reader_ids'] = reader_ids_list
            except json.JSONDecodeError:
                raise serializers.ValidationError({
                    'reader_ids': 'Must be a valid JSON list string.'
                })

        return validated_data

    def create(self, validated_data: dict) -> Blog:
        """
        Overrides create to support saving instances. This is as 
            both date_created and is_approved fields must be handled by the server.

        Parameters: 
            validated_data (dict): The validated data to create a new instance.

        Returns:
            Blog: A blog instance created with the validated data.
        """
        validated_data['date_created'] = timezone.now()
        validated_data['is_approved'] = False 
        return Blog.objects.create(**validated_data)
    
    def update(self, instance: Blog, validated_data: dict) -> Blog:
        """
        Overrides update to support updating instances. This is as 
            both date_updated and is_approved fields must be handled by the server.

        Parameters: 
            instance (Blog): The instance to be updated.
            validated_data (dict): The validated data to create a new instance.

        Returns:
            Blog: A blog instance created with the validated data.
        """
        # fields values sent by the client 
        instance.title        = validated_data.get('title', instance.title)
        instance.content      = validated_data.get('content', instance.content)
        instance.is_draft     = validated_data.get('is_draft', instance.is_draft)
        instance.keywords     = validated_data.get('keywords', instance.keywords)
        instance.category     = validated_data.get('category', instance.category)
        # fields values handled by the server
        instance.is_approved  = False
        instance.date_updated = timezone.now()

        instance.save()
        return instance

    class Meta:
        model = Blog
        fields = [
            'id', 
            'user', 
            'magazine', 
            'category', 
            'title', 
            'content', 
            'date_created',
            'date_updated',
            'is_approved',
            'is_draft', 
            'reader_ids', 
            'keywords', 
            'files'
        ]
