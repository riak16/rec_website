from django.conf.urls import url ,include
from homepage import views

urlpatterns =[
	url(r'^$',views.home.as_view()),
	url(r'^home/',views.home1.as_view()),
	url(r'^crypt/',include('Crypt.urls')),
	url(r'^credit/',include('credit.urls')),
	url(r'^success/',views.success.as_view()),
]