from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class ViewsBaseTestCase(APITestCase):
    
    def setUp(self, endpoint: str = "/api/"):
        """
        Set up the test case with a test user and token.
        
        Args:
            endpoint (str, optional): The endpoint to test. Defaults to None.
        """
        
        # Create a test user
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            first_name="Test",
            last_name="User",
            is_staff=True
        )
        
        # Get token
        token = self.client.post(
            "/api/login/",
            data={
                "username": self.username,
                "password": self.password
            },
            format='json'
        ).data['token']
        
        # Save the token for later use
        self.token = token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        
        # Save endpoint for later use
        self.endpoint = endpoint