"""podcasts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from stories.views import StoryDetailView, IssueDetailView, RegionDetailView, HomePageView, PersonDetailView
from django.conf import settings


urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', HomePageView.as_view()),
                  url(r'stories/(?P<slug>[\w-]+)/$', StoryDetailView.as_view(), name='story'),
                  url(r'issues/(?P<slug>[\w-]+)/$', IssueDetailView.as_view(), name='issue'),
                  url(r'regions/(?P<slug>[\w-]+)/$', RegionDetailView.as_view(), name='region'),
                  url(r'people/(?P<slug>[\w-]+)/$', PersonDetailView.as_view(), name='person'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Missouri Health Talks Admin'
admin.site.site_title = 'Missouri Health Talks Admin'