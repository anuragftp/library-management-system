from django.urls import path
from user.views import ProfileView,ProfileEditView
from django.contrib.auth.decorators import login_required
urlpatterns = [
   
   path('lmb/<str:username>/',login_required(ProfileView.as_view()),name='profile_view'),
   path('feed/<str:username>/edit/',login_required(ProfileEditView.as_view()),name='profile_edit_view')
  
   
]
