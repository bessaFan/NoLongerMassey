import scrapy
from bs4 import BeautifulSoup


# noinspection SpellCheckingInspection
class InfoScraper(scrapy.Spider):
    name = "spiderman"
    start_urls = [
        'https://www.google.ca/search?q=pencil&oq=pencil&aqs=chrome..69i57j0l5.1309j1j9&sourceid=chrome&ie=UTF-8'
    ]

    def parse(self, response):
        for block in response.css('.s'):
            print(block)
            text = BeautifulSoup(block.css('.st').extract_first(), 'lxml').get_text()
            yield {
                'article': text.replace("\n", ""),
            }
            next_page = response.css('cite::text').extract_first()
            print(next_page)
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
