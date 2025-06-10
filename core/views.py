from rest_framework import viewsets

from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from core import serializers


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):

        queryset = User.objects.filter(id=self.request.user.id)

        # submomento_id = self.request.GET.get("submomento_id")
        # if submomento_id:
        #     return queryset.filter(submomento_id=submomento_id)

        return queryset


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        
        # Get username from post data
        username = request.data.get("username")
        
        # First, delete any existing token for the user (if it exists)
        try:
            token = Token.objects.get(user__username=username)
            print(token)
            token.delete()
        except Token.DoesNotExist:
            pass
        
        # Now, proceed with the regular token creation process
        response = super().post(request, *args, **kwargs)
        
        # Get the newly created token
        token = Token.objects.get(key=response.data['token'])
        
        # return token
        response.data['token'] = token.key
        
        return response