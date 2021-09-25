"""socialclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view


from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage.as_view(),name='home'),

    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include("django.contrib.auth.urls")),
    path('groups/',include('groups.urls',namespace='groups')),
    path('posts/',include('posts.urls',namespace='posts')),

    path('login_success/',views.login.as_view(),name='login_success'),
    path('thanks/',auth_view.LoginView.as_view(template_name='accounts/login.html'),name='thanks'),



    #REST FRAMEWORK URLS
    path('api/posts/',include('posts.api.urls',namespace='posts_api')),
    path('api/accounts/',include('accounts.api.urls',namespace='accounts_api')),
    path('api/groups/',include('groups.api.urls',namespace='groups_api')),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)