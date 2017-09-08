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
    filter_horizontal = ['people', 'issues']
    inline_type = 'stacked'
    inline_reverse = ['transcript']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    search_fields = ['name', 'title']
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
                ('first_name', 'second_name'),
                'title',
                'description',
                'photo'
            )
        }),
    )
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'center_lat', 'center_long']
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
                ('center_lat', 'center_long'),
                'map_zoom',
                'description'
            )
        }),
        ('Media', {
            'fields': (
                'image',
                'video_embed_url'
            )
        }),
    )
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'lat', 'long']
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
                ('lat', 'long'),
                'description',
            )
        }),
    )
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
                'description'
            )
        }),
    )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Transcript, TranscriptAdmin)