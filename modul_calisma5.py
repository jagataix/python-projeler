import requests

from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

html_içerik = response.content



x = BeautifulSoup(html_içerik,"html.parser")
filmler = x.find_all("h3",{"class":"ipc-title__text"})
filmler.pop(0)

puanlar = x.find_all("span",{"class":"ipc-rating-star--rating"})

sayı = float(input("Filtrelemek istediğiniz puan değerini giriniz :"))
 
for y,z in zip(filmler,puanlar):
    a = str(y.text)
    b = a[3:]
    if(b[0]==" "):
       c = b[1:]
    else:
        c = b
    if float(z.text) >= sayı:  
       print("Film :",c," Puanı :",z.text)
       print("-----------")

                                                                                                    