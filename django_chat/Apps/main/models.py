from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='电话号码', null=False, default=1)

    def toDict(self):
        return {'id':self.id,'username':self.username,'password':self.password,'last_name':self.last_name,'first_name':self.first_name,'phone':self.phone,'date_joined':self.date_joined.strftime('%Y-%m-%d %H:%M:%S'),}

    class Meta:
        db_table = 'chat_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    @staticmethod
    def get_title_list():
        return ['id号', '密码', '最后登录时间', '是否为管理员', '用户名', '姓氏', '名字', '邮箱', '权限', '是否禁止登录', '创建时间', '电话号码']


class Answer(models.Model):
    problem = models.CharField(max_length=20)
    solutions = models.TextField(verbose_name='回答')
    img = models.ImageField(upload_to='img', null=True, blank=True)
    url = models.URLField(verbose_name='链接', null=True, blank=True)

    class Meta:
        db_table = 'chat_answer'
        verbose_name = '应答'
        verbose_name_plural = verbose_name


class CountUser(models.Model):
    user = models.ForeignKey('User', verbose_name='用户', on_delete=models.DO_NOTHING)
    cip = models.GenericIPAddressField(protocol='both')
    browser = models.CharField(max_length=20, verbose_name='浏览器')
    login_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_count'
        verbose_name = '统计'
        verbose_name_plural = verbose_name


class HighProblem(models.Model):
    problem = models.CharField(max_length=20)
    count = models.IntegerField(default=1)
    ask_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat_high'
        verbose_name = '高频短语'
        verbose_name_plural = verbose_name

    @staticmethod
    def get_title_list():
        return ['id号', '问题', '提问时间', '提问次数']