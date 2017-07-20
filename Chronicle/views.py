from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.views.generic import TemplateView
from Chronicle.forms import InfoForm
from .forms import ChronicleForms
from homepage.models import Info
from django.core.mail import send_mail
import string

# Create your views here.
#class CryptHome(TemplateView):
	#def get(self,request,**kwargs):
		#return render(request,'Crypt/crypt_home.html',context=None)

class ChronicleHome(TemplateView):
	template_name='Chronicle/chronicle_home.html'

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



class ChronicleForm(TemplateView):
	template_name='Chronicle/chronicle_form.html'

	def get(self,request):
		if request.session.get('user') is None:
			return HttpResponseRedirect('/chronicle/')
		form =  ChronicleForms()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		if request.session.get('user') is None:
			return HttpResponseRedirect('/chronicle/')
		form=ChronicleForms(request.POST)
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
			send_mail('ISTE NITK Recruitments 2017','Hello ' + user.name + '!\n\nThank You for filling up the recruitment form. We have received your submission. We look forward to meeting you in the interaction.\n\nIf you haven\'t applied then please report back to us.\n\nSee you soon! :)\n\nTeam ISTE-NITK','istenitkchapter@gmail.com',[user.email],fail_silently=False,)
			return redirect('/success')
		else:
			return render(request,self.template_name,{'form':form})


	