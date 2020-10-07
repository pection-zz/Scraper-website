import scrapy

class AlibabaCategorySpider(scrapy.Spider):
    name = 'category'
    start_urls = [
        'https://quotes.toscrape.com/'

    ]
    def parse(self,response):
        title = response.css('title::text').extract()
        yield {'titletext': title}
