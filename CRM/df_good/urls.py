from  . import  views
from django.conf.urls import url

urlpatterns=[
    url(r'^prolist(\d+)/$',views.prolist),
    url(r'^sell/',views.sell),
    url(r'^prodetail(\d+)/$',views.prodetail),
    url(r'^dingzhi/',views.dingzhi),
    url('^help/',views.help),
    url('^xuanshang/',views.xuanshang),
    url(r'test/',views.test),
]