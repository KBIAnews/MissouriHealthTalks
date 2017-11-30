# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Transcript (models.Model):
    TYPE_NORMAL = 0
    TYPE_SMART = 1
    TYPE_CHOICES = (
        (TYPE_NORMAL, 'Normal'),
        (TYPE_SMART, 'Smart'),
    )
    name = models.CharField("Transcript Name",
                            max_length=1024,
                            help_text="For your use. Not displayed to users.")
    type = models.IntegerField("Transcript Type",
                               default=TYPE_NORMAL,
                               choices=TYPE_CHOICES,
                               help_text="Smart transcripts include timecodes and follow along with audio.")
    text = models.TextField("Transcript Text",
                            blank=True,
                            help_text="Markdown version of your transcript. Optional for smart.")

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        ordering = ['name']

class TranscriptLine (models.Model):
    speaker = models.CharField("Speaker Display Name",
                               max_length=140)
    text = models.TextField("Text",
                            blank=False,
                            help_text="What the speaker says. Markdown compatible.")
    tc_min = models.IntegerField("Minutes",
                                 default=0)
    tc_sec = models.IntegerField("Seconds")
    transcript = models.ForeignKey(Transcript,
                                   related_name="lines",
                                   related_query_name="line")

    def __str__(self):
        return "%s - %i min %i sec" % (self.name, self.tc_min, self.tc_sec)

    class Meta:
        ordering = ['tc_min', 'tc_sec']

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
    photo = models.ImageField("Profile Photo",
                              blank=False,
                              help_text="Make sure these are square. Pay special attention to file size when"
                                        + " creating these, since they are displayed frequently.")

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
    title = models.CharField(max_length=1024,
                             help_text="If this title is a quote, make sure your quotation marks aren't curly - Django hates those.")
    recorded_date = models.DateField("Date Recorded")
    air_date = models.DateField("Date First Aired", null=True)
    description = models.TextField(help_text=("Appears at the top of stories and on index pages. "
                                   + "Supports markdown."))
    audio_file = models.FileField("Story MP3 Audio")
    photo = models.ImageField("Story Photo", blank=True)
    location = models.ForeignKey(Location,
                                 related_name="stories",
                                 related_query_name="story")
    region = models.ForeignKey(Region,
                               related_name="stories",
                               related_query_name="story")
    people = models.ManyToManyField(Person,
                                    related_name="stories",
                                    related_query_name="story")
    issues = models.ManyToManyField(Issue,
                                    related_name="stories",
                                    related_query_name="story")
    transcript = models.ForeignKey(Transcript,
                                   help_text=("If you do not add a transcript, one will not"
                                    + " be displayed."),
                                   blank=True,
                                   null=True,
                                   related_name='transcript')

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return "/stories/%s/" % self.slug

    class Meta:
        ordering = ['-air_date', 'slug']
        verbose_name_plural = "stories"