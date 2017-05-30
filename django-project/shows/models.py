# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Show (models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="shows/images")
    overall_order = models.IntegerField("Overall Ordering - Use instead of per item.", default=0)
    feed_url = models.URLField(
        "Podcast (RSS) Feed URL",
        max_length=1024,
        null=True,
        blank=True)
    itunes_url = models.URLField(
        "Apple Podcasts/iTunes Page URL",
        max_length=1024,
        null=True,
        blank=True)
    stitcher_url = models.URLField(
        "Stitcher Page URL",
        max_length=1024,
        null=True,
        blank=True)
    google_url = models.URLField(
        "Google Play Podcasts Page URL",
        max_length=1024,
        null=True,
        blank=True)
    overcast_url = models.URLField(
        "Overcast Page URL",
        max_length=1024,
        null=True,
        blank=True)
    pocket_casts_url = models.URLField(
        "Pocket Casts Page URL",
        max_length=1024,
        null=True,
        blank=True)
    npr_one_url = models.URLField(
        "NPR One URL",
        max_length=1024,
        null=True,
        blank=True)

    class Meta:
        ordering = ['overall_order','slug']

    def get_absolute_url(self):
        return "/shows/%s/" % self.slug

    def __str__(self):
        return "%s" % self.name

class Episode(models.Model):
    name = models.CharField(max_length=512)
    date = models.DateField()
    audio_url = models.URLField("MP3 File URL", max_length=1024)
    show = models.ForeignKey(Show, related_name='episodes')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "%s" % self.name

class Category(models.Model):
    slug = models.SlugField("Category 'Slug'", unique=True)
    name = models.CharField("Category Display Name", max_length=1024)
    order = models.IntegerField("Category Display Position on Home Screen", unique=True)
    display_on_home = models.BooleanField("Display this category on Home Screen", default=True)
    shows = models.ManyToManyField(
        Show,
        through='ShowCategory',
        through_fields=('category', 'show')
    )

    class Meta:
        ordering = ['order']
        verbose_name_plural = "categories"

    def __str__(self):
        return "%s" % self.name

class ShowCategory(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="membership")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="membership")
    order = models.IntegerField("Nonfunctional Order", default=0)

    class Meta:
        ordering = ['order']
