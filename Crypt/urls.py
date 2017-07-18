from django.conf.urls import url
from Crypt import views

urlpatterns = [
	url(r'^$',views.CryptHome.as_view()),
	url(r'^form/$',views.CryptForm.as_view()),
]