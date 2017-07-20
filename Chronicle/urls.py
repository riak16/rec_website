from django.conf.urls import url
from Chronicle import views

urlpatterns = [
	url(r'^$',views.ChronicleHome.as_view()),
	url(r'^form/$',views.ChronicleForm.as_view()),
]