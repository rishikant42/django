from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	url(r'^new/$', new),
        url(r'^all/$', 'article.views.articles'),
        url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
        url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
	url(r'^create/$', 'article.views.create'),
        url(r'^search/$', 'article.views.search_titles'),

)
