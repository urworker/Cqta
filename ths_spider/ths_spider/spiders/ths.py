import scrapy


class ThsSpider(scrapy.Spider):
    name = 'ths'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
