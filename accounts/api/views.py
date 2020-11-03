from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RegisterSerializer


@api_view(['POST',])
def registration_view(request):

    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data=serializer.errors
        return Response(data)