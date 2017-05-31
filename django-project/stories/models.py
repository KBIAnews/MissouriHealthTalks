# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Location (models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=512)
    lat = models.FloatField("Latitude")
    long = models.FloatField("Longitude")
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ['slug']

class Region (models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=512)
    center_lat = models.FloatField("Map Center Latitude")
    center_long = models.FloatField("Map Center Longitude")
    map_zoom = models.IntegerField(default=11)
    image = models.ImageField(blank=True)
    video_embed_url = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return "/regions/%s/" % self.slug

    class Meta:
        ordering = ['slug']

class Person(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=1024)
    first_name = models.CharField(max_length=1024)
    second_name = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField("Square Profile Photo", blank=False)

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return "/people/%s/" % self.slug

    class Meta:
        ordering = ['slug']
        verbose_name_plural = "people"

class Issue(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return "/issues/%s/" % self.slug

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ['slug']

class Story (models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=1024)
    date = models.DateField()
    description = models.TextField()
    audio_file = models.FileField("Story MP3 Audio")
    photo = models.ImageField("Story Photo", blank=True)
    location = models.ForeignKey(Location,
                                 related_name="stories",
                                 related_query_name="story",)
    region = models.ForeignKey(Region,
                               related_name="stories",
                               related_query_name="story",)
    people = models.ManyToManyField(Person,
                                    related_name="stories",
                                    related_query_name="story")
    issues = models.ManyToManyField(Issue,
                                    related_name="stories",
                                    related_query_name="story",)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return "/stories/%s/" % self.slug

    class Meta:
        ordering = ['date', 'slug']
        verbose_name_plural = "stories"
