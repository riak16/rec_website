from django.conf.urls import url
from Credit import views

urlpatterns = [
	url(r'^$',views.CreditHome.as_view()),
	url(r'^form/$',views.CreditForm.as_view()),
]