import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from bs4 import BeautifulSoup

urls = []
BLACKLIST = ['youtube', 'amazon', 'ebay', 'kijiji', 'bestbuy', 'petsmart', 'walmart', 'vimeo']


class InfoScraper(scrapy.Spider):
    name = "spiderman"
    start_urls = urls

    def parse(self, response):
        for block in response.css('.s'):
            next_page = response.css('cite::text').extract_first()
            if next_page not in BLACKLIST:
                text = BeautifulSoup(block.css('.st').extract_first(), 'lxml').get_text().replace("\n", "")
                if "..." not in text or "buy" not in text:
                    paragraphs.append(text)
                    yield {
                        'article': text,
                    }
                # print(next_page)
                # if next_page is not None:
                #     yield response.follow(next_page, callback=self.parse)

            text = BeautifulSoup(block.css('.st').extract_first(), 'lxml').get_text().replace("\n", "")
            paragraphs.append(text)
            yield {
                'article': text,
            }
            if "..." not in text:
                paragraphs.append(text)
                yield {
                    'article': text,
                }


paragraphs = []


def return_query(query, num_queries):
    query = query.replace(" ", "+")
    return "http://www.google.com/search?q=what+is+" + query + "&num=" + str(num_queries)


def run(query):
    urls.append(return_query(query, 35))
    print(urls[0])
    runner = CrawlerRunner()
    d = runner.crawl(InfoScraper())
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
    print(paragraphs)

    # run('benzene')
    return ' '.join(map(str, paragraphs))
