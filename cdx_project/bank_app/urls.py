from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('', 
	url(r'^$', views.index, name = "index"),
	url(r'^register/$', views.register, name = "register"),
	url(r'^login/$', views.user_login, name = "register"),
	url(r'^logout$', views.user_logout, name = "logout"),
	url(r'^emergency-message/$', views.emergency_message, name = "error_message"),
	)