from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from  rest_framework.permissions import IsAuthenticated,AllowAny
# from ..models import UserProfile
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import AccountSerializer
from rest_framework.authtoken.models import Token
from django.http import Http404
from rest_framework.settings import api_settings


#
# class ProfileViewset(viewsets.ModelViewSet):
#     serializer_class = ProfileSerializer
#     queryset = UserProfile.objects.all()
#     lookup_field = 'user'



@api_view(['POST',])
@permission_classes((AllowAny,))
def registration_view(request):

    if request.method == "POST":
        serializer = AccountSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            print('account= ',account)
            data['response'] = "successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token']=token
            return Response(data,status=status.HTTP_200_OK)
        else:
            data=serializer.errors
            return Response(data)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_view(request):

    try:
        profile = User.objects.get(id=request.user.pk)
    except User.DoesNotExist:
        raise Http404

    if request.method == "GET":
        serializer = AccountSerializer(profile)
        return Response(serializer.data)


@api_view(['PUT','PATCH',])
@permission_classes((IsAuthenticated,))
def update_account_view(request):
    try:
        profile = User.objects.get(user=request.user.pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT" or request.method=="PATCH":
        serializer = AccountSerializer(profile, data=request.data, partial=True)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response']="details updated successfully"
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
