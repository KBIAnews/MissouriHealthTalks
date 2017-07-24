# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bakery.views import BuildableListView, BuildableDetailView

from .models import Story, Location, Issue, Person, Region

# Create your views here.

class HomePageView(BuildableListView):
    queryset = Story.objects.all()
    model = Story # This also means the template for this will be story_list.html

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context

class StoryDetailView(BuildableDetailView):
    model = Story
    template_name = 'stories/story_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Story.objects.get(slug=self.kwargs['slug'])
        return super(StoryDetailView, self).get_objects()

class IssueDetailView(BuildableDetailView):
    model = Issue
    template_name = 'stories/issue_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Issue.objects.get(slug=self.kwargs['slug'])
        return super(IssueDetailView, self).get_objects()

class RegionDetailView(BuildableDetailView):
    model = Region
    template_name = 'stories/region_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Region.objects.get(slug=self.kwargs['slug'])
        return super(RegionDetailView, self).get_objects()

class PersonDetailView(BuildableDetailView):
    model = Person
    template_name = 'stories/person_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Person.objects.get(slug=self.kwargs['slug'])
        return super(PersonDetailView, self).get_objects()
