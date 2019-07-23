from django.db import models
# from django import forms

# Create your models here.

# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名',max_length=128)
#     password = forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput)

class User(models.Model):
    '''用户表'''

    gender=(
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']  # 优先显示最先创建的
        verbose_name = '用户'
        verbose_name_plural = '用户'


