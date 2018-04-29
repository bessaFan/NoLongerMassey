from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from bs4 import BeautifulSoup

urls = []


class InfoScraper(scrapy.Spider):
    name = "spiderman"
    start_urls = urls

    def parse(self, response):
        for block in response.css('.s'):
            text = BeautifulSoup(block.css('.st').extract_first(), 'lxml').get_text().replace("\n", "")
            if "..." not in text:
                paragraphs.append(text)
                yield {
                    'article': text,
                }
            # next_page = response.css('cite::text').extract_first()
            # print(next_page)
            # if next_page is not None:
            #     yield response.follow(next_page, callback=self.parse)


paragraphs = []


def return_query(query):
    return return_query(query, 15)


def return_query(query, num_queries):
    query = query.replace(" ", "+")
    return "http://www.google.com/search?q=" + query + "&num=" + str(num_queries)


def run(query):
    urls.append(return_query(query, 15))
    print(urls[0])
    runner = CrawlerRunner()
    d = runner.crawl(InfoScraper())
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
    return ' '.join(map(str, paragraphs))
