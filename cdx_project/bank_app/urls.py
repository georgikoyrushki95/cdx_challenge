from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('', 
	url(r'^$', views.index, name = "index"),
	url(r'^register/$', views.register, name = "register"),
	url(r'^sign-in/$', views.login, name = "register"),
	url(r'^error-message/$', views.error_message, name = "error_message")
	)