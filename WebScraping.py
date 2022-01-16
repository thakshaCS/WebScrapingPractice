import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

website_url = "https://www.newegg.ca/p/pl?d=graphics+cards"
uClient = urlopen(website_url)  # downloads webpage
page_html = uClient.read()  # offloads content into variable
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")  # parse file as html file
# page_soup.h1 # grabs header
containers = page_soup.findAll("div", {"class":"item-container"}) # grabs all
# div that have the class item-container, returned as a list

for container in containers:
    brand = container.div.div.a.img["title"] # index as if its a dictionary
    # to grab an # attribute
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
