from django.conf.urls import url
from Charge import views

urlpatterns = [
	url(r'^$',views.ChargeHome.as_view()),
	url(r'^form/$',views.ChargeForm.as_view()),
]