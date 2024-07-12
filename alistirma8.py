"""
Programlama Ödevi - Fonksiyonlar
Tebrikler! Bölümü başarıyla bitirdiniz. Şimdi, öğrendiklerinizin akılda kalması için ödevinizi yapma zamanı!

*Not: Buradaki tüm problemler sizin algoritma yeteneğinizi oldukça geliştirecektir. O yüzden zorlandığınız noktalarda pes etmeyin. Üzerine kafa yormaya ve sürekli denemeye çalışın.*

Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok

Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok

Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi

Problem 5
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
"""

"1"

def mukemmmel(x):
    toplam=0
    for i in range(1,x):
        if x % i == 0 :
            toplam+= i
    if toplam == x:
        return True
    else:
        return False
    
sayi=int(input("Bir sayi gir :"))

if mukemmmel(sayi):
    print("Bu bir mukemmel sayıdır.")
else:
    print("Bu bir mukemmel sayı değildir.")
    
print("\n\n")

"2 ve 3"

def EBOB(x,y):
    deger=1
    if x<y:
        c=x
    else:
        c=y
    for i in range(1,c+1):
        if x%i == 0 and y%i == 0 :
            deger = i
    
    return deger
    
    

a=int(input("Birinci sayiyi giriniz :"))
b=int(input("İKinci sayiyi giriniz :"))



print("{} ve {} sayılarının EBOB'u {}".format(a,b,EBOB(a,b)))
print("{} ve {} sayılarının EKOK'u {}".format(a,b,a*b/EBOB(a,b)))

print("\n\n")

"4"

def okunus(x):
    yaziyla=[]
    
    if(x[0]=="1"):
        yaziyla.append("On")
    elif(x[0]=="2"):
        yaziyla.append("Yirmi")
    elif(x[0]=="3"):
        yaziyla.append("Otuz")
    elif(x[0]=="4"):
        yaziyla.append("Kırk")
    elif(x[0]=="5"):
        yaziyla.append("Elli")
    elif(x[0]=="6"):
        yaziyla.append("Altmış")
    elif(x[0]=="7"):
        yaziyla.append("Yetmiş")
    elif(x[0]=="8"):
        yaziyla.append("Seksen")
    elif(x[0]=="9"):
        yaziyla.append("Doksan")

    if(x[1]=="1"):
        yaziyla.append("bir")
    elif(x[1]=="2"):
        yaziyla.append("iki")
    elif(x[1]=="3"):
        yaziyla.append("üç")
    elif(x[1]=="4"):
        yaziyla.append("dört")
    elif(x[1]=="5"):
        yaziyla.append("beş")
    elif(x[1]=="6"):
        yaziyla.append("altı")
    elif(x[1]=="7"):
        yaziyla.append("yedi")
    elif(x[1]=="8"):
        yaziyla.append("sekiz")
    elif(x[1]=="9"):
        yaziyla.append("dokuz")


    return yaziyla



sayi=input("Bir sayı giriniz :")

yazi=okunus(sayi)

print(yazi[0],yazi[1])


print("\n\n")

"5"

def pisagor():
    pis=list()
    
    for x in range(1,101):
        for y in range(1,101):
            c=(x**2 + y**2)**0.5
            if c==int(c):
                pis.append((x,y,int(c)))
    
    return pis
                
for i in pisagor():
    print(i)




