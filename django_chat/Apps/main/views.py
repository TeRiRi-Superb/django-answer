from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View
from .models import User, CountUser
import time
import re


# Create your views here.
class IndexView(View):
    def get(self, request):
        if 'username' in request.session:
            user = request.session.get('username')
            print(request.META['HTTP_USER_AGENT'])
            return JsonResponse({'res': 0, 'message': '成功', 'user': user})
        return JsonResponse({'res': 1, 'message': '未登录'})


class RegisterUser(View):
    def get(self, request):
        return JsonResponse({'res': 0, 'message': '注册页面'})

    def post(self, request):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        print([user, pwd, phone, mail])
        if not all([user, pwd, phone, mail]):
            return JsonResponse({'res': 1, 'message': '数据不全'})

        e = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
        if not e.search(mail):
            return JsonResponse({'res': 2, 'message': '邮箱错误'})

        p = re.compile(r'1[35678]\d{9}')
        if not p.search(phone):
            return JsonResponse({'res': 3, 'message': '无效手机号'})

        pw = re.compile(r'^[a-zA-Z0-9]{6,20}$')
        if not pw.search(pwd):
            return JsonResponse({'res': 4, 'message': '密码格式错误'})

        try:
            User.objects.create_user(username=user, password=pwd, email=mail, phone=phone)
            return JsonResponse({'res': 0, 'message': '创建成功'})
        except Exception:
            return JsonResponse({'res': 5, 'message': '创建失败'})


class LoginUser(View):
    def get(self, request):
        if 'username' in request.session:
            return redirect(reverse('main:index'))

        return JsonResponse({'res': 0, 'message': '跳转到首页'})

    def post(self, request):
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')

        user = authenticate(username=username, password=pwd)

        if user is not None:
            if user.is_active:
                request.session['username'] = user.toDict()
                # print(request.META['HTTP_USER_AGENT'])
                count_user = CountUser.objects
                cip = request.META['REMOTE_ADDR']
                user_agent = request.META['HTTP_USER_AGENT']
                print(request.META)

                if 'Safari' in user_agent:
                    browser = '谷歌'
                elif 'Firefox' in user_agent:
                    browser = '火狐'
                elif 'Opera' in user_agent:
                    browser = 'Opera'
                else:
                    browser = 'IE'

                count_user.create(user=user, cip=cip, browser=browser,  login_time=time.time())

                return JsonResponse({'res': 0, 'message': '登录成功'})
            else:
                return JsonResponse({'res': 2, 'message': '账号被禁止登录'})
        else:
            return JsonResponse({'res': 1, 'message': '密码格式错误'})


class LogoutView(View):
    def get(self, request):
        del request.session['username']
        return JsonResponse({'res': 0, 'message': '已注销登录'})