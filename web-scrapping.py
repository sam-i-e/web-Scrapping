import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
req = requests.get(url)

page = BeautifulSoup(req.content, "html.parser")
print(page.prettify())

title = page.head
print(title.text)

all_products = []
col = ['Name', 'Price']

products = page.findAll("div", {"class": "_3pLy-c row"})
print(products)

for product in products:
    lname = product.select("div > div._4rR01T")[0].text.strip()
    print(lname)
    price = product.select("div > div._30jeq3 ")[0].text.strip()
    print(lprice)

    all_products.append([lname, lprice])

print("Record Inserted Successfully...")

data = pd.DataFrame(all_products, columns=col)
print(data)
data.to_csv('laptop_products.csv', index=False)