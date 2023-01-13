import requests
from bs4 import BeautifulSoup

# Website 1
website1 = "website api"
page1 = requests.get(website1)
soup1 = BeautifulSoup(page1.content, "html.parser")
price1 = soup1.find("span", class_="price").get_text(0)

# Website 2
website2 = "Website api"
page2 = requests.get(website2)
soup2 = BeautifulSoup(page2.content, "html.parser")
price2 = soup2.find("span", class_="price").get_text()

if float(price1) < float(price2):
    print(f"The price on {website1} is cheaper: {price1}")
elif float(price1) > float(price2):
    print(f"The price on {website2} is cheaper: {price2}")
else:
    print(f"The prices on both websites are equal: {price1}")
