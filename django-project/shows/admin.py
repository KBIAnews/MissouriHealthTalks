# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Show, Episode, Category, ShowCategory

# Create custom admins with inlines for categories
class ShowCategoryInline(admin.TabularInline):
    model = Category.shows.through

class EpisodeInline(admin.TabularInline):
    model = Episode

class ShowAdmin(admin.ModelAdmin):
    inlines = [
        ShowCategoryInline,
        EpisodeInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ShowCategoryInline,
    ]
    exclude = ('shows',)

# Register your models here.

admin.site.register(Show, ShowAdmin)
admin.site.register(Episode)
admin.site.register(Category, CategoryAdmin)