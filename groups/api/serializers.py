from rest_framework import serializers
from ..models import Group
from django.utils.text import slugify
from accounts.api.serializers import ProfileSerializer,AccountSerializer
from posts.api.serializers import  PostSerializer


class GroupSerializer(serializers.ModelSerializer):
    #members = AccountSerializer(many=True)
    #posts = PostSerializer(many=True)
    class Meta:
        model = Group
        fields = ['id','slug','name','description','members','posts']
        # depth = 2




        # depth = 2