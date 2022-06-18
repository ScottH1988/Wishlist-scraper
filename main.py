import requests
from bs4 import BeautifulSoup
import re

url = "https://www.amazon.co.uk/hz/wishlist/ls/1EZ8OPSIRSFPT"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

items = soup.find_all("h2", class_ = "a-size-base")

#re.compile is a "regex" in case you forget
item_titles = soup.find_all("a", id=re.compile("itemName_"))
item_prices = soup.find_all(class_ = "a-offscreen")
item_discounts = soup.find_all("span", id=re.compile("itemPriceDrop_"))


for item_title in item_titles:
    print(item_title.get_text()) 
for item_price in item_prices:
    print(item_price.get_text()) 
for item_discount in item_discounts:
    print(item_discount.get_text()) 




"""
#this will print to a text file
   with open("items.txt", "a") as f:
         print(item_title, item_price, item_discount, file=f) 
"""
    









