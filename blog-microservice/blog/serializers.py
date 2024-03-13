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
    reader_ids = serializers.ListField(child=serializers.CharField())
    keywords = serializers.ListField(child=serializers.CharField())
    files = FileSerializer(many=True, read_only=True)
    
    def to_internal_value(self, data):
        keywords        = data.get('keywords')
        reader_ids      = data.get('reader_ids')
        validated_data  = super().to_internal_value(data)

        if type(keywords) is not list: 
            keywords_list = json.loads(keywords)
            validated_data['keywords'] = keywords_list

        if type(reader_ids) is not list: 
            reader_ids_list = json.loads(reader_ids)
            validated_data['reader_ids'] = reader_ids_list

        return validated_data

    def create(self, validated_data):
        validated_data['date_created'] = timezone.now()
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