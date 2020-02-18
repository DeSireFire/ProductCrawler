# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class GoodscrawlerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class KapitalItem(Item):
    brand = Field()
    title = Field()
    art_no = Field()
    item_url = Field()
    images = Field()
    image_base_url = Field()
