# -*- coding: utf-8 -*-
from datetime import datetime
import scrapy


class PantipSpider(scrapy.Spider):
    name = 'pantipspider'
    start_urls = ['http://pantip.com/forum']
    allowed_domains = ["pantip.com"]

    def parse(self, response):
        for url in response.xpath('//a/@href').re(r'/topic/[0-9]+'):
            print(response.urljoin(url))
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        item = TopicItem()
        item['feed'] = 'http://pantip.com/forum'
        item['favicon'] = 'http://ptcdn.info/pantip/pantip_logo.png'
        item['description'] = response.xpath("//meta[@property='og:description']/@content").extract()[0]
        item['proof'] = response.css('span.like-score::text').extract()[0]
        item['image'] = response.xpath("//meta[@property='og:image']/@content").extract()[0]

        item['timestamp'] = datetime.utcnow().isoformat(' ')
        item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()[0]
        item['type'] = response.xpath("//meta[@property='og:type']/@content").extract()[0]
        item['title'] = response.xpath("//meta[@property='og:title']/@content").extract()[0]
        item['id'] = item['url'].rsplit('/', 1)[-1]
        item['category'] = u'ทั่วไป'
        tag = response.css("a.tag-item::text").extract()[0]
        if tag:
            item['category'] = tag

        item['article_url'] = item['url']
        yield item


class TopicItem(scrapy.Item):
    feed = scrapy.Field()
    favicon = scrapy.Field()
    description = scrapy.Field()
    proof = scrapy.Field()
    image = scrapy.Field()

    timestamp = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    id = scrapy.Field()

    category = scrapy.Field()
    article_url = scrapy.Field()