
from . import views
from django.urls import path, include

urlpatterns = [
   path('', views.view_profile, name='home'),
   path("accounts/", include("django.contrib.auth.urls")),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('register/', views.register, name="register"),
   path('profile/', views.profile, name='profile'),
   path('upload/', views.upload, name='upload'),
 
   path('project', views.ProjectListView.as_view(), name='project-list'),
   path('create', views.create_project, name='create'),
   path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
   path('project/<int:pk>/update', views.ProjectUpdateView.as_view(), name='project-update'),
   path('project/<int:pk>/', views.delete_project, name='project-delete'),
   path('project/search/', views.SearchResultsView.as_view(), name='search'),
   path('<int:id>/grade', views.project_grading, name='grades'),

]
