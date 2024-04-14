from django.urls import path
from moderatorAdmin import views

urlpatterns = [
    path("getComments", views.getComments, name="getComments"), #get comments
    path("deleteComment", views.deleteComment, name="deleteComment") ,#deletecomment

    #Moderator can add categories, get all categoires, post many categories(optional)
    path("addCategory", views.addCategory, name="addCategory"), #add categories (general)
    path("getAllCategories", views.get_all_categories, name="getAllCategories"), #add categories
    path("postManyCategories", views.postManyCategories, name="postManyCategories"), #settallcategories

     path("addCategoryToBlog", views.addCategoryToBlog, name="addCategoryToBlog"), #add category to blog #bunu ekledim
    
    path("rejectPost", views.rejectPost, name="rejectPost"), #rejecting or approving blogs, user'a delete gidicek, hepsine id eklencek
    path("approvePost", views.approvePost, name="approvePost"), #rejecting or approving blogs, user'a notification gidicek, hepsine id eklencek
    path("getReadyPosts", views.getReadyPosts, name="getReadyPosts"), #notification gidice, hepsine id eklencek
    path("postFeedback", views.postFeedback, name="postFeedback"), #posting the feedback, user'a notification gidicek, id eklencek
    #path("deletePost", views.deletePost, name="deletePost"), #deletePost
    
    #Admin    
    path("changeRole", views.changeRole, name="changeRole"), #change role (remove moderator)#ADMIN, user' a notification gidicek, id eklencek
    path("getAllUsers", views.getAllUsers, name="getAllUsers"), #getAllTheUsers
    
    path("testApi", views.test_api, name="testApi"), #deletePost
    
   
    
]#
