# Scrapy settings for dirbot project

SPIDER_MODULES = ['pantipbot.spiders']
NEWSPIDER_MODULE = 'pantipbot.spiders'
DEFAULT_ITEM_CLASS = 'pantipbot.items.TopicItem'

ITEM_PIPELINES = {'pantipbot.pipelines.FilterWordsPipeline': 1}
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
