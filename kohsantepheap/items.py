# -*- coding: utf-8 -*-


import scrapy


class KohsantepheapItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    htmlcontent = scrapy.Field()
    imageUrl = scrapy.Field()
    categoryId = scrapy.Field()
