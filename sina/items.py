# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    docid = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    timestamp = scrapy.Field()
    source = scrapy.Field()
    key_words = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()
    links = scrapy.Field()
