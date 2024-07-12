"""
Programlama Ödevi - Koşullu Durumlar
Tebrikler! Bölümü başarıyla bitirdiniz. Şimdi, öğrendiklerinizin akılda kalması için ödevinizi yapma zamanı!

Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF

Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

abs(-4)
4
abs(5)
5
"""

"1"

boy=float(input("Boyunuzu metre cinsinden giriniz :"))
kilo=int(input ("Kilonuzu giriniz                 :"))

endeks=kilo/(boy ** 2)

if endeks>30:
    print("Obez")
elif endeks>25:
    print("Fazla kilolu")
elif endeks>18.5:
    print("Normal")
else:
    print("Zayıf")

print("\n\n")

"2"

a=int(input("Birinci sayıyı giriniz :"))
b=int(input("İkinci sayıyı girinizb :"))
c=int(input("Üçüncü sayıyı giriniz  :"))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

print("\n\n")
    
"3"

vize1=int(input("Vize 1 notunuzu giriniz :"))
vize2=int(input("Vize 2 notunuzu giriniz :"))
final=int(input("Final  notunuzu giriniz :"))

net=vize1*(3/10)+vize2*(3/10)+final*(4/10)

if net>90:
    print("AA")
elif net>85:
    print("BA")
elif net>80:
    print("BB")
elif net>75:
    print("CB")
elif net>70:
    print("CC")
elif net>65:
    print("DC")
elif net>60:
    print("DD")
elif net>55:
    print("FD")
else:
    print("FF")

print("\n\n")

"4"

secim=input("1-Dörtgen\n2-Üçgen\nSeçiminizi yapın :")

if secim=="1":
    a=int(input("Birinci  kenar :"))
    b=int(input("İkinci   kenar :"))
    c=int(input("Üçüncü   kenar :"))
    d=int(input("Dördüncü kenar :"))
    if (a==b and a==c and a==d):
        print("Bu bir kare")
    elif (a==c and b==d):
        print("Bu bir dikdörtgen")
    else:
        print("Bu sıradan bir dörtgen")
   
elif secim=="2":
     a=int(input("Birinci  kenar :"))
     b=int(input("İkinci   kenar :"))
     c=int(input("Üçüncü   kenar :"))
     if(a+b <= c or abs(a-b)>=c or a+c <= b or abs(a-c)>=b or b+c <= a or abs(b-c)>=a):
         print("Bu kenarlar bir üçgen oluşturamaz")
     elif (a==b and a==c):
         print("Bu bir eşkenar üçgen")
     elif ((a==c and b!=a) or (a==b and b!=c) or (b==c and b!=a) ):
         print("Bu bir ikizkenar üçgen")
     elif( (a**2 + b**2==c**2) or (a**2 + c**2==b**2) or (c**2 + b**2==a**2) ):
         print("Bu bir dik üçgen")
     else:
         print("Bu sıradan bir üçgen") 
else:
    print("Yanlıs seçim yaptınız!")
    












