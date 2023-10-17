# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

creat_tabel_sql="""
    create table if not exists dangdanginfo(
    id int auto_increment primary key,
    title varchar(255),
    author varchar(255),
    price float
    )
"""
sql="""
insert into dangdanginfo(
title,author,price
)
values(
\"{}\",\"{}\",{}
)
"""
db=pymysql.connect(host='localhost',user='root',passwd='1928374655',port=3306,db='homework')
cursor=db.cursor()
class MyspiderPipeline:
    def process_item(self, item, spider):
        
        item=dict(item)
        cursor.execute(sql.format(item['title'],item['author'],item['price']))
        db.commit()
        return item
