# -*- coding: utf-8 -*-
from datetime import datetime
import scrapy
from scrapy.crawler import CrawlerProcess


class PantipSpider(scrapy.Spider):
    name = 'pantipspider'
    start_urls = ['http://pantip.com/forum']
    allowed_domains = ["pantip.com"]

    def parse(self, response):
        for url in response.xpath('//a/@href').re(r'/topic/[0-9]+'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        item = TopicItem()
        item['feed'] = 'http://pantip.com/forum'
        item['favicon'] = response.urljoin(response.css('div.display-post-avatar > a > img::attr(src)').extract()[0])
        item['description'] = response.xpath("//meta[@property='og:description']/@content").extract()[0]
        item['proof'] = response.css('span.like-score::text').extract()[0]
        item['image'] = response.xpath("//meta[@property='og:image']/@content").extract()[0]

        item['timestamp'] = datetime.utcnow().isoformat(' ')
        item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()[0]
        item['type'] = response.xpath("//meta[@property='og:type']/@content").extract()[0]
        item['title'] = response.xpath("//meta[@property='og:title']/@content").extract()[0]
        item['id'] = item['url'].rsplit('/', 1)[-1]

        try:
            tag = response.css("a.tag-item::text").extract()[0]
            item['category'] = tag
        except IndexError:
            item['category'] = u'ไม่ระบุ'

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


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(PantipSpider)
process.start()

