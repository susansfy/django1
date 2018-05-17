#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_action(request):
	if request.method=='POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		#if username == 'admin' and password == 'admin123':
			#return HttpResponse('login success!')
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			request.session['user']=username  #将session信息记录到浏览器
			response = HttpResponseRedirect('/home/')
			
			return response
		else:
			return render(request,'index.html',{'error':'username or password incorrect'})

	else:
		return render(request,'index.html')

@login_required
def  home_page(request):
	username = request.session.get('user','')  #读取浏览器session
	return render(request,'home.html')