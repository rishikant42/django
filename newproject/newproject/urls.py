from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
from article.views import *

#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^temp/$', temp),
    url(r'^temp2/$', temp2),
    url(r'^temp3/$', temp3),
    url (r'^temp4/$', temp4),
    url(r'^test/$', 'article.views.test'),
    url(r'^article/', include('article.urls')),
)
