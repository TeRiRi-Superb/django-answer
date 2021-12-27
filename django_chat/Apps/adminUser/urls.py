"""django_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from Apps.adminUser.views import *

urlpatterns = [
    path('admin/', AdminUser.as_view(), name='admin_user'),

    path('admin/resetpwd/<int:uid>', ResetPwdView.as_view(), name='reset_pwd'),
    path('admin/banuser/<int:uid>', BanUserView.as_view(), name='ban_user'),
    path('admin/deluser/<int:uid>', DelUserView.as_view(), name='del_user'),
    path('admin/delanswer/<int:aid>', DelAnswerView.as_view(), name='del_answer'),
    path('admin/editanswer/<int:aid>', EditAnswerView.as_view(), name='edit_answer'),
    path('admin/userexcel/', UserExcelView.as_view(), name='user_excel'),
]
