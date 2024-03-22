import pandas as pd
import httpx 
from selectolax.parser import HTMLParser

url = "https://www.wrs.it/fr/627-amortisseur-de-direction"

def get_html(base_url, page):
    resp = httpx.get(url)
    html = HTMLParser(resp.text)

    products = html.css('article[data-id-product]')
    for product in products:
        product.css_first('a[class*="thumbnail"]').attributes['href']

def main():
    page_number = 1

    for i in range(36):
        i = f"https://www.wrs.it/fr/627-amortisseur-de-direction?page={page_number}"
        page_number += 1
        print(i)

        #html = get_html(base_url, page=f"?page=" + f"{page_number}")
        

if __name__ == "__main__":
    main()
    #document.querySelectorAll('article[data-id-product]')