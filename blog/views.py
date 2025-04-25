import requests

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.conf import settings

from blog import serializers
from blog import models


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """Api viewset for Post model"""

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostListItemSerializer

    def get_queryset(self):
        """filter with get parameters"""
        queryset = models.Post.objects.filter(is_active=True).order_by("-updated_at")

        # Get lang rrom headers Accept-Language
        # lang = self.request.META.get("HTTP_ACCEPT_LANGUAGE", None)

        # # Filter by lang
        # if lang is not None:
        #     queryset = queryset.filter(lang=lang)

        # return queryset
        return queryset

    def get_serializer_class(self, *args, **kwargs):
        """Return serializer class"""
        if "details" in self.request.query_params:
            return serializers.PostDetailSerializer
        if "summary" in self.request.query_params:
            return serializers.PostListItemSerializer
        return self.serializer_class


class DownloadFileView(APIView):
    def post(self, request):
        """Download file from URL and return it as a response"""

        serializer = serializers.FileURLSerializer(data=request.data)
        if serializer.is_valid():

            # Get url file
            file_url = serializer.validated_data["url"]

            # Check if the URL is valid
            if settings.DOWNLOAD_FILES_DOMAIN not in file_url:
                return Response(
                    {"error": "Invalid URL domain"}, status=status.HTTP_400_BAD_REQUEST
                )

            # Download the file and return it
            try:
                r = requests.get(file_url, stream=True)
                r.raise_for_status()
                filename = file_url.split("/")[-1] or "downloaded_file"
                content_type = r.headers.get("Content-Type", "application/octet-stream")
                response = HttpResponse(r.content, content_type=content_type)
                response["Content-Disposition"] = f'attachment; filename="{filename}"'
                return response
            except requests.RequestException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
