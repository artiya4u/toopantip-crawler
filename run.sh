#!/usr/bin/env bash

# Export path for scrapy.
PATH=$PATH:/usr/local/bin
export PATH

# Run crawler.
scrapy runspider pantip_spider.py -o topics-temp.json

# Move temp file to real file.
mv -f topics-temp.json topics.json
