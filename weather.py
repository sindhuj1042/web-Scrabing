import requests
from bs4 import BeautifulSoup
search="Weather in Erode"
url=f"https://www.google.com/search?&q={search}"
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
updates=s.find("div",class_="BNeawe").text
print(updates)