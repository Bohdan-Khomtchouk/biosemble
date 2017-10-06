#!/usr/bin/env python

# Copyright (C) 2017 Bohdan Khomtchouk
# This file is part of biosemble.

# -------------------------------------------------------------------------------------------


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NciPipeline(object):
    def process_item(self, item, spider):
        return item
