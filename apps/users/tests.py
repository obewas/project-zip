from django.test import TestCase, Client
from .models import Project, Profile, Photo
from datetime import datetime
from django.contrib.auth.models import User, Project
from django.contrib.auth import get_user_model
import Json
django.urls import reverse
# Create your tests here.

class ProfileModelTests(TestCase):                                                                                        
    @classmethod                                                                                                          
    def setUpTestData(cls):                                                                                               
        get_user_model().objects.create()                                                                                                                                                                                   

    def test_profile(self):                                                                                    
        profile = get_user_model().objects.last().profile
	
	
class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

class TestViews(TestCase):
    test_project_list_GET(self):
    client = Client()

    response = client.get(reverse('list'))

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'project/project-list.html')


