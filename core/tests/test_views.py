from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from core.tests_base.test_views import ViewsBaseTestCase


class CustomObtainAuthTokenTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.username = "testuser"
        cls.password = "testpassword"
        cls.user = User.objects.create_user(
            username=cls.username,
            password=cls.password
        )
        
        # Setup endpoints
        cls.token_obtain_url = "/api/login/"

    def test_obtain_token(self):
        """
        Test obtaining a token with valid credentials.
        """
        response = self.client.post(
            self.token_obtain_url,
            data={
                "username": self.username,
                "password": self.password
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        
    def test_obtain_token_invalid_credentials(self):
        """
        Test obtaining a token with invalid credentials.
        """
        
        response = self.client.post(
            self.token_obtain_url,
            data={
                "username": self.username,
                "password": "wrongpassword"
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)
        self.assertIn('non_field_errors', response.data)
        
    def test_recreate_token(self):
        """
        Test recreating a token for an existing user.
        """
        # First, obtain a token
        response = self.client.post(
            self.token_obtain_url,
            data={
                "username": self.username,
                "password": self.password
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        initial_token = response.data['token']
        
        # Now, recreate the token
        response = self.client.post(
            self.token_obtain_url,
            data={
                "username": self.username,
                "password": self.password
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_token = response.data['token']
        
        # Ensure the new token is different from the initial one
        self.assertNotEqual(initial_token, new_token)


class UserViewSetTestCase(ViewsBaseTestCase):
    
    def setUp(self):
        """
        Set up the test case with a test user and token.
        """
        super().setUp("/api/user/")
        
    def test_get_current_user_data(self):
        """
        Test retrieving the current user's data.
        """
        
        # get response
        response = self.client.get(self.endpoint)
                
        # validate response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Validate only response 1 user (the current user)
        self.assertEqual(len(response.data), 1)
        
        # validate user data
        user_data = response.data[0]
        self.assertEqual(user_data['id'], self.user.id)
        self.assertEqual(user_data['username'], self.user.username)
        self.assertEqual(user_data['first_name'], self.user.first_name)
        self.assertEqual(user_data['last_name'], self.user.last_name)
        self.assertEqual(user_data['is_staff'], self.user.is_staff)
