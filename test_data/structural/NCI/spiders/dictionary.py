#!/usr/bin/env python

# Copyright (C) 2017 Bohdan Khomtchouk
# This file is part of biosemble.

# -------------------------------------------------------------------------------------------


# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.exceptions import CloseSpider
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from string import ascii_uppercase
import time
import json
from collections import OrderedDict
from bs4 import BeautifulSoup


class DictionarySpider(scrapy.Spider):
    name = "dictionary"
    allowed_domains = ["www.cancer.gov"]

    def __init__(self, *args, **kwargs):
        super(DictionarySpider, self).__init__(*args, **kwargs)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.filename = "Glossary_for_Next-Generation_DNA_Sequencing.json"
        self.dictionary = OrderedDict()

    def start_requests(self):
        # try:
        base = "http://seqinformatics.com/?page_id=32"
        # start_urls = [base + "?expand={}".format(i) for i in ascii_uppercase]
        #    print("**" * 10 + "\n" + base + "\n" + "**" * 10)
        # except:
        #    self.continue_ = False
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/46.0'}
        yield Request(url=base, headers=headers)
        # for item in start_urls:
        #    time.sleep(0.1)
        #    yield Request(url=item, headers=headers)

    def parse(self, response):
        # url = response.url
        # hxs = scrapy.Selector(response)
        # words = hxs.xpath("//*[@id='cgvBody']/div[2]/div/dl/dl/dt/dfn")
        # defs = hxs.xpath("//*[@id='cgvBody']/div[2]/div/dl/dl/dd")

        soup = BeautifulSoup(response.body, 'lxml')
        result = dict(i.text.strip().split(':', 1) for i in soup.findAll("p") if i.b)
        # defs = [i.text.strip() for i in soup.findAll("dd", {"class": "definition"})]
        # result = dict(zip(words, defs))
        if result:
            self.dictionary.update(result)
        else:
            print("*****EXIT*****")
            raise CloseSpider("It ran out of app!!!")
            # sys.exit(0)

    def spider_closed(self, spider):
        with open(self.filename, 'w') as f:
            json.dump(self.dictionary, f, indent=4)
