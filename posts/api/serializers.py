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
    groupname = serializers.SerializerMethodField("get_groupname")
    # group = AttrPKField()
    class Meta:
        model = Post
        fields = ['id','title','message','groupname','group','username','updated_at','slug']

    def get_username(self,post):
        username = post.user.username
        return username

    def get_groupname(self,post):
        groupname = post.group.name if post.group != None else None
        return groupname




class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','message']