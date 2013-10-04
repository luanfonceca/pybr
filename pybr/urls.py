from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybr.views.home', name='home'),
    # url(r'^$', 'pybr.views.home', name='home'),
    # url(r'^pybr/', include('pybr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('core.urls')),
)
