from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'danaTeacher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'liudana/', views.do_app) ,

]