"""
URL configuration for bl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from comment.views import comment
from comment.views import post
from login.views import log
from login.views import register
from login.views import form
from login.views import redirect_f
from login.views import change_user
from login.views import userprofile
from login.views import register_redirect
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from login.views import activate
from login.views import home_P

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post',comment),
    path('postf',post),
    path('online',log, name='login'),
    path('register__F',register, name='register'),
    path('loginformf',form),
    path('Redirect_Form',redirect_f),
    path('change_u',change_user, name='change_u'),
    path('userp',userprofile),
    path('Register_Mail',register_redirect),
    
    # password Reset --------------------------------
    path('reset/password/',PasswordResetView.as_view(template_name='reset_pass.html'),name='password_reset'),
    path('reset/password/done/',PasswordResetDoneView.as_view(template_name='reset_pass_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='pass_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done',PasswordResetView.as_view(template_name='pass_reset_complete.html'),name='password_reset_complete'),
    path('activate/<uidb64>/<token>/',activate,name='activate'),
    path('home_page',home_P, name='home'),



    
]
