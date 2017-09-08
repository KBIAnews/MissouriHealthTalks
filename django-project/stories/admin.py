# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Person, Story, Region, Issue, Location, Transcript, TranscriptLine

class TranscriptLineInline(admin.StackedInline):
    model = TranscriptLine

class TranscriptAdmin(admin.ModelAdmin):
    inlines = [
        TranscriptLineInline,
    ]

# Register your models here.

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date', 'region', 'location']
    search_fields = ['title', 'slug', 'description', 'transcript__text']
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    search_fields = ['name', 'title']
admin.site.register(Region)
admin.site.register(Issue)
admin.site.register(Location)
admin.site.register(Transcript, TranscriptAdmin)