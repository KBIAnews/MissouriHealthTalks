# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bakery.feeds import BuildableFeed

from .models import Story

# Create your views here.

class StoriesRSSFeed(BuildableFeed):
    link='https://www.missourihealthtalks.org/rss.xml'
    build_path = 'rss.xml'
    item_author_name = 'KBIA and Missouri Health Talks'

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return 'https://www.missourihealthtalks.org{}'.format(item.get_absolute_url())

    def item_guid(self, item):
        return 'https://www.missourihealthtalks.org{}'.format(item.get_absolute_url())

    def item_guid_is_permalink(self, obj):
        return True

    def item_description(self, item):
        return item.description

    def items(self, obj):
        return Story.objects.order_by('-air_date')
