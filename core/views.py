from rest_framework import viewsets
from django.contrib.auth.models import User

from core import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):

        queryset = User.objects.filter(id=self.request.user.id)

        # submomento_id = self.request.GET.get("submomento_id")
        # if submomento_id:
        #     return queryset.filter(submomento_id=submomento_id)

        return queryset
