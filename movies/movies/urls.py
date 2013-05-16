from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from movies import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movies.views.home', name='home'),
    # url(r'^movies/', include('movies.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photos/', 'catalogue.views.photo_list', name='photo_list'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
