#coding=gbk
import scrapy
from bs4 import BeautifulSoup

# 运行时
# cd git/novelSpider
# scrapy crawl lewen

class NovelSpider(scrapy.Spider):

    name = "lewen"

    def start_requests(self):

        urls = ['http://www.lwxs3.com/0/1/42.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        output = open('1.txt', 'a+')
        soup = BeautifulSoup(response.body)
        title = (soup.title.get_text()).split("_")[1]
        output.write(title+"\n")
        content = soup.find("div", class_="panel-body content-body content-ext").get_text()
        output.write(content+"\n")
        next_page = soup.find("li",class_="next").a.get("href")
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)