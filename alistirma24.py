"""
Problem 4
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri *isimlere* göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
"""


adlar = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyadlar = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(adlar,soyadlar))
liste.sort()

for x in liste:
    
    print("{} {}".format(x[0],x[1]))
                                                                                                                                                                                             