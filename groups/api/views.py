from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from ..models import Group,GroupMember
from django.db import  IntegrityError
from .serializers import GroupSerializer
from rest_framework.generics import ListAPIView
from django.contrib.auth import models
from rest_framework.filters import SearchFilter,OrderingFilter


class ApiPostListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # pagination_class = PageNumberPagination
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ('title', 'message', 'user__username')



@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_create_groupview(request):
    account = request.user
    grp = Group()
    #grp.members.add(account)
    if request.method == "POST":
        serializer = GroupSerializer(grp,data=request.data)


        if serializer.is_valid():
            serializer.save()
            grp.members.add(account)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_detail_group(request,slug):
    try:
        grp = Group.objects.get(slug=slug)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GroupSerializer(grp)
        return Response(serializer.data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_join_group(request,slug):
    try:
        grp = Group.objects.get(slug=slug)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        data={}
        try:
            GroupMember.objects.create(user=request.user, group=grp)
        except IntegrityError:
            data['Response']="User already joined group"
        else:
            data['Response'] = "User joined the group"
        return Response(data)



@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_leave_group(request,slug):
    try:
        grp = Group.objects.get(slug=slug)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        data={}
        try:
            membership = GroupMember.objects.filter(user=request.user,group__slug=slug).get()
        except GroupMember.DoesNotExist:
            data['Response']="User does not exist in group"
        else:
            membership.delete()
            data['Response'] = "User left the group"
        return Response(data)