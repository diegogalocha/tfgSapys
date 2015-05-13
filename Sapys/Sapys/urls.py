from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^appointments/$','principal.views.appointmentList', name="appointmentList"),
    url(r'^appointment/new/$','principal.views.new_appointment', name="new_appointment"),
    url(r'^login/$','Sapys.views.login_page', name="login"),
    url(r'^$','Sapys.views.homepage', name="homepage"),
    url(r'^logout/$','Sapys.views.logout_view', name="logout"),
    )
