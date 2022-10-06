from rest_framework import serializers

from .models import Article


# class ArticleModel:
#     def __init__(self, title, text, slug):
#         self.title = title
#         self.text = text
#         self.slug = slug


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "text", "photo", "slug")
