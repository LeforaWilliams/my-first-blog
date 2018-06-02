from django.conf.urls import url
from . import views

#here we are telling django? how to name new urls for posts, we use the regex
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]