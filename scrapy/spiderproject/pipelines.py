# -*- coding: utf-8 -*-
import pymysql
import sys
sys.getdefaultencoding()


class WikiPipeline(object):
    # 创建数据库连接
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="db_demo", charset='gb2312')

    def process_item(self, item, spider):

        title = item['title']
        link = item['link']
        data_time = item['data_time']
        class_another = item['class_another']

        # 把多出来的空格以及其它杂乱的东西处理掉并保存列表中
        wiki_title = []
        for x in range(len(title)):
            wiki_title.append(title[x].replace('\n', '').replace(' ', ''))

        wiki_link = []
        for a in range(len(link)):
            wiki_link.append(link[a])

        wiki_data_time = []
        for b in range(0, len(data_time), 3):
            wiki_data_time.append(data_time[b])

        wiki_class_another = []
        for c in range(0, len(class_another), 2):
            wiki_class_another.append(class_another[c])

		# 通过zip把四个列表组合在一起，插入数据库中
        for insert_q in list(zip(wiki_title, wiki_link, wiki_data_time, wiki_class_another)):
            sql_insert = "INSERT INTO wiki_info(title, link, data_time, class_another) VALUES ('{}', 'http://wiki.ioin.in{}', '{}', '{}')".format(insert_q[0], insert_q[1], insert_q[2], insert_q[3])
            print(sql_insert)
            self.conn.query(sql_insert)
        return item


    def close_spider(self):
        self.conn.close()
