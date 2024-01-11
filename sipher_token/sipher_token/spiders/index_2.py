import scrapy
import pandas as pd


class Index3Spider(scrapy.Spider):
    name = "index_2"
    page = 0
    #max_retries = 20

    def start_requests(self):
        data = pd.read_csv('ather_wallets.csv')
        dict_data = data.to_dict(orient='records')

        self.wallet_address = [i.get('wallet_address') for i in dict_data]

        yield scrapy.Request(
            url      = f'https://etherscan.io/address/{self.wallet_address[self.page]}#multichain-portfolio',
            method='GET',
            meta={
                'wallet_address': self.wallet_address[self.page]
            },
            headers={
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': 'cf_chl_2=2014976871b2e22; ASP.NET_SessionId=dzerr5s3v1rtjtyn3z2mugyo; __cflb=02DiuFnsSsHWYH8WqVXbZzkeTrZ6gtmGUAKBDCYQJZPrc; _ga_T1JC9RNQXV=GS1.1.1704961940.1.0.1704961940.60.0.0; _ga=GA1.2.89710279.1704961940; _gid=GA1.2.1140073809.1704961945; etherscan_offset_datetime=+7; cf_clearance=CtlWvlr3G08bKuqjKu83.2_zsdU5UyPCydFMdZhTjyc-1704961945-0-2-1ec25fd0.9dc3df80.bcf4d68a-150.2.1704961945',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
            },
            cookies={
                "cf_chl_2": "2014976871b2e22",
                "ASP.NET_SessionId": "dzerr5s3v1rtjtyn3z2mugyo",
                "__cflb": "02DiuFnsSsHWYH8WqVXbZzkeTrZ6gtmGUAKBDCYQJZPrc",
                "_ga_T1JC9RNQXV": "GS1.1.1704961940.1.0.1704961940.60.0.0",
                "_ga": "GA1.2.89710279.1704961940",
                "_gid": "GA1.2.1140073809.1704961945",
                "etherscan_offset_datetime": "+7",
                "cf_clearance": "CtlWvlr3G08bKuqjKu83.2_zsdU5UyPCydFMdZhTjyc-1704961945-0-2-1ec25fd0.9dc3df80.bcf4d68a-150.2.1704961945"
            }

        )

    def parse(self, response):

        if self.page > len(self.wallet_address):
            return
 
        wallet_address = response.meta['wallet_address']

        yield {
            'wallet_address': wallet_address,
            'multichain_portfolio': response.xpath('//a[@id="multichain-button"]/span/text()').get().split('$')[1]
        }

        self.page +=1
        yield scrapy.Request(
            url      = f'https://etherscan.io/address/{self.wallet_address[self.page]}#multichain-portfolio',
            method='GET',
            meta={
                'wallet_address': self.wallet_address[self.page]
            },
            headers={
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': 'cf_chl_2=2014976871b2e22; ASP.NET_SessionId=dzerr5s3v1rtjtyn3z2mugyo; __cflb=02DiuFnsSsHWYH8WqVXbZzkeTrZ6gtmGUAKBDCYQJZPrc; _ga_T1JC9RNQXV=GS1.1.1704961940.1.0.1704961940.60.0.0; _ga=GA1.2.89710279.1704961940; _gid=GA1.2.1140073809.1704961945; etherscan_offset_datetime=+7; cf_clearance=CtlWvlr3G08bKuqjKu83.2_zsdU5UyPCydFMdZhTjyc-1704961945-0-2-1ec25fd0.9dc3df80.bcf4d68a-150.2.1704961945',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
            },
            cookies={
                "cf_chl_2": "2014976871b2e22",
                "ASP.NET_SessionId": "dzerr5s3v1rtjtyn3z2mugyo",
                "__cflb": "02DiuFnsSsHWYH8WqVXbZzkeTrZ6gtmGUAKBDCYQJZPrc",
                "_ga_T1JC9RNQXV": "GS1.1.1704961940.1.0.1704961940.60.0.0",
                "_ga": "GA1.2.89710279.1704961940",
                "_gid": "GA1.2.1140073809.1704961945",
                "etherscan_offset_datetime": "+7",
                "cf_clearance": "CtlWvlr3G08bKuqjKu83.2_zsdU5UyPCydFMdZhTjyc-1704961945-0-2-1ec25fd0.9dc3df80.bcf4d68a-150.2.1704961945"
            }

        )
