from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('new/',views.CreateGroup.as_view(),name='create'),
    path('posts/in/<slug:slug>/',views.DetailGroup.as_view(),name='single'),
    path('all/',views.ListGroup.as_view(),name='all'),
    path('join/<slug:slug>/',views.JoinGroup.as_view(),name='join'),
    path('leave/<slug:slug>/',views.LeaveGroup.as_view(),name='leave'),
]