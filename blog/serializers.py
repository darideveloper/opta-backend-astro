import json

from rest_framework import serializers

from blog import models
from utils.media import get_media_url


class PostListItemSerializer(serializers.ModelSerializer):
    """ Api serializer for Post model """
    
    class Meta:
        model = models.Post
        fields = (
            "id",
            "title",
            "lang",
            "banner_image_url",
            "description",
            "author",
            "created_at",
            "updated_at",
        )


class PostDetailSerializer(PostListItemSerializer):
    """ Api serializer for Post model """
    
    video_url = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()
    keywords = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Post
        fields = "__all__"
        
    def get_keywords(self, obj):
        """ Get keywords values """
        keywords_json = obj.keywords
        keywords = json.loads(keywords_json)
        keywords_values = [keyword["value"] for keyword in keywords]
        return keywords_values
    
    def get_video_url(self, obj):
        """ Get video url """
        return get_media_url(obj.video_file)
    
    def get_pdf_url(self, obj):
        """ Get PDF url """
        return get_media_url(obj.pdf_file)
