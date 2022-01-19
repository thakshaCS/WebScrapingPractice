
import urllib.request
from bs4 import BeautifulSoup

website_url = "https://www.newegg.ca/p/pl?d=graphics+cards"
uClient = urllib.request.urlopen(website_url)  # downloads webpage
page_html = uClient.read()  # offloads content into variable
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")  # parse file as html file
# page_soup.h1 # grabs header
containers = page_soup.findAll("div", {"class":"item-container"})  # grabs all
# div that have the class item-container, returned as a list


# open a file
filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)
print(containers[0].a.img["title"])
for container in containers:
    brand_container = container.findAll("div", {"class": "item-branding"})
    brand = brand_container[0].a.img["title"]  # index as if its a dictionary  to grab an  attribute
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("name: " + product_name)
    print("shipping: " + shipping)
    f.write(
        brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
f.close()
