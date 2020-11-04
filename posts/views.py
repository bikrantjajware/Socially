from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import  SelectRelatedMixin
from  django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib import messages
from . import  models

User = get_user_model()


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Post
    fields = ['message']
    template_name_suffix = '_update_form'



class ListPost(LoginRequiredMixin,SelectRelatedMixin,ListView):
    model = models.Post
    select_related=("user","group")

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['listgroups']=self.request.user.user_groups.all()
        return context


class CreatePost(LoginRequiredMixin,CreateView):
    fields = ('title','message','group')
    model = models.Post

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
        except IntegrityError:
            print("error occured")
        else:
            print("success here")
        return super().form_valid(form)


class PostDetail(SelectRelatedMixin,DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return  queryset.filter(user__username__iexact=self.kwargs.get('username'))


class UserPosts(ListView):

    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()


    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['post_user']= self.post_user
        return context


class DeletePost(LoginRequiredMixin,SelectRelatedMixin,DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,"Post Deleted")
        return super().delete(self,request,*args,**kwargs)