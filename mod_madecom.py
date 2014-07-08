#Import scraping modules.
from lxml import html
import requests

def madecom():
    #Scrape list of sale pages.
    base_page = requests.get('http://www.made.com/sale')
    base_page_text = html.fromstring(base_page.text)
    sale_page_urls = base_page_text.xpath('/html/body/div[3]/div[2]/div/div/div/div/div/a/@href')
    
    #Define arrays.
    product_names = []
    product_urls = []
    product_images = []
    product_prices_regular = []
    product_prices_discounted = []
    product_descriptions = []
    
    products = []
    
    #Scrape all product information.
    for sale_page_url in sale_page_urls:
        sale_page = requests.get(sale_page_url)
        sale_page_text = html.fromstring(sale_page.text)
        
        product_names += sale_page_text.xpath('//*[starts-with(@id, "list-item-")]/h3/a/text()')
        product_urls += sale_page_text.xpath('//*[starts-with(@id, "list-item-")]/h3/a/@href')
        product_images += sale_page_text.xpath('//*[starts-with(@id, "list-item-")]/a/img[not(@class="preview")]/@src')
        product_prices_regular += sale_page_text.xpath('//*[starts-with(@id, "old-price-")]/text()')
        product_prices_discounted += sale_page_text.xpath('//*[starts-with(@id, "product-price-")]/text()')
        
        #product_descriptions += sale_page_text.xpath('')        
        
        #Trim pound signs (and whitespace).
        for index, product_price_regular in enumerate(product_prices_regular):
            product_price_regular = product_price_regular.replace('£','')
            product_prices_regular[index] = product_price_regular
        for index, product_price_discounted in enumerate(product_prices_discounted):
            product_price_discounted = product_price_discounted.replace(' ','')
            product_price_discounted = product_price_discounted.replace('£','')
            product_prices_discounted[index] = product_price_discounted
            
        #Remove last entries from arrays as these are for gift card entries.
        product_names.pop(-1)
        product_urls.pop(-1)
        product_images.pop(-1)
        
        #Compile all the separate lists into a two-dimensional list.
        for index, product_name in enumerate(product_names):
            products += [[product_names[index], product_urls[index], product_images[index], product_prices_regular[index], product_prices_discounted[index]]]
        
    return products