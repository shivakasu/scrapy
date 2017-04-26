import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'thunder'
    allowed_domains = ['xxxxx']
    start_urls = ['xxxxx']

    rules = (
        Rule(LinkExtractor(allow=('index\_\d+\.html')),follow=True),
        Rule(LinkExtractor(allow=('\/\d+\.html')),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        url=response.url
        title=response.xpath('//title/text()').extract()
        links=response.selector.re('thunder://[^<>]+<')
        self.save_in_file(url,title,links)


    def save_in_file(self,url,title,links):
        if len(links)==0:
            pass
        else:
            f=open('data_win.txt','a')
            f.write(url+"\r\n")
            f.write(title[0]+"\r\n")
            for link in links:
                f.write(link[:-1]+"\r\n")
            f.write("\r\n\r\n")
            f.close()
            f1=open('data_linux.txt','a')
            f1.write(url+"\n")
            f1.write(title[0]+"\n")
            for link in links:
                f1.write(link[:-1]+"\n")
            f1.write("\n\n")
            f1.close()
