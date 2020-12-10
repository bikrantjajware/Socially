from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,CreateView,DetailView,RedirectView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.contrib import messages
from django.urls import  reverse_lazy
from . import models


class ListGroup(ListView):
    model = models.Group


# create view requires a <name>_form.html , ex:- group_form.html file
class CreateGroup(LoginRequiredMixin,CreateView):
    fields = ('name', 'description')
    model = models.Group

    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.save()
        instance.members.add(self.request.user)
        return super().form_valid(form)

    # def get_success_url(self):
    #     group = get_object_or_404(models.Group, slug=self.kwargs.get('slug'))
    #     try:
    #         models.GroupMember.objects.create(user=self.request.user, group=group)
    #     except IntegrityError:
    #         messages.warning(self.request, "User already joined")
    #     else:
    #         messages.success(self.request, "User joined the group")
    #
    #     return reverse('groups:single',kwargs={'slug':self.slug})

    # def get(self, request, *args, **kwargs):

    #     return super().get(self,*args,**kwargs)
#slug_field¶
#The name of the field on the model that contains the slug. By default, slug_field is 'slug'
# slug_url_kwarg¶
# The name of the URLConf keyword argument that contains the slug. By default, slug_url_kwarg is 'slug'.


class DetailGroup(DetailView):
    model = models.Group
    slug_url_kwarg = 'slug'
    slug_field = 'slug'


    # def get(self, request, *args, **kwargs):
    #     group = get_object_or_404(models.Group,slug=self.kwargs.get('slug'))
    #     try:
    #         models.GroupMember.objects.create(user=self.request.user,group=group)
    #     except IntegrityError:
    #         messages.warning(self.request,"User already joined")
    #     else:
    #         messages.success(self.request,"User joined the group")
    #     return super().get(self,*args,**kwargs)




class JoinGroup(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        group = get_object_or_404(models.Group,slug=self.kwargs.get('slug'))

        try:
             models.GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'user already registered')
        else:
            messages.success(self.request,'user joined the group')


        return super().get(self,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = models.GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'user no longer in group')
        else:
            membership.delete()
            messages.success(self.request,'user left the group successfully')


        return super().get(self,*args,**kwargs)


