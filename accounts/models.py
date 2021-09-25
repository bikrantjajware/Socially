
from django.contrib.auth.models import User,PermissionsMixin
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from  django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image,ImageDraw,ImageFont
import os
from django.conf import settings

base= settings.BASE_DIR
media = settings.MEDIA_ROOT
font_dir = os.path.join(os.path.join(base,'fonts'),'OpenSans-Regular.ttf')




# class UserProfile(models.Model):
#     user = models.OneToOneField(User,default=None,related_name='user_profile',on_delete=models.CASCADE)
#     bio = models.TextField(max_length=200,blank=True,null=True,default='write your bio')
#     phone = PhoneNumberField(null=True, blank=True, unique=True,default='')
#     avatar = models.ImageField(null=True,upload_to='images/profile_pics/')
#
#
#     def __str__(self):
#         return '@{}'.format(self.user.username)





#using a decorator to bind signals to this function
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#bjajware@septy
#\
# def create_default_profile_image(text,name):
#     dp = Image.new('RGB',(360,360),color=(73, 109, 137))
#     draw = ImageDraw.Draw(dp)
#     font = ImageFont.truetype(font_dir,280)
#     draw.text((80,8),text,font=font)
#     dp.save(os.path.join(media,'images/profile_pics/{}.png'.format(name)))

# @receiver(post_save,sender=User)
# def create_profile(sender,instance,created,**kwargs):
#     if created:
#         curuser = instance
#         text =''
#         if curuser.first_name != '' and curuser.last_name != '':
#             text = curuser.first_name[0] + curuser.last_name[0]
#         elif curuser.first_name != '':
#             text = curuser.first_name[0]
#         else:
#             text = curuser.username[0].upper()
#         create_default_profile_image(text,curuser.username)
#         UserProfile.objects.create(user=instance,avatar=os.path.join(media,'images/profile_pics/{}.png'.format(curuser.username)),phone=None)