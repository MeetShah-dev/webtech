from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('magazine-feed/', views.magazine_feed),
    path('read-blog/', views.read_blog),
    path('create-blog/', views.create_blog),
    path('update-blog/', views.update_blog),
    path('delete-blog/', views.delete_blog),
    path('delete-file/', views.delete_file),
]


