from django.shortcuts import render

from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from . import forms

# Create your views here.


class signup(CreateView):
    form_class = forms.Register
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'