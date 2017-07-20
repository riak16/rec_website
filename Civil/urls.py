from django.conf.urls import url
from Civil import views

urlpatterns = [
	url(r'^$',views.CivilHome.as_view()),
	url(r'^form/$',views.CivilForm.as_view()),
]