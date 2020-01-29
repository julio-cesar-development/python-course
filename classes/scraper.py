# -*- coding: utf-8 -*-

# pip install scrapy
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re

class BlogSpider(scrapy.Spider):
  name = 'blogspider'
  allowed_domains = ['blackdevs.com.br']
  start_urls = ['https://blackdevs.com.br']

  def parse(self, response):
    # print('response.headers', response.headers)
    # print('response.body', response.body)
    # print('response.css', response.css)
    # print('response.status', response.status)
    # print('response.text', response.text)
    # print('response.url', response.url)

    # sel = Selector(text=r'Julio').get()
    # print('sel', sel)

    # print('\n')

    matches = re.search(r'<.*>Julio.*>', response.text)
    print(matches.group(0))

    print('\n')

    title = response.css('title::text').re(r'Port.*')
    print('title', title)

    print('\n')

    divs = response.xpath('//div').get()
    print('divs', divs)



# scrapy runspider scraper.py

# scrapy shell https://blackdevs.com.br
