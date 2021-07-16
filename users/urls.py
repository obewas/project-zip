from users.views import dashboard
from django.urls import path

urlpatterns = [
   path("accounts/", include("django.contrib.auth.urls")),
   path('dashboard/', dashboard, name='dashboard' ),
]