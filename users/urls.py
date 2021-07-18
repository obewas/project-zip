from users.views import dashboard, register, profile, ProjectListView
from django.urls import path, include

urlpatterns = [
   path('', ProjectListView.as_view(), name='home'),
   path("accounts/", include("django.contrib.auth.urls")),
   path('dashboard/', dashboard, name='dashboard'),
   path('register/', register, name="register"),
   path('profile/', profile, name='profile'),
   
]