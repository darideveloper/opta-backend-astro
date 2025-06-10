from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class CustomObtainAuthTokenTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.username = "testuser"
        cls.password = "testpassword"
        cls.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
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
