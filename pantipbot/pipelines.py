from scrapy.exceptions import DropItem


class FilterExistTopicPipeline(object):
    """
        Filter exist topic item by id.
    """

    # put exist topic.
    topic_ids = set()
    banned_ids = list()

    # Image is too scared.
    banned_ids.append('34382712')

    def process_item(self, item, spider):
        if item['id'] in self.topic_ids:
            raise DropItem("Already have topic: %s" % item['id'])
        elif item['id'] in self.banned_ids:
            raise DropItem("Banned topic: %s" % item['id'])
        else:
            self.topic_ids.add(item['id'])
            return item
