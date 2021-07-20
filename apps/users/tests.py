from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Project, Profile

# Create your tests here.
User = get_user_model()
class ProjectApiTestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='John', email='obewas@gmail.com')
        user_obj.set_password('tested1234')
        user_obj.save()
        project = Project.objects.create(
            user=user_obj,
            profile=Profile.owner,
            title='New title',
            description='some_random_content',
            project_image='picture.jpg',
            link='connectedurl',
            rating=5,
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)


