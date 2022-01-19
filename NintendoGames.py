import urllib.request
from bs4 import BeautifulSoup

# website we are scraping
website_url = "https://www.walmart.ca/search?q=apple"
uClient = urllib.request.urlopen(website_url)
page_html = uClient.read()  # offloads content into variable
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")  # parse file as html file
# containers = page_soup.findAll("div", {"class":"productItemRow_hyNOs row_1m0dd"})  # grabs all
# # div that have the class item-container, returned as a list
# print(containers[0])
