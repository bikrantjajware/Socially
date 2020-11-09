from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
import misaka
# Create your models here.

User = get_user_model()

from django import  template
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True) #allow_unicode=True , allows slug to accept unicode letters in addition to from ASCII
    description = models.TextField(default='',blank='',)
    description_html = models.TextField(editable=False,blank=True,default='')
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)

        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
         ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together =('group','user')



'''

The related_name attribute specifies the name of the reverse relation from the User model back to your model.

If you don't specify a related_name, Django automatically creates one using the name of your model with the suffix _set, for instance User.map_set.all().

If you do specify, e.g. related_name=maps on the User model, User.map_set will still work, but the User.maps. syntax is obviously a bit cleaner and less clunky;
so for example, if you had a user object current_user, you could use current_user.maps.all() to get all instances of your Map model that have a relation to current_user.

'''


'''
DIFFERENCE B/W TextField and CharField

It's a difference between RDBMS's varchar (or similar) — those are usually specified with a maximum length,
 and might be more efficient in terms of performance or storage — and text (or similar) types — those are usually limited
  only by hardcoded implementation limits (not a DB schema).
  
  A good rule of thumb is that you use CharField when you need to limit the maximum length, TextField otherwise.
'''