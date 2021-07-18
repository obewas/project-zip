from users.views import dashboard, register, profile
from django.urls import path, include

urlpatterns = [
   path("accounts/", include("django.contrib.auth.urls")),
   path('dashboard/', dashboard, name='dashboard' ),
   path('register/', register, name="register"),
   path('profile/', profile, name='profile'),
   
]