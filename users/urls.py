from users.views import dashboard, register
from django.urls import path, include

urlpatterns = [
   path("accounts/", include("django.contrib.auth.urls")),
   path('dashboard/', dashboard, name='dashboard' ),
   path('register/', register, name="register"),
   
]