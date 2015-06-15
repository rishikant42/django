from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import current_datetime, hours_ahead,my_view


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d+)/$', hours_ahead),
    url(r'^book/', include('books.urls')),
    url(r'^search/$', 'books.views.search'),
    url(r'contact/$', 'books.views.contact'),
    url(r'^mydata/(?P<month>\w{3})/(?P<day>\d\d)/$', my_view),
    (r'^mydata/birthday/$', my_view, {'month': 'jan', 'day':15}),
)
