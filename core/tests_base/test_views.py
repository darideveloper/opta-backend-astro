from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class ViewsBaseTestCase(APITestCase):

    def setUp(
        self,
        endpoint: str = "/api/",
        restricted_get: bool = True,
        restricted_post: bool = True,
        restricted_put: bool = True,
        restricted_delete: bool = True,
        restricted_unauthenticated_get: bool = True,
    ):
        """
        Set up the test case with a test user and token.

        Args:
            endpoint (str, optional): The endpoint to test. Defaults to None.
            restricted_get (bool, optional): Whether GET requests are restricted.
                Defaults to True.
            restricted_post (bool, optional): Whether POST requests are restricted.
                Defaults to True.
            restricted_put (bool, optional): Whether PUT requests are restricted.
                Defaults to True.
            restricted_delete (bool, optional): Whether DELETE requests are restricted.
                Defaults to True.
            restricted_unauthenticated_get (bool, optional):
                Whether unauthenticated GET requests are restricted. Defaults to True.
        """

        # Create a test user
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            first_name="Test",
            last_name="User",
            is_staff=True,
        )

        # Get token
        token = self.client.post(
            "/api/login/",
            data={"username": self.username, "password": self.password},
            format="json",
        ).data["token"]

        # Save the token for later use
        self.token = token
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

        # Save endpoint for later use
        self.endpoint = endpoint

        # Save restrictions for later use
        self.restricted_get = restricted_get
        self.restricted_post = restricted_post
        self.restricted_put = restricted_put
        self.restricted_delete = restricted_delete
        self.restricted_unauthenticated_get = restricted_unauthenticated_get

    def validate_invalid_method(self, method: str):
        """Validate that the given method is not allowed on the endpoint"""

        response = getattr(self.client, method)(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_authenticated_user_get(self):
        """Test that authenticated users can not get from the endpoint"""

        if self.restricted_get:
            self.validate_invalid_method("get")

    def test_authenticated_user_post(self):
        """Test that authenticated users can not post to the endpoint"""

        if self.restricted_post:
            self.validate_invalid_method("post")

    def test_authenticated_user_put(self):
        """Test that authenticated users can not put to the endpoint"""

        if self.restricted_put:
            self.validate_invalid_method("put")

    def test_authenticated_user_delete(self):
        """Test that authenticated users can not delete from the endpoint"""

        if self.restricted_delete:
            self.validate_invalid_method("delete")

    def test_unauthenticated_user_get(self):
        """Test unauthenticated user get request"""

        # Remove token from client credentials
        if self.restricted_unauthenticated_get:
            self.client.credentials(HTTP_AUTHORIZATION="")

            # Make request
            response = self.client.get(self.endpoint)

            # Check response
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
