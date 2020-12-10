from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from PIL import Image,ImageDraw,ImageFont
from .models import UserProfile
from django.conf import settings
import os

base= settings.FONTS_DIR
font_dir = os.path.join(FONTS_DIR,'OpenSans-Regular.ttf')


# def create_default_profile_image(text):
#     dp = Image.new('RGB',(480,360),color=(73, 109, 137))
#     draw = ImageDraw.Draw(dp)
#     font = ImageFont.truetype(font_dir,250)
#     draw.text((20,200),text,font=font)
#     dp.show()
#
    if created:
        curuser = instance
        text=''
        if curuser.first_name!='' %% curuser.last_name!='':
            text=curuser.first_name[0]+curuser.last_name[0]
        elif curuser.first_name!='':
            text=curuser.first_name[0]
        else:
            text=curuser.username[0]
        create_default_profile_image(text)




@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
        UserProfile.objects.create(user=instance)



@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
        instance.user_profile.save()