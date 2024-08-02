import requests

import sys

url = "http://api.frankfurter.app/latest?from="
ilk_döviz = input("İlk Döviz :")
ikinci_döviz = input("İkinci Döviz :")

para = float(input("Çevireceğiniz değeri giriniz :"))
veri = requests.get(url + ilk_döviz)

json_verisi = veri.json()
try:
    print(para,ilk_döviz,"=",(json_verisi["rates"][ikinci_döviz])* para,ikinci_döviz)
except KeyError:
    sys.stderr.write("Para birimlerini yanlış girdiniz!")
    sys.stderr.flush()
                                                                                                                  