from rest_framework.urlpatterns import format_suffix_patterns
from .views import dashboard, register, profile, ProjectList, ProjectDetail, UserDetail, ProfileList
from django.urls import path, include

urlpatterns = [
   path('', ProjectList.as_view(), name='home'),
   path("accounts/", include("django.contrib.auth.urls")),
   path('dashboard/', dashboard, name='dashboard'),
   path('register/', register, name="register"),
   path('profile/', profile, name='profile'),

   path('projects/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
   path('users/', ProfileList.as_view()),
   path('users/<int:pk>/', UserDetail.as_view()),
   
]
urlpatterns = format_suffix_patterns(urlpatterns)