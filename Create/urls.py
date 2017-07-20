from django.conf.urls import url
from Create import views

urlpatterns = [
	url(r'^$',views.CreateHome.as_view()),
	url(r'^form/$',views.CreateForm.as_view()),
]