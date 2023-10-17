import scrapy
import pymysql
from mySpider.items import MyspiderItem

db=pymysql.connect(host='localhost',user='root',passwd='1928374655',port=3306,db='homework')
cursor=db.cursor()
creat_tabel_sql="""
    create table if not exists dangdanginfo(
    id int auto_increment primary key,
    title varchar(255),
    author varchar(255),
    price float
    )
"""
class DangdangspiderSpider(scrapy.Spider):
    name = "dangdangSpider5"
    allowed_domains = ["search.dangdang.com"]
    start_urls = ["https://book.dangdang.com/01.54.htm?ref=book-01-A"]

    def parse(self, response):
        cursor.execute(creat_tabel_sql)
        cursor.close()
        db.commit()
        db.close()
        for each in response.xpath('//*[@class="product_ul"]//li'):
            title=each.xpath('./p[1]/a/text()').extract_first()
            author=each.xpath('./p[2]/text()').extract_first()
            price=each.xpath('./p[4]/span[1]/span[2]/text()').extract_first()+each.xpath('./p[4]/span[1]/span[3]/text()').extract_first()
            item= MyspiderItem(title=title,author=author,price=price)
            yield item

        