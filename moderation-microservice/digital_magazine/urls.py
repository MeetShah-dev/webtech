from django.urls import path
from moderatorAdmin import views

urlpatterns = [
    # path("home", views.home, name="home"), #taking the home function of view without /
    # path("home_view", views.home_view, name="home_view"), #taking the home function of view without /
    # path("test", views.test_api, name="test_api"), #taking the home function of view without /
    # path("list", views.snippet_list, name="snippet_list"), #taking the home function of view without /
    # path("post", views.snippet_listPOST, name="snippet_listPOST"), #taking the home function of view without /
    #path("postFeedback", views.postFeedback, name="postFeedback"), #taking the home function of view without /
    #path("deleteUser", views.deleteUser, name="deleteUser"), #taking the home function of view without /
    # path("addComment", views.addComment, name=" addComment"), #add comment
   
    


    path("changeRole", views.changeRole, name="changeRole"), #change role (remove moderator)#ADMIN 


    #path("banUser", views.banUser, name="banUser"), #tbanUser #at least for now deleted
     
    #path("adminAddUser", views.adminAddUser, name="adminAddUser"), #at least it is deleted, UI 
    #path("changeSchedule", views.changeScheduleOfMagazine, name="changeSchedule"), #changing the schedule of magazine

    #path("rejectOrApprove", views.rejectOrApprove, name="rejectOrApprove"), #rejecting or approving blogs
    path("postFeedback", views.postFeedback, name="postFeedback"), #posting the feedback
    path("getComments", views.getComments, name="getComments"), #get comments
    path("deleteComment", views.deleteComment, name="deleteComment") ,#deletecomment
    path("addCategory", views.addCategory, name="addCategory"), #add categories (general)
    path("getAllCategories", views.get_all_categories, name="getAllCategories"), #add categories
    path("postManyCategories", views.postManyCategories, name="postManyCategories"), #settallcategories
    path("getAllUsers", views.getAllUsers, name="getAllUsers"), #getAllTheUsers

    path("rejectPost", views.rejectPost, name="rejectPost"), #rejecting or approving blogs
    path("approvePost", views.approvePost, name="approvePost"), #rejecting or approving blogs
    path("deletePost", views.deletePost, name="deletePost"), #deletePost
    path("getReadyPosts", views.getReadyPosts, name="getReadyPosts"), #deletePost
    path("testApi", views.test_api, name="testApi"), #deletePost
    
   
    
]#