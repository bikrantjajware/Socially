from django.http import Http404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from ..models import Post
from .serializers import PostSerializer,PostUpdateSerializer
from django.contrib.auth import models

account = models.User.objects.get(username='bikrant')
print(account)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_detail_view(request,slug):
    try:
        userpost = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PostSerializer(userpost)
        return Response(serializer.data)


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination


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
@permission_classes((IsAuthenticated,))
def api_update_postview(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    requser = request.user

    if post.user != requser:
        return Response({'Response':"you dont have correct permissions to edit "})

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
@permission_classes((IsAuthenticated,))
def api_delete_postview(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    requser = request.user
    if post.user != requser:
        return Response({'Response': "you dont have correct permissions to delete "})

    if request.method == "DELETE":
        operation = post.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_create_postview(request):
    account = request.user
    post = Post(user=account)
    if request.method == "POST":
        serializer = PostUpdateSerializer(post,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#    account = User.objects.get(pk=1)
