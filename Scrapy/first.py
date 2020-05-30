from scrapy import item,Field
class Article(Item):
    #define the fields for your item here like:
    # name = scrapy.Field()
    title=Field()
    
