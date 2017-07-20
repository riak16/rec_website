from django.conf.urls import url
from Clutch import views

urlpatterns = [
	url(r'^$',views.ClutchHome.as_view()),
	url(r'^form/$',views.ClutchForm.as_view()),
]