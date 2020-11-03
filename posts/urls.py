
from django.urls import path
from . import  views

app_name='posts'

urlpatterns = [

    path('new/',views.CreatePost.as_view(),name='create'),
    path('by/<str:username>/<int:pk>/',views.PostDetail.as_view(),name='single'),
    path('all/',views.ListPost.as_view(),name='all'),
    path('by/<str:username>/',views.UserPosts.as_view(),name='by_user'),
    path('delete/<int:pk>',views.DeletePost.as_view(),name='delete'),
    path('update/<int:pk>/',views.PostUpdateView.as_view(),name='update'),


]