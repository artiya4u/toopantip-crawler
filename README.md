# TooPantip Crawler

Script to generate Pantip topics for TooPantip App.

## Run
```bash
    scrapy runspider pantip_spider.py -o topics.json
```

## Cron
```cron
    */5 * * * * scrapy runspider /home/ubuntu/toopantip-crawler/pantip_spider.py -o \
    /home/ubuntu/topics.json >> crawler.log
```

## Check 

Link: http://toopantip.artiya.me/topics.json