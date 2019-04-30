from django.conf.urls import include, url
from django.contrib import admin
from sess import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'teach_session.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sess/', v.Mysess),
    url(r'^student/', v.student),
]
