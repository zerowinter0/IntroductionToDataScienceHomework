from lxml import etree
import requests
import csv
import pymysql
db=pymysql.connect(host='localhost',user='root',passwd='1928374655',port=3306,db='homework')
cursor=db.cursor()
creat_tabel_sql="""
    create table if not exists movie(
    id int auto_increment primary key,
    name varchar(255)
    )
"""
cursor.execute(creat_tabel_sql)
sql="""
insert into movie(
name
)
values(
\"{}\"
)
"""
urls={'https://movie.douban.com/top250?start={}&filter='.format(str(i))for i in range(0,250,25)}
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'

}
for url in urls:
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    infos=selector.xpath("//ol[@class='grid_view']/li")
    for info in infos:
        name=info.xpath(".//div[@class='info']//div[@class='hd']//a/span[1]/text()")
        cursor.execute(sql.format(name))
db.commit()
db.close()
cursor.close()