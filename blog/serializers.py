import json

from rest_framework import serializers

from blog import models


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