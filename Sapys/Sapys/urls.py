from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','principal.views.index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^appointments/','principal.views.appointmentList'),
    url(r'^appointment/new/','principal.views.new_appointment'),
)
