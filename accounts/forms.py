from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile,User
from django.forms import ModelForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Register(ModelForm):

    # def __init__(self,*args,**kwargs):
    #     super(Register, self).__init__(*args, **kwargs)
    #     for field in ["username", "password1", "password2", "email","avatar"]:
    #         self.fields[field].help_text = None



    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        # help_texts = {k: "" for k in fields}


"""
A ModelForm for creating a new user.

It has three fields: username (from the user model), password1, and password2.
It verifies that password1 and password2 match, validates the password using validate_password(),
and sets the user’s password using set_password().
"""
