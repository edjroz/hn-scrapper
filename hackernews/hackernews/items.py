from scrapy.item import Item, Field


class HackerNewItem(Item):
    title = Field()
    url = Field()
