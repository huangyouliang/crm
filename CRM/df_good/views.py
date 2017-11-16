from django.shortcuts import render
from  .models import Pro_body
# Create your views here.
def prolist(request,sort):
    #good_list = Pro_body.objects.all()
    print('sort:',sort)
    if sort=='1':
        good_list = Pro_body.objects.all()
    elif sort == '4':
        good_list = Pro_body.objects.order_by("pprice")

    context={
        'title':'手机商城',
        'good_list':good_list
    }
    return render(request,'df_goods/prolist1.html',context)
def sell(request):
    return render(request,'df_goods/sell.html')
def prodetail(request,id):
    good = Pro_body.objects.get(id=id)
    context={
        'title':'手机详情',
        'good':good,
    }
    return render(request,'df_goods/prodetail.html',context)
#定制
def dingzhi(request):
    return render(request,'df_goods/dingzhi.html')
# 帮助
def help(request):
    return render(request,'help.html')
#悬赏
def xuanshang(request):
    return render(request,'df_goods/xuanshang.html')
def test(request):
    return render(request,'df_goods/prodetail.html')