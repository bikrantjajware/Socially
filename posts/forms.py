from django import  forms
from .models import Post
from groups.models import Group


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','message','group']

    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user',None)
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['group'].queryset = Group.objects.filter(members=self.user.user_profile)