

import scrapy
from scrapy.utils.reactor import install_reactor 
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
from scrapy import Selector
from scrapy_playwright.page import PageMethod
import logging
from datetime import datetime

def should_abort_request(req):

    if req.resource_type == "image":
        logging.log(logging.INFO, f"Ignoring Image {req.url}")
        return True
    if req.method.lower() == 'post':
        logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
        return True

    return False

class A1Spider(scrapy.Spider):
    name = "1"
    custom_settings = {

        

         "proxy": {
                "server": "http://proxy.scrapeops.io:5353" ,
                "username": "scrapeops.headless_browser_mode=true",
                "password": "e4ea08af-ef35-4354-885d-e75b34979a52",
            } ,
     
        'FEEDS': {
            f'links-{datetime.now()}.csv': 
        #     'links.csv':
            {
                'format': 'csv'
            }},
        #'PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT': '100000',
        #'PLAYWRIGHT_ABORT_REQUEST': should_abort_request ,

    }


    def start_requests(self):
        for k in range (1,228) :

            yield scrapy.Request(
           # url= link ,
           url = f'https://www.bilbasen.dk/brugt/bil?includeengroscvr=true&pricefrom=0&includeleasing=true&fuel=3&page={k}',

            callback=self.parse1,
                           
                meta=dict(
                playwright = True,
                playwright_include_page = True ,
                
                playwright_page_methods = [


         ],
                errback =self.errback 
            ))

    

    async def parse1(self, response):
              
              
        page = response.meta["playwright_page"]
        await page.close()


        for i in  range (6,41):

            cars= response.xpath(f'//*[@id="srp-content"]/div[{i}]/div[2]/div[1]/a/text()').extract()

            KM= response.xpath(f'//*[@id="srp-content"]/div[{i}]/div[3]/div[1]/div[3]/text()').extract()
            
            year= response.xpath(f'//*[@id="srp-content"]/div[{i}]/div[3]/div[1]/div[4]/text()').extract()

            price= response.xpath(f'//*[@id="srp-content"]/div[{i}]/div[3]/div[1]/div[5]/text()').extract()
            
            
            

            

            yield{
               'car' : cars ,
               'Kilometer'  : KM ,
               'Year'   : year

            }

#        links = response.css('.item_inner::attr(href)').extract() 

#        for link in links:3


#           
        
        
        
    async def errback(self,failure) :
        page = failure.request.meta["playwright_page"]
        await page.close()