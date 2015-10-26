#!/usr/bin/env bash

# Export path for scrapy.
PATH=$PATH:/usr/local/bin
export PATH

file=topics-temp.json
minimumsize=200

while true; do
    # Run crawler.
    scrapy runspider pantip_spider.py -o $file
    actualsize=$(wc -c <"$file")
    if [ $actualsize -ge $minimumsize ]; then
        # Move temp file to real file.
        mv -f $file topics.json
        break
    fi
done


