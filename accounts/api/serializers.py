from rest_framework import serializers
from ..models import User

from phonenumber_field.serializerfields import PhoneNumberField


class AccountSerializer(serializers.ModelSerializer):
    password2= serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['pk','username','email','password','password2']
        extra_kwargs = {
            'password' :{'write_only':True }
        }

    def save(self):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"password":"password must match"})
        account.set_password(password)
        account.save()
        return account

#
# class ProfileSerializer(serializers.ModelSerializer):
#     user = AccountSerializer()
#     class Meta:
#         model = UserProfile
#         fields = ['user','bio','phone','avatar']