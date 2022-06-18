import requests
from bs4 import BeautifulSoup
import re

url = "https://www.amazon.co.uk/hz/wishlist/ls/1EZ8OPSIRSFPT"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

items = soup.find_all("h2", class_ = "a-size-base")

#re.compile is a "regex" in case you forget

item_title = soup.find("a", id=re.compile("itemName_")).get_text()
item_price = soup.find(class_ = "a-offscreen").get_text()
item_discount = soup.find("span", id=re.compile("itemPriceDrop_")).get_text()

print(item_title) 
print(item_price)
print(item_discount) 






