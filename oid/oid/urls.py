from django.conf.urls import patterns, include, url

from django.contrib import admin
import index.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index.views.index),


    url(r'^/login-form/', 'index.views.steam_success'),
    url(r'^/logged-in/', 'index.views.steam_success'),
    url(r'^/login-error/', 'index.views.steam_success'),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
