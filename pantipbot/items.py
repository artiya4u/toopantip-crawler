import scrapy


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
