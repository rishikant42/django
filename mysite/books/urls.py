from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	url(r'^new/$', new),
#	url(r'^image/$', my_image),
	url(r'^csv/$',unruly_passengers_csv),
	url(r'^pdf/$',hello_pdf),
        url(r'^newpdf/$', new_pdf),

)

