from xml.dom.minidom import TypeInfo

from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Pro_body(models.Model):
    pname = models.CharField('品牌', max_length=20)
    pversion = models.CharField('型号',max_length=20)
    pcolor = models.CharField('颜色',max_length=20)
    pmarket_time = models.DateTimeField('上市时间')
    input_mode = models.CharField('输入方式',max_length=20)
    smart_phone = models.BooleanField('智能机',default=True)
    call_mode_3G = models.BooleanField('3G视频通话',default=True)
    systerm = models.CharField('操作系统',max_length=20)
    CPU_mode = models.CharField('CPU型号',max_length=20)
    CPU_frequency = models.CharField('CPU频率',max_length=20)
    CPU_kerenl = models.IntegerField('CPU核数')
    operator = models.CharField('运营商',max_length=20)
    pphoto = models.ImageField('照片',upload_to='goods',default='')
    pprice = models.CharField('价格',max_length=20,default='')
    pcomment = models.CharField('评论',max_length=100,default='')


    # gadv = models.BooleanField('广告',default=False)
    def __str__(self):
        return str(self.pversion)
#模型名称
    class Meta:
        verbose_name = '产品主体'
        verbose_name_plural = verbose_name

        def __unicode__(self):
            return self.pname.encode('utf-8')