#!/usr/bin/env bash

# Export path for scrapy.
PATH=$PATH:/usr/local/bin
export PATH

file=topics-temp.json
minimum_size=2000
rm ${file}
scrapy crawl pantipspider -o ${file} --logfile pantip_spider.log
actual_size=$(wc -c <"$file")
if [ ${actual_size} -ge ${minimum_size} ]; then
    # Move temp file to real file.
    mv -f ${file} topics.json
fi


