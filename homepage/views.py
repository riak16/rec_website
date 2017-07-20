from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.views.generic import TemplateView
from .models import Info

# Create your views here.
class home(TemplateView):
	def get(self,request,**kwargs):
		return render(request,'homepage/home.html',context=None)
class home1(TemplateView):
	def get(self,request,**kwargs):
		return redirect('/')

class success(TemplateView):
	def get(self,request,**kwargs):
		if request.session.get('user') is None:
			return HttpResponseRedirect('/')
		pk_info=request.session.get('user')
		user=get_object_or_404(Info,pk=pk_info)
		request.session['user']=pk_info
		return render(request,'homepage/success.html',context=None)

class no(TemplateView):
	def get(self,request,**kwargs):
		pk_info=request.session.get('user')
		del request.session['user']
		return redirect('/')