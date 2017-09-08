# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_reverse_admin import ReverseModelAdmin

from .models import Person, Story, Region, Issue, Location, Transcript, TranscriptLine

class TranscriptInline(admin.StackedInline):
    model = Transcript

class TranscriptLineInline(admin.StackedInline):
    model = TranscriptLine

class TranscriptAdmin(admin.ModelAdmin):
    inlines = [
        TranscriptLineInline,
    ]

# Register your models here.

@admin.register(Story)
class StoryAdmin(ReverseModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date', 'region', 'location']
    search_fields = ['title', 'slug', 'description', 'transcript__text']
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'slug'),
                'date',
                ('region', 'location'),
                'description',
            ),
        }),
        ('Tagging', {
            'fields': (
                'people',
                'issues'
            )
        }),
        ('Media',
         {
             'fields': (
                 'audio_file',
                 'photo',
             )
         })
    )
    inline_type = 'stacked'
    inline_reverse = ['transcript']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    search_fields = ['name', 'title']

admin.site.register(Region)
admin.site.register(Issue)
admin.site.register(Location)
admin.site.register(Transcript, TranscriptAdmin)