from django.conf.urls import url ,include
from homepage import views

urlpatterns =[
	url(r'^$',views.home.as_view()),
	url(r'^home/',views.home1.as_view()),
	url(r'^crypt/',include('Crypt.urls')),
	url(r'^credit/',include('Credit.urls')),
	url(r'^civil/',include('Civil.urls')),
	url(r'^create/',include('Create.urls')),
	url(r'^clutch/',include('Clutch.urls')),
	url(r'^chronicle/',include('Chronicle.urls')),
	url(r'^charge/',include('Charge.urls')),
	url(r'^success/',views.success.as_view()),
	url(r'^no/',views.no.as_view()),
]