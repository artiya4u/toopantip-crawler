#!/usr/bin/env bash
scrapy runspider pantip_spider.py -o topics-temp.json
mv topics-temp.json topics.json
