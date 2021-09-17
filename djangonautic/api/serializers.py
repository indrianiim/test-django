from rest_framework import serializers
from django.db.models import fields
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner'
        )