from django.conf.urls import url, include, url
from .import views
urlpatterns = [
	url(r'^$', views.post_list),
]