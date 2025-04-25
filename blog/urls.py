from django.urls import path, include

from rest_framework import routers
from blog import views

router = routers.DefaultRouter()

router.register(r'posts', views.PostViewSet, 'posts')

urlpatterns = [
    path('', include(router.urls)),
    path('download-file/', views.DownloadFileView.as_view(), name='download-file'),
]
