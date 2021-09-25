from rest_framework import serializers
from ..models import Post
from groups.models import Group


# class AttrPKField(serializers.PrimaryKeyRelatedField):
#
#     def get_queryset(self):
#         user = serializers.CurrentUserDefault()
#         queryset = Group.objects.filter(members=user)
#         return queryset



class PostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField("get_username")
    # group = AttrPKField()
    class Meta:
        model = Post
        fields = ['id','title','message','group','username','updated_at']

    def get_username(self,post):
        username = post.user.username
        return username



class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','message']