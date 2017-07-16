import requests

from bs4 import  BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Ankara"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")


print(soup.find_all("div",{"class":"yp-poi-box-2"}))






