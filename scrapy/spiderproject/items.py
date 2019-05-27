# -*- coding: utf-8 -*-
import scrapy


class WikiItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 链接
    link = scrapy.Field()
    # 时间
    data_time = scrapy.Field()
    # 类型
    class_another = scrapy.Field()
    pass
