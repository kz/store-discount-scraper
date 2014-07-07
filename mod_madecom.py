#Import scraping modules.
from lxml import html
import requests

def madecom():
    #Scrape list of sale pages.
    base_page = requests.get('http://www.made.com/sale')
    base_page_text = html.fromstring(base_page.text)
    sale_page_urls = base_page_text.xpath('/html/body/div[3]/div[2]/div/div/div/div/div/a/@href')
    product_images = []
    #Scrape all product information.
    for sale_page_url in sale_page_urls:
        sale_page = requests.get(sale_page_url)
        sale_page_text = html.fromstring(sale_page.text)
        product_images += sale_page_text.xpath('//*[starts-with(@id, "list-item-")]/a/img[not(@class="preview")]/@src')
    return product_images