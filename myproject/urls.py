
from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

admin.autodiscover()

urlpatterns = patterns('',
        (r'^myapp/', include('myapp.urls')),
        (r'^$', 'myapp.views.index'),
        (r'^admin/', include(admin.site.urls)),

)


