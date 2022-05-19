import scrapy
from ..items import MytheresaItem
class MytheresaSpider(scrapy.Spider):
    name = 'mytheresa'
    allowed_domains = ['https://www.mytheresa.com/int_en/men/shoes.html']
    start_urls = ['https://www.mytheresa.com/int_en/men/shoes.html',
                  'https://www.mytheresa.com/int_en/men/shoes.html?p=2',
                  'https://www.mytheresa.com/int_en/men/shoes.html?p=3',
                  'https://www.mytheresa.com/int_en/men/shoes.html?p=4',
                  'https://www.mytheresa.com/int_en/men/shoes.html?p=5',
                  'https://www.mytheresa.com/int_en/men/shoes.html?p=6',
                  'https://www.mytheresa.com/int_en/men/shoes.html?p=7',
                  ]
    page=1

    def parse(self, response,**kwargs):

        name1 = response.xpath('//span[@class="ph1"]/text()').extract()
        name2=response.xpath('//a[@class="pa1-rm"]/text()').extract()
        price = response.xpath('//span[@class="price"]/text()').extract()
        yield {"name1":name1}
        yield {"name2": name2}
        yield {"price": price}

        next='https://www.mytheresa.com/int_en/men/shoes.html?p='+str(MytheresaSpider.page)
        print(next)
        yield response.follow(next, callback=self.parse)

        if MytheresaSpider. page <=8:
            MytheresaSpider.page += 1
            print("page num",MytheresaSpider.page)
            yield response.follow(next, callback=self.parse)











