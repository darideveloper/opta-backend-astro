from django.urls import path, include

from rest_framework import routers
from core import views

router = routers.DefaultRouter()


router.register(r'user', views.UserViewSet, 'user')

urlpatterns = [
    path('api/', include(router.urls)),
]
