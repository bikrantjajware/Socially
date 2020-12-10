
from .views import api_create_groupview,api_detail_group,api_join_group,api_leave_group,ApiPostListView
from django.urls import path

app_name= 'groups'

urlpatterns = [
    path('all/',ApiPostListView.as_view(),name='list'),
    path('new/',api_create_groupview,name='create'),
    path('detail/<slug:slug>/',api_detail_group,name='detail'),
    path('join/<slug:slug>/',api_join_group,name='join'),
    path('leave/<slug:slug>/',api_leave_group,name='leave'),

]