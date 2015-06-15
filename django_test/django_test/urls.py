from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import home
from article.views import HelloTemplate

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url (r'^hello/$', 'article.views.hello'),
    url(r'^hello_template/$', 'article.views.hello_template'),
    url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
    url(r'^$',home),
    (r'^articles/', include('article.urls')),   
    url(r'^accounts/login/$', 'django_test.view.login'),
    url(r'^accounts/auth/$', 'django_test.view.auth_view'),
    url(r'^accounts/logout/$', 'django_test.view.logout'),
    url(r'^accounts/loggedin/$', 'django_test.view.loggedin'),
    url(r'^accounts/invalid/$', 'django_test.view.invalid_login'),
    url(r'^accounts/register/$', 'django_test.view.register_user'),
    url(r'^accounts/register_success/$', 'django_test.view.register_success'),

)
