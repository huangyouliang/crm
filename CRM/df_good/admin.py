from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import   Pro_body

admin.site.register(Pro_body)

class Pro_bodyAdmin(admin.ModelAdmin):
    list_display = ('pname','pversion','pcolor','pmarket_time','input_mode')


    # smart_phone = models.BooleanField('智能机', default=True)
    # call_mode_3G = models.BooleanField('3G视频通话', default=True)
    # systerm = models.CharField('操作系统', max_length=20)
    # CPU_mode = models.CharField('CPU型号', max_length=20)
    # CPU_frequency = models.CharField('CPU频率', max_length=20)
    # CPU_kerenl = models.IntegerField('CPU核数')
    # operator = models.CharField('运营商', max_length=20)