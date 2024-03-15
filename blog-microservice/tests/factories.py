import os
import uuid
import json
import factory

from faker import Faker
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

from blog.models import Blog, File, User, Magazine, Category, Role

fake = Faker()


class FileGenerator:
    @staticmethod
    def upload_image() -> SimpleUploadedFile:
        """
        Utility method to generate an image.

        Returns:
            SimpleUploadedFile: The image file.
        """
        file_path = os.path.join(os.getcwd(), "tests\\blog\\files\\img1.jpeg")
        with open(file_path, 'rb') as f:
            file_content = f.read()
            file = SimpleUploadedFile("img1.jpeg", file_content, content_type="image/jpeg")
        return file

    @staticmethod
    def upload_video() -> SimpleUploadedFile:
        """
        Utility method to generate a video.

        Returns:
            SimpleUploadedFile: The video file.
        """
        file_path = os.path.join(os.getcwd(), "tests\\blog\\files\\vid1.mp4")
        with open(file_path, 'rb') as f:
            file_content = f.read()
            file = SimpleUploadedFile("vid1.mp4", file_content, content_type="video/mp4")
        return file


class DataGenerator:
    @staticmethod
    def data_with_files(blog: 'BlogFactory') -> dict:
        """
        Utility method to generate data including files in a multipart format.

        Parameters:
            blog (BlogFactory): Used to create blogs.

        Returns:
            dict: The multipart data.
        """
        placeholder1 = str(uuid.uuid4())
        placeholder2 = str(uuid.uuid4())
        content = fake.paragraph() + placeholder1 + fake.paragraph() + placeholder2 + fake.paragraph()

        data = {
            "user": blog.user.id,
            "magazine": blog.magazine.id,
            "category": blog.category.id,
            "title": blog.title,
            "content": content,
            "is_draft": False,
            "reader_ids": json.dumps(blog.reader_ids), 
            "keywords": json.dumps(blog.keywords), 
            'file_placeholders': json.dumps([
                {'file1': placeholder1},
                {'file2': placeholder2},
            ]),
            'file1': FileGenerator.upload_image(),
            'file2': FileGenerator.upload_video()
        }
        return data

    @staticmethod
    def data_text(blog: 'BlogFactory') -> dict:
        """
        Utility method to generate data in a multipart format.
        
        Parameters:
            blog (BlogFactory): Used to create blogs.

        Returns:
            dict: The multipart data.
        """
        data = {
            "user": blog.user.id,
            "magazine": blog.magazine.id,
            "category": blog.category.id,
            "title": blog.title,
            "content": blog.content,
            "is_draft": False,
            "reader_ids": json.dumps(["reader1", "reader2"]), 
            "keywords": json.dumps(["keyword1", "keyword2"]), 
        }
        return data
    

class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role

    name = "user"
    privilege_properties = json.dumps({"privilege": "basic"})


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name          = fake.first_name()
    last_name           = fake.last_name()
    email               = factory.Sequence(lambda n: f"email{n}@example.com")
    date_of_birth       = fake.date_of_birth(minimum_age=18, maximum_age=90)
    date_created        = timezone.now()
    last_login_date     = timezone.now()
    email_notification  = True
    profile_photo       = FileGenerator.upload_image()
    nationality         = fake.country()
    type                = fake.random_element(elements=('Student', 'Staff'))
    gender              = fake.random_element(elements=('Male', 'Female'))

    role                = factory.SubFactory(RoleFactory)


class MagazineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Magazine

    title           = "Students' Struggles"
    flag            = "Upcoming"
    date_created    = timezone.now()
    date_released   = timezone.now()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Studies"


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    # is_approved is True on creation, only for testing purposes
    title        = fake.sentence()
    content      = fake.paragraph()
    is_approved  = True 
    is_draft     = False
    date_created = timezone.now()
    reader_ids   = [[fake.random_number(digits=5) for _ in range(2)]]
    keywords     = [fake.word() for _ in range(2)]

    user         = factory.SubFactory(UserFactory)
    magazine     = factory.SubFactory(MagazineFactory)
    category     = factory.SubFactory(CategoryFactory)


class DraftFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title        = fake.sentence()
    content      = fake.sentence()
    is_approved  = False 
    is_draft     = True
    date_created = timezone.now()

    user         = factory.SubFactory(UserFactory)
    magazine     = factory.SubFactory(MagazineFactory)
    category     = factory.SubFactory(CategoryFactory)


class FileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = File

    uid = uuid.uuid4()
    url = FileGenerator.upload_video()

    blog = factory.SubFactory(BlogFactory)

    @factory.post_generation
    def edit_related_blog(instance, create, extracted, **kwargs):
        if create:
            extra_content = str(instance.uid) + fake.paragraph()
            instance.blog.content += extra_content
            instance.blog.save()