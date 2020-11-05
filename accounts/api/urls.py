from  django.urls import path
from .views import registration_view,account_view,update_account_view
from rest_framework.authtoken.views import obtain_auth_token

app_name="account"

urlpatterns = [
    path('register',registration_view,name='register'),
    path('login',obtain_auth_token,name='login'),
    path('view',account_view,name='view'),
    path('update',update_account_view,name='update'),
]