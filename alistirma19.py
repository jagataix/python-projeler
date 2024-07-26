"""
Problem 1
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]

*Not : map() fonksiyonunu kullanmaya çalışın.*

Problem 2
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

*** Not: filter() fonksiyonunu kullanmaya çalışın. ***

Problem 3
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

*Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.*

Problem 4
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.

*Not: zip() fonksiyonunu kullanmaya çalışın. *
"""                                       
 
"1"
from functools import*

def alan(x):
    return x[0]*x[1]
                                                                                                                                                                                                                                       

kenarlar = [(10,5),(8,12),(7,13),(4,17)]

alanlar= list(map(alan,kenarlar))

print(alanlar)

"2"

def ucgen_mi(a):
    if(a[0]**2 +a[1]**2 ==a[2]**2):
        return True
    else:
        return False
        
kenar = [(7,24,25),(2,11,18),(5,12,13)]

ucgenler = list(filter(ucgen_mi,kenar))

print(ucgenler)

"3"

sayilar = [1,5,12,4,9,16,11,8]

cift = list(filter(lambda x : x % 2 == 0,sayilar))

print(reduce(lambda x,y: x+y,cift))

"4"

adlar = ["Kerim","Mehmet","Yavuz","Rıza"]
soyadlar = ["Özhaseki","Şentürk","Kabadayı","Alsancak"]

liste=list(zip(adlar,soyadlar))

for i,j in liste:
    print(i,j)














