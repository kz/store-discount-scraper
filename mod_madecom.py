# Import scraping modules and database.
from lxml import html
import requests
import main_database

def madecom():
    # Create a table as specified below if it doesn't exist.
    table_columns = [
        ['sku','text unique'],
        ['name','text'],
        ['url','text'],
        ['image','text'],
        ['price_regular','mediumint'],
        ['price_discounted','mediumint'],
        ['description','longtext']
    ]
    main_database.create_table('madecom',table_columns)

    # Scrape list of sale pages.
    base_page = requests.get('http://www.made.com/sale')
    base_page_text = html.fromstring(base_page.text)
    sale_page_urls = base_page_text.xpath('/html/body/div[3]/div[2]/div/div/div/div/div/a/@href')
    
    # Define arrays.
    product_skus = []
    product_names = []
    product_urls = []
    product_images = []
    product_prices_regular = []
    product_prices_discounted = []
    product_descriptions = []
    
    # Scrape product information and insert into database for each sale page.
    for sale_page_url in sale_page_urls:
        products = []
        sale_page = requests.get(sale_page_url)
        sale_page_text = html.fromstring(sale_page.text)
        
        # Scrape all information available directly on the sale page.
        product_names += sale_page_text.xpath('//*[starts-with(@id, "list-item-")]/h3/a/text()')
        product_urls += sale_page_text.xpath('//*[starts-with(@id, "list-item-")]/h3/a/@href')
        product_images += sale_page_text.xpath('//*[starts-with(@id, "list-item-")]/a/img[not(@class="preview")]/@src')
        product_prices_regular += sale_page_text.xpath('//*[starts-with(@id, "old-price-")]/text()')
        product_prices_discounted += sale_page_text.xpath('//*[starts-with(@id, "product-price-")]/text()')
        
        # Trim pound signs (and whitespace) from the scraped information and then convert these strings into integers (in pence form, i.e., '£39.99' -> '39.99' -> '3999').
        for index, product_price_regular in enumerate(product_prices_regular):
            product_price_regular = product_price_regular.replace('\r','')
            product_price_regular = product_price_regular.replace('\n','')
            product_price_regular = product_price_regular.replace(' ','')
            product_price_regular = product_price_regular.replace('£','')
            product_price_regular = product_price_regular.replace('.','')
            product_price_regular = product_price_regular.replace(',','')
            if product_price_regular == '':
                product_price_regular = 0
            else:
                product_price_regular = int(product_price_regular) * 100
            product_prices_regular[index] = product_price_regular
        for index, product_price_discounted in enumerate(product_prices_discounted):
            product_price_discounted = product_price_discounted.replace('\r','')
            product_price_discounted = product_price_discounted.replace('\n','')
            product_price_discounted = product_price_discounted.replace(' ','')
            product_price_discounted = product_price_discounted.replace('£','')
            product_price_discounted = product_price_discounted.replace('.','')
            product_price_discounted = product_price_discounted.replace(',','')
            if product_price_discounted == '':
                product_price_discounted = 0
            else:
                product_price_discounted = int(product_price_discounted) * 100
                
            product_prices_discounted[index] = product_price_discounted
        
        # Remove last entries from arrays as these are for gift card entries.
        product_names.pop(-1)
        product_urls.pop(-1)
        product_images.pop(-1)        
        
        # Scrape all information only available inside product pages.
        for product_url in product_urls:
            product_url_page = requests.get(product_url)
            product_url_page_text = html.fromstring(product_url_page.text)
            
            product_sku = product_url_page_text.xpath('//span[@class="identifier"]/span[@class="value"]/text()')
            product_sku = product_sku[0].replace('\n','')
            product_sku = product_sku.replace(' ','')
            product_skus += product_sku
            
            product_description_headers = product_url_page_text.xpath('/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[*]/div[*]/h2/text()')
            product_description_text = product_url_page_text.xpath('/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[*]/div[*]/p/text()')
            product_description = []
            for index, product_description_header in enumerate(product_description_headers):
                if product_description_header != 'Visit us':
                    try:
                        product_description += [[product_description_headers[index], product_description_text[index]]]
                        product_descriptions += product_description
                    except IndexError:
                        product_description += [[product_description_headers[index]]]
                        product_descriptions += product_description
                        
        # Compile all the separate lists into a two-dimensional list.
        for index, product_name in enumerate(product_names):
            products += [[product_skus[index], product_names[index], product_urls[index], product_images[index], product_prices_regular[index], product_prices_discounted[index], product_descriptions[index]]]
            
        # Insert the scraped information into the database.
            main_database.madecom(products)