from django.db import models
from django.contrib.auth import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(models.User,models.PermissionsMixin):

    def __str__(self):
        return '@{}'.format(User.username)

usermodel = get_user_model()


@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print("methods called")
    if created:
        Token.objects.create(user=instance)