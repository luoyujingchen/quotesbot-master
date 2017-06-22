# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/review/best/']
    n = 0



    def parse(self, response):
        for title in response.css("h3.title"):
            url = title.css("a[class~=title-link]::attr(href)").extract_first()
            scrapy.Request(url, self.getText)

        next_page_url = response.css("link.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            if self.n <= 2:
                self.n = self.n +1
            else:
                raise CloseSpider('Here we are!')
            yield scrapy.Request(response.urljoin(next_page_url))

    def getText(self,response):
        yield {
            'title' : response.xpath("//h1/span/text()"),
            'useful_count' : response.css("button[class~=useful_count]::text")
        }