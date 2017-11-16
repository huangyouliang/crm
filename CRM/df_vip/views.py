from django.http import HttpResponse
from django.shortcuts import render,  redirect
from  df_vip.models import Vip_address
from  df_user.models import User


# Create your views here.

#客户中心
def vip_sell(request):
    if request.method == 'POST':
        user1 = User.objects.get(id=request.session['id'])
        post = request.POST
        #vip_user1.name = post.get('name')
        user1.city = post.get('city')
        user1.sex = post.get('sex')
        user1.email = post.get('email')
        user1.ID_num = post.get('ID_num')
        user1.intro = post.get('intro')
        user1.photo = request.FILES['img']
        user1.save()
    id = request.session['id']
    print('id:',id)
    vip = User.objects.get(id=id)
    print('name：', vip.user)
    context = {
        'title':'客户中心',
        'vip': vip,
    }
    return render(request, 'df_vip/vip.html',context)
#修改密码
def vip_pwd(request):
    if request.method == 'POST':
        user1 = User.objects.get(id=request.session['id'])
        post= request.POST
        passwd = post.get('passwd')
        repasswd = post.get('repasswd')
        if passwd == '' or repasswd =='':
            return HttpResponse('输入密码为空。')
        elif passwd != repasswd:
            return HttpResponse('两次输入密码不一致。')
        else :
            User.objects.filter(id=request.session['id']).update(passwd=passwd)
            #return HttpResponse('成功！。')
            return render(request, 'df_vip/vip_pwd.html')
    return render(request,'df_vip/vip_pwd.html')
#主页
def index(request):
    return render(request,'index.html')
#订单中心
def vip_order(request):
    return render(request,'df_vip/vip_order.html')
#搜藏
def vip_shoucang(request):
    return render(request,'df_vip/vip_shoucang.html')
#收货地址
def vip_address(request):
    address = Vip_address.objects.filter(user=request.session['username'])
    context={
        'title':'收货地址',
        'address':address,
    }
    return render(request,'df_vip/vip_address.html',context)
def vip_address_add(request):
    if request.method == 'POST':
        user_id = request.session['id']
        post =request.POST
        name = post.get('name')
        city = post.get('city')
        address = post.get('address')
        code = post.get('code')
        tel = post.get('tel')
        Vip_address.objects.create(
            user_id = user_id,
            name = name,
            city = city,
            address = address,
            code = code,
            tel = tel,
        )
        return redirect('/vip_address')
    return render(request,'df_vip/vip_address_add.html')
#修改收货地址
def vip_add_modify(request,id):
    id = int(id)
    address = Vip_address.objects.get(id=id)
    print('code1:',address.name)
    if request.method == 'POST':
        address.name= request.POST.get('name1')
        address.city = request.POST.get('city1')
        address.name= request.POST.get('name1')
        address.address = request.POST.get('address1')
        address.code = request.POST.get('code1')
        address.tel = request.POST.get('tel1')
        address.save()
        return redirect('/vip_address')
    context={
        'title':'修改地址',
        'address':address,
    }
    return render(request,'df_vip/vip_add_modify.html',context)

#删除地址
def addressdel(request,id):
    id = int(id)
    print('id',id)
    Vip_address.objects.get(id=id).delete()
    return redirect('/vip_address')
#上传照片
# def uploadImg(request):
#     if request.method == 'POST':
#         new_img = Vip_address(img=request.FILES.get('img'))
#         new_img.save()
#     return redirect('/vip/')