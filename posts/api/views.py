from django.http import Http404
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Post
from .serializers import PostSerializer,PostUpdateSerializer
from django.contrib.auth import models

account = models.User.objects.get(username='bikrant')
print(account)

class PostList(APIView):

    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)


    def post(self,request):
        pass

class PostUpdate(APIView):

    def put(self,request,pk):
        post = Post.objects.get(pk)
        grp=post.group
        usr=post.user
        serializer = PostUpdateSerializer(post,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT',])
def api_update_postview(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PostUpdateSerializer(post,data=request.data)
        #print(serializer.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"]="update was successful"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
def api_delete_postview(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "DELETE":
        operation = post.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['POST',])
def api_create_postview(request):
    account = models.User.objects.get(username='bikrant')
    post = Post(user=account)
    if request.method == "POST":
        serializer = PostUpdateSerializer(post,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#    account = User.objects.get(pk=1)
