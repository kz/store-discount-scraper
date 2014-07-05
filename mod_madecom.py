#Import scraping modules
from lxml import html
import requests

def madecom():
    base_page = requests.get('http://www.made.com/sale')
    base_page_text = html.fromstring(base_page.text)
    sale_pages = base_page_text.xpath('/html/body/div[3]/div[2]/div/div/div/div/div/a/@href')
    return sale_pages
