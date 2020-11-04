from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField("get_username")
    class Meta:
        model = Post
        fields = ['title','message','group','username']

    def get_username(self,post):
        username = post.user.username
        return username



class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','message']