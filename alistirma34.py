"""
Proje 3
https://www.doviz.com/ sitesinden anlık olarak doların,euronun,altının ve borsanın değerlerini öğrenin ve bunları kullanarak bir proje geliştirmeye çalışın.

*Not: Bu projeyi, requests ve beautifulsoup kullanarak geliştirin.*
"""

import requests

from bs4 import BeautifulSoup


url ="https://www.doviz.com/"

kaynak = requests.get(url)

html_ayırıcı = kaynak.content

parçalar = BeautifulSoup(html_ayırıcı,"html.parser")

adlar = parçalar.find_all("span",{"class":"name"})
değerler = parçalar.find_all("span",{"class":"value"})

for i,j in zip(adlar,değerler):
    print(i.text,j.text)
                                                                                                                                                                                                                                                       