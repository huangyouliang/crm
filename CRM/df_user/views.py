from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from  df_user.models import User
from django.template import RequestContext
#return render_to_response('template.html',context_instance=RequestContext(request))
# Create your views here.
#测试
# def test(request):
#     return render_to_response('index.html')
#注册
def reg(request):
    if request.method == 'POST':
        post = request.POST
        user = post.get('user')
        passwd = post.get('passwd')
        repasswd = post.get('repasswd')
        print('user:',user)
        if passwd != repasswd:
            return HttpResponse('两次密码输入不一致！')
        User.objects.create(
            user = user,
            passwd = passwd,
        )
        return render(request,'login.html',locals())
    return render(request,'reg.html',locals())
#登陆

def login(request):
    if request.method =='POST':
        post = request.POST
        user = post.get('user')
        passwd = post.get('passwd')
        user1 = User.objects.filter(user = user)
        request.session['id'] = user1[0].id
        request.session['username']=user
        print('user:',user,'passwd:',passwd)
        count = User.objects.filter(user=user,passwd=passwd).count()
        print('count:',count)
        if count > 0:
            context={
                'title':'主页',
            }
            return  render(request,'index.html',context)
        else:
            return HttpResponse('密码错误！')
    return render(request,'login.html',locals())

#退出
def logout(request):
    request.session.flush()
    context={
        'title':'登录系统',
    }
    # user_name = ''
    return render(request,'login.html',context)

