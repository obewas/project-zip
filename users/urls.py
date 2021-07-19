
from . import views
from django.urls import path, include

urlpatterns = [
   path('',views.view_profile, name='home'),
   path("accounts/", include("django.contrib.auth.urls")),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('register/', views.register, name="register"),
   path('profile/', views.profile, name='profile'),


   path('project', views.ProjectListView.as_view(), name='project-list'),
   path('project/create', views.ProjectCreateView.as_view(),name='project-create'),


]
