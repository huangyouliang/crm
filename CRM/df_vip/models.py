from django.db import models

# Create your models here.d
class Vip_address(models.Model):
     user = models.ForeignKey('df_user.User')
     name = models.CharField('收货人',max_length=12)
     city = models.CharField('地区',max_length=20)
     address = models.CharField('街道地址',max_length=100)
     code = models.EmailField('邮编',max_length=6)
     tel = models.CharField('电话',max_length=18)
