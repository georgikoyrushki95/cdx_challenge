from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('', 
	url(r'^$', views.index, name = "index"),
	url(r'^register/$', views.register, name = "register"),
	url(r'^sign-in/$', views.login, name = "register"),

	)