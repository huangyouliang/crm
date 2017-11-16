
from . import views
from django.conf.urls import url

urlpatterns = [
    # url(r'^test',views.test),
    url(r'^reg/',views.reg),
    url(r'^login',views.login),
    url(r'^logout',views.logout),
]