from django.conf.urls import url
from . import views
from .forms import LoginForm
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^list/(?P<pagenum>[0-9]+)/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_view, name='post_view'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^join/$', views.join, name='join'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'diary/login.html',},
          name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),    
    #url(r'^login/$', views.login),

]