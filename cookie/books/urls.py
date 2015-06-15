from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	url(r'^new/$', new),
#	url(r'^image/$', my_image),
	url(r'^csv/$',unruly_passengers_csv),
	url(r'^pdf/$',hello_pdf),
        url(r'^newpdf/$', new_pdf),
	url(r'^color/$',show_color),
	url(r'^set_color/$', set_color),
 	url(r'^foo/(\d{1,2})/$', my_view),
)

