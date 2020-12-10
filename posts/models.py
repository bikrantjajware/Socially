from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Group
from django.urls import reverse
from django.utils.text import slugify
import misaka
from  django.utils import  timezone
User = get_user_model()
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True,editable=False,default=slugify(title))
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',blank=True,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.message + ' ' + self.slug

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
       # unique_together = ['user','message',]


    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})


