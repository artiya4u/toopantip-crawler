#!/usr/bin/env bash

# Export path for scrapy.
PATH=$PATH:/usr/local/bin
export PATH

file=topics-temp.json
unsorted_file=topics-unsorted.json
minimum_size=2000
rm ${file}
rm ${unsorted_file}
scrapy crawl pantipspider -o ${unsorted_file} --logfile pantip_spider.log
python sort_topic_json.py
actual_size=$(wc -c <"$file")
if [ ${actual_size} -ge ${minimum_size} ]; then
    # Move temp file to real file.
    mv -f ${file} topics.json
    sftp robot@artiya.me <<< $'put topics.json'
fi


