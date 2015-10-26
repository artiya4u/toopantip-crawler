from scrapy.exceptions import DropItem


class FilterExistTopicPipeline(object):
    """
        Filter exist topic item by id.
    """

    # put all words in lowercase
    topic_ids = set()

    def process_item(self, item, spider):
        for tid in self.topic_ids:
            if tid in item['id']:
                raise DropItem("Already have topic: %s" % tid)
        else:
            self.topic_ids.add(item['id'])
            return item
