import scrapy


class InfoScraper(scrapy.Spider):
    name = "spiderman"
    start_urls = [
        # 'http://quotes.toscrape.com/'
        'https://www.google.ca/search?q=pencil&oq=pencil&aqs=chrome.0.69i59.1289j0j1&sourceid=chrome&ie=UTF-8'
    ]

    def parse(self, response):
        # BLOCK_SELECTOR = '.st'
        for block in response.css('.s'):
            yield {
                'Content': block.css('.st').extract_first(),
            }
