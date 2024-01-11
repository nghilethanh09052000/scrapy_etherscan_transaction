import scrapy
import json

class IndexSpider(scrapy.Spider):

    name = "index"

    def start_requests(self):
        for i in range(1, 21):
            post_body = {
                "cmd"       : "request.get",
                "url"       : f"https://etherscan.io/token/generic-tokenholders2?m=light&a=0x9F52c8ecbEe10e00D9faaAc5Ee9Ba0fF6550F511&s=114340911000000000000000000&sid=8c8f147ae230344f6ec7a8c52859a197&p={i}",
                "maxTimeout": 60000
            }
            json_data = json.dumps(post_body)
            yield scrapy.Request(
                url      = 'http://localhost:8191/v1',
                method   = "POST",
                headers  = {
                    'Content-Type': 'application/json'
                },
                body = json_data,
                callback=self.parse
            )
    
    def parse(self, response, **kwargs):
        data = response.json()
        html = data['solution']['response']
        selector   = scrapy.Selector(text=html)

        rows = selector.xpath('//div[@id="maintable"]/div[2]/table/tbody/tr')
        for row in rows:
            yield {
                'rank'        : str(row.xpath('./td[1]/text()').get()),
                'address'     : str(row.xpath('./td[2]/div//a[@class="js-clipboard link-secondary "]/@data-clipboard-text').get()),
                'quantity'    : str(row.xpath('./td[3]/text()').get()),
                'value'       : str(row.xpath('./td[5]/text()').get().replace('$','').replace(',',''))
            }
    
