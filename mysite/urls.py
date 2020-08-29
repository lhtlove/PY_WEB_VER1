"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mysite.views import IndexView, UserCreateView, UserCreateDoneTV
from bookmark.views import BookmarkLV, BookmarkDV
from youtube.views import YoutubeLV, YoutubeDV
from blog.views import PostLV, PostDV

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),      #정규식, 얘들이 정규식을 읽고 필요한 파일을 불러옴.

    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register_done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^bookmark/$', BookmarkLV.as_view(), name='bookmark_index'),
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
    url(r'^youtube$', BookmarkLV.as_view(), name='youtube_index'),
    url(r'^youtube/(?P<pk>\d+)/$', YoutubeDV.as_view(), name='youtube_detail'),
    url(r'^blog/$', PostLV.as_view(), name='blog_index'),
    url(r'^blog/(?P<pk>\d+)/$', PostDV.as_view(), name='blog_detail'),    #<pk> = primary_key
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
