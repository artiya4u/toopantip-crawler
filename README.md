# TooPantip Crawler

Script to generate Pantip topics for TooPantip App.

## Run
```bash
    scrapy runspider pantip_spider.py -o topics.json
```

## Cron
```cron
    */5 * * * * scrapy runspider pantip_spider.py -o /var/www/html/topics.json
```

## Check 

Link: http://toopantip.artiya.me/topics.json