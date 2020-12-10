from rest_framework import serializers
from ..models import Group
from accounts.api.serializers import ProfileSerializer
from posts.api.serializers import  PostSerializer


class GroupSerializer(serializers.ModelSerializer):
    members = ProfileSerializer(many=True)
    posts = PostSerializer(many=True)
    class Meta:
        model = Group
        fields = ['id','slug','name','description','members','posts']

