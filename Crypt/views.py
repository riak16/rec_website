from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.views.generic import TemplateView
from Crypt.forms import InfoForm
from .forms import CryptForms
from homepage.models import Info
import string

# Create your views here.
#class CryptHome(TemplateView):
	#def get(self,request,**kwargs):
		#return render(request,'Crypt/crypt_home.html',context=None)

class CryptHome(TemplateView):
	template_name='Crypt/crypt_home.html'

	def get(self,request):
		form = InfoForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=InfoForm(request.POST)
		if form.is_valid():
			#request.session.set_expiry(request.session.get_expiry_age())
			user=form.save()
			request.session['user'] = user.pk
			return HttpResponseRedirect('form')
		else:
			return render(request,self.template_name,{'form':form})



class CryptForm(TemplateView):
	template_name='Crypt/crypt_form.html'

	def get(self,request):
		form =  CryptForms()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		if request.session.get('user') is None:
			return HttpResponseRedirect('/credit/')
		form=CryptForms(request.POST)
		if form.is_valid():
			pk_info=request.session.get('user')
			user=get_object_or_404(Info,pk=pk_info)
			#form_new=InfoForm(name=info_post['name'], rollno=info_post['rollno'], email=info_post['email'], mobileno=info_post['mobileno'])
			#form_new.save()
			ans = form.save(commit=False)
			ans.creator=user
			ans.name=user.name
			ans.save()
			request.session['user']=pk_info
			return redirect('/success')
		else:
			return render(request,self.template_name,{'form':form})


	