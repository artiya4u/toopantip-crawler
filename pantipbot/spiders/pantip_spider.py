# -*- coding: utf-8 -*-
import json
from datetime import datetime

import scrapy

from pantipbot.items import TopicItem


class PantipSpider(scrapy.Spider):
    name = 'pantipspider'
    start_urls = ['http://pantip.com/forum', 'http://m.pantip.com/desktop/',
                  'http://pantip.com/home/ajax_pantip_trend?p=1']
    allowed_domains = ["pantip.com"]

    def parse(self, response):
        print('URL:' + response.url)
        if response.url in ['http://pantip.com/forum', 'http://pantip.com/']:
            for url in response.xpath('//a/@href').re(r'/topic/[0-9]+'):
                yield scrapy.Request(response.urljoin(url), self.parse_topic)

        if response.url in ['http://pantip.com/home/ajax_pantip_trend?p=1']:
            json_response = json.loads(response.body)
            for topic in json_response['trend']:
                yield scrapy.Request(response.urljoin('http://pantip.com/topic/' + topic['topic_id']), self.parse_topic)

    @staticmethod
    def parse_topic(response):
        item = TopicItem()
        item['feed'] = 'http://pantip.com/'
        item['favicon'] = response.urljoin(response.css('div.display-post-avatar > a > img::attr(src)').extract()[0])
        item['description'] = response.xpath("//meta[@property='og:description']/@content").extract()[0]
        item['proof'] = response.css('span.like-score::text').extract()[0]
        item['image'] = response.xpath("//meta[@property='og:image']/@content").extract()[0]

        item['timestamp'] = datetime.utcnow().isoformat(' ')
        full_url = response.xpath("//meta[@property='og:url']/@content").extract()[0]
        tid = full_url.rsplit('/', 1)[-1]
        item['id'] = tid
        item['url'] = 'http://m.pantip.com/topic/' + tid
        item['type'] = response.xpath("//meta[@property='og:type']/@content").extract()[0]
        item['title'] = response.xpath("//meta[@property='og:title']/@content").extract()[0]

        try:
            tag = response.css("a.tag-item::text").extract()[0]
            item['category'] = tag
        except IndexError:
            item['category'] = u'ไม่ระบุ'

        yield item
