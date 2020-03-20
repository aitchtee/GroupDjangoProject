"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', 'posts.views.post_home'),
    url(r'^post_detail/(?P<id>\d+)/$', 'posts.views.post_detail'),
    url(r'^post_update/(?P<id>\d+)/$', 'posts.views.post_update'),
    url(r'^post_delete/$', 'posts.views.post_delete'),
    url(r'^post_create/$', 'posts.views.post_create'),
    url(r'^$', 'posts.views.post_list'),
]
