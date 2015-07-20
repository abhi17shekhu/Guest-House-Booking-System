from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
urlpatterns = [
	url(r'^$', login),
	url(r'^templates/registration/login.html',login),
	url(r'^templates/registration/logout.html',views.logout_view),
	url(r'^templates/blog/index.html', views.post_list),
    url(r'^templates/blog/booking.html', views.post_edit),
    url(r'^templates/blog/confirmed.html', views.granted),
    url(r'^templates/blog/details.html', views.detail),
    url(r'^templates/blog/status.html', views.status_check),
    url(r'^templates/blog/conf_arrived.html', views.arrived),
    url(r'^templates/blog/print_booking.html', views.print_booking),
    url(r'^blog/login/', views.post_list),
    
]