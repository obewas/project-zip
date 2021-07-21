from django.test import TestCase
from .models import Project, Profile, Photo
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your tests here.

class ProfileModelTests(TestCase):                                                                                        
    @classmethod                                                                                                          
    def setUpTestData(cls):                                                                                               
        get_user_model().objects.create()                                                                                                                                                                                   

    def test_profile(self):                                                                                    
        profile = get_user_model().objects.last().profile
	
	
