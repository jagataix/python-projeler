"""
Programlama Ödevi - Döngüler
Tebrikler! Bölümü başarıyla bitirdiniz. Şimdi, öğrendiklerinizin akılda kalması için ödevinizi yapma zamanı!

*Not: Buradaki tüm problemler sizin algoritma yeteneğinizi oldukça geliştirecektir. O yüzden zorlandığınız noktalarda pes etmeyin. Üzerine kafa yormaya ve sürekli denemeye çalışın.*

Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

*İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.*

Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.*

Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi *continue* ile yapmaya çalışın.

Problem 6
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

İpucu: Basit düşünmeye çalışın.
"""

"1"

toplam=0



sayi=int(input("Bir sayi giriniz :"))

for x in range(1,sayi):
    if sayi % x == 0:
        toplam+=x

if(toplam == sayi):
    print("{} mükemmel bir sayıdır.".format(sayi))
else:
    print("{} mükemmel bir sayı değildir.".format(sayi))
    

"2"

basamak=0

toplam=0


sayi2=int(input("Bir sayı giriniz :"))

sayim=sayi2
sayim2=sayim
while (sayi2 != 0):
     sayi2 = sayi2/10-(sayi2%10)/10
     
     basamak += 1
    
print(basamak)


for x in range(1,basamak+1):
    toplam += (sayim % 10)**basamak
    
    sayim = sayim/10-(sayim%10)/10
    
print(toplam)

if(toplam == sayim2):
    print("{} bir Armstrong sayısıdır".format(sayim2))
else:
    print("{} bir Armstrong sayısı değildir".format(sayim2))
    
print("\n\n")
    
"3"

for x in range(1,11):
        print("**************")
        for y in range(1,11):
       
          print("{} X {} = {}".format(x,y,x*y))
        


print("\n\n")

"4"

topla=0

while True:
    sayi=input("Sayı gir :")
    if sayi=="q":
        break
    else:
       sayi=int(sayi)
       topla +=sayi

print("Toplam :",topla)

print("\n\n")

"5"

for x in range(1,101):
    if(x % 3 != 0):
        continue
    print(x)
 
print("\n\n")


"6"

listemxd=list()

listemxd=[x for x in range(1,101) if(x%2==0)]

print(listemxd)

































