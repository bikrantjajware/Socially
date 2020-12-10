from  django.urls import path
from .views import registration_view,account_view,update_account_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter,SimpleRouter
from django.urls import include
from .views import ProfileViewset

router = SimpleRouter()
router.register('profile',ProfileViewset)


app_name="account"

urlpatterns = [
    path('register',registration_view,name='register'),
    path('token',obtain_auth_token,name='login'),
    path('login',account_view,name='view'),
    path('update',update_account_view,name='update'),
]

urlpatterns += router.urls