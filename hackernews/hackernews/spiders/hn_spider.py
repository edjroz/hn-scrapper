from scrapy import Spider
from scrapy.selector import Selector

from hackernews.items import HackerNewItem

class HackerNewsSpider(Spider):
    name = "hackernews"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = [
        "http://news.ycombinator.com/",        
    ]
    def parse(self,response):
        sel = Selector(response)
        news = sel.xpath("//tr[@class='athing']/td[3]")
        
        for new in news:
            item = HackerNewItem()
            item['title'] = new.xpath("a[@href]/text()").extract()[0]
            item['url'] = new.xpath("a/@href").extract()[0]
            
            yield item
