import scrapy
class DangdangspiderSpider4(scrapy.Spider):
    name = "dangdangSpider4"
    allowed_domains = ["book.dangdang.com"]
    start_urls = ["https://book.dangdang.com/01.54.htm?ref=book-01-A"]

    def parse(self, response):

        # context = response.xpath('/html/head/title/text()')   
        # title = context.extract_first()  
        
        filename="dangdang.html"
        open(filename,'wb').write(response.body)