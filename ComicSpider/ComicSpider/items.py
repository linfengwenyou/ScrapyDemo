# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicspiderItem(scrapy.Item):
    name = scrapy.Field()
    image_url = scrapy.Field()
    link_url = scrapy.Field()


    pass

import types
from inspect import isgeneratorfunction

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield  b
        a,b = b,a+b
        n = n + 1



value = isinstance(fab(5), types.GeneratorType)
print(value)

for n in fab(11):
    print(n)