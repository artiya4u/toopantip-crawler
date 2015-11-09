from scrapy.exceptions import DropItem


class FilterExistTopicPipeline(object):
    """
        Filter exist topic item by id.
    """

    # put exist topic.
    topic_ids = set()

    def process_item(self, item, spider):
        if item['id'] in self.topic_ids:
            raise DropItem("Already have topic: %s" % item['id'])
        else:
            self.topic_ids.add(item['id'])
            return item
