# -*- coding: utf-8 -*-
import scrapy
from ComicSpider.items import ComicspiderItem
import pprint


class ComicSpider(scrapy.Spider):
    name = 'comic1'
    allowed_domains = ['kuman.com']
    start_urls = ['http://www.kuman.com']

    def parse(self, response):
        # fin = open('comic.html','wb')
        # fin.write(response.body)

        items = []
        for each in response.xpath("//li"):
            print(each.extract())

            item = ComicspiderItem()
            names = each.xpath(".//@title").extract()
            if len(names) > 0:
                item["name"] = names[0]

            url_links = each.xpath(".//@href").extract()
            if len(url_links) > 0:
                item["link_url"] = url_links[0]

            url_images = each.xpath(".//@src").extract()
            if len(url_images) > 0:
                item["image_url"] = url_images[0]

            items.append(item)

            print("-------------")
            # item = ComicspiderItem()
            #
            # names = each.xpath("@title").extract()
            # if len(names) > 0:
            #     item["name"] = names[0]
            #
            # print(each.extract())
            # images = each.xpath("//@src").extract()
            # print(images)

        return items
