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
admin.site.register(Person)
admin.site.register(Story)
admin.site.register(Region)
admin.site.register(Issue)
admin.site.register(Location)
admin.site.register(Transcript, TranscriptAdmin)