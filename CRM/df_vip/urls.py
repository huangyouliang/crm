
from . import views
from django.conf.urls import url

urlpatterns = [
   # url(r'^test',views.test),
    url(r'^vip/',views.vip_sell),
    url(r'^vip_pwd',views.vip_pwd),
    url(r'^index/',views.index),
    url(r'^vip_order/',views.vip_order),
    url(r'^vip_shoucang',views.vip_shoucang),
    url('vip_address',views.vip_address),
    url('vip_add',views.vip_address_add),
    url(r'^vip_modify/(\d+)/$',views.vip_add_modify),
    url(r'^addressdel/(\d+)/$',views.addressdel),
    #url(r'^upload',views.uploadImg),

]