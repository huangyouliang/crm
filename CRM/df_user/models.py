from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField('用户名',max_length=20,)
    passwd = models.CharField('密码',max_length=20)
    city = models.CharField('所在城市', max_length=20,default='')
    sex = models.CharField('性别', max_length=5,default='')
    email = models.EmailField('邮箱', max_length=20,default='')
    ID_num = models.CharField('身份证', max_length=18,default='')
    intro = models.CharField('简介', max_length=200,default='')
    photo = models.ImageField('照片', default=True,upload_to='media')

    class Meta:
        verbose_name = '用户'
    def __str__(self):
        return self.name

