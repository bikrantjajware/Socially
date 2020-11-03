from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class Register(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super(Register, self).__init__(*args, **kwargs)
        for field in ["username", "password1", "password2", "email"]:
            self.fields[field].help_text = None



    class Meta:
        fields = ('username', 'password1', 'password2', 'email')
        model = get_user_model()
        # help_texts = {k: "" for k in fields}


"""
A ModelForm for creating a new user.

It has three fields: username (from the user model), password1, and password2.
It verifies that password1 and password2 match, validates the password using validate_password(),
and sets the user’s password using set_password().
"""
