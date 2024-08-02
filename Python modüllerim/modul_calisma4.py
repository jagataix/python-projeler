import requests

from bs4 import BeautifulSoup

bilgiler = requests.get("https://www.obilet.com/ucuslar/250_0-251_18/20240804/1a/economy/all")


html_içerik = bilgiler.content                                                                                              

x = BeautifulSoup(html_içerik,"html.parser")




for y in x.find_all('a'):
    print(y.get("href"))
    print("---------------------------------")
 
print("*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*--*-")
for y in x.find_all('a'):
    print(y.text)
    print("---------------------------------")



print(x.find_all("div",{"class":"list-container"}))

