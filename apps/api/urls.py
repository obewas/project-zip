from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import project_list, project_detail

urlpatterns = [
    path('projects/', project_list, name='api_list'),
    path('project/<int:pk>', project_detail, name='api-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)