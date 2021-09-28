from .views import PostList,api_update_postview,api_create_postview,api_delete_postview,api_detail_view
from django.urls import path


app_name = 'posts'

urlpatterns = [
    path('all/',PostList.as_view(),name='postlist'),
    path('update/<slug:slug>/',api_update_postview,name='postupdate'),
    path('create/',api_create_postview,name='postcreate'),
    path('delete/<int:pk>/',api_delete_postview,name='postdelete'),
    path('detail/<slug:slug>/',api_detail_view,name='postdetail'),


]