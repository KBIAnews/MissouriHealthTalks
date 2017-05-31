# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bakery.views import BuildableListView, BuildableDetailView

from .models import Story, Location, Issue, Person, Region

# Create your views here.

class HomePageView(BuildableListView):
    queryset = Story.objects.all()
    model = Story # This also means the template for this will be story_list.html

class StoryDetailView(BuildableDetailView):
    model = Story
    template_name = 'stories/story_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Story.objects.get(slug=self.kwargs['slug'])
        return super(StoryDetailView, self).get_objects()
