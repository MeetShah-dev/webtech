import json

from rest_framework import serializers
from django.utils import timezone

from .models import Blog, File, Category, Magazine


class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(format='hex_verbose')
    
    class Meta:
        model = File
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    magazine     = serializers.PrimaryKeyRelatedField(read_only=True)
    category_ids = serializers.ListField(child=serializers.CharField(), required=True, write_only=True)
    reader_ids   = serializers.ListField(child=serializers.CharField(), required=False)
    keywords     = serializers.ListField(child=serializers.CharField(), required=False)
    date_created = serializers.DateTimeField(required=False)
    files        = FileSerializer(many=True, read_only=True)
    categories   = CategorySerializer(many=True, read_only=True)
    
    def to_internal_value(self, data: dict) -> dict:
        """
        Overrides to_internal_value to support deserialization, for write operations. 
            This is as both keywords and reader_ids are lists sent by the client as 
            strings that should be treated as python objects.

        Parameters:
            data (dict): input data from the client request.

        Returns:
            dict: deserialized validated data to be stored in the DB.
        """
        keywords        = data.get('keywords', False)
        reader_ids      = data.get('reader_ids', False)
        category_ids    = data.get('category_ids', False)
        validated_data  = super(BlogSerializer, self).to_internal_value(data)

        if category_ids and type(category_ids) is not list: 
            try:
                category_ids_list = json.loads(category_ids)
                validated_data['category_ids'] = category_ids_list
            except json.JSONDecodeError:
                raise serializers.ValidationError({
                    'category_ids': 'Must be a valid JSON list string.'
                })

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
            This method also creates many to many relationships between the blog
            created and the categories provided based on their ids.

        Parameters: 
            validated_data (dict): The validated data to create a new instance.

        Returns:
            Blog: A blog instance created with the validated data.
        """
        # new posts are associated with the latest upcoming magazine
        magazine = self.__get_latest_upcommig_magazine()

        validated_data['magazine']      = magazine
        validated_data['date_created']  = timezone.now()
        validated_data['is_approved']   = False
        categories = validated_data.pop('category_ids', [])

        blog = Blog.objects.create(**validated_data)

        # bulk creation of many to many table rows
        blog_categories_instances = [
            Blog.categories.through(blog_id=blog.pk, category_id=category_id)
            for category_id in categories
        ]
        Blog.categories.through.objects.bulk_create(blog_categories_instances)

        return blog

    def update(self, instance: Blog, validated_data: dict) -> Blog:
        """
        Overrides update to support updating instances. This is as 
            both date_updated and is_approved fields must be handled by the server.
            This method also updates many to many relationships between the blog
            updated and the categories provided based on their ids.

        Parameters: 
            instance (Blog): The instance to be updated.
            validated_data (dict): The validated data to create a new instance.

        Returns:
            Blog: A blog instance created with the validated data.
        """
        # fields values handled by the server
        instance.is_approved  = False
        instance.date_updated = timezone.now()
        # fields values sent by the client 
        instance.title        = validated_data.get('title', instance.title)
        instance.content      = validated_data.get('content', instance.content)
        instance.is_draft     = validated_data.get('is_draft', instance.is_draft)
        instance.keywords     = validated_data.get('keywords', instance.keywords)

        if 'category_ids' in validated_data:
            new_category_ids     = validated_data.pop('category_ids', [])
            current_category_ids = list(instance.categories.values_list('id', flat=True))
            removed_category_ids = list(set(current_category_ids) - set(new_category_ids))
            new_category_ids     = list(set(new_category_ids) - set(current_category_ids))
            
            # remove categories that aren't present in the updated data
            instance.categories.remove(*removed_category_ids)

            # update of new categories through bulk create
            blog_categories_instances = [
                Blog.categories.through(blog_id=instance.pk, category_id=category_id)
                for category_id in new_category_ids
            ]
            Blog.categories.through.objects.bulk_create(blog_categories_instances)
                
        instance.save()
        return instance
    
    @staticmethod
    def __get_latest_upcommig_magazine() -> Magazine:
        """
        Gets the latest upcoming magazine instance to set the blogs' FK upon their creation.

        Returns:
            Magazine: A magazine instance.
        """
        try:
            magazine = Magazine.objects.filter(
                flag='upcoming'
            ).order_by('-date_released')[:1][0]
            return magazine
        except Magazine.DoesNotExist:
            raise LookupError('Error: There are no upcoming magazines in the database.')

    class Meta:
        model = Blog
        fields = [
            'id', 
            'user', 
            'magazine', 
            'categories', 
            'title', 
            'content', 
            'date_created',
            'date_updated',
            'is_approved',
            'is_draft', 
            'category_ids',
            'reader_ids', 
            'keywords', 
            'files'
        ]
