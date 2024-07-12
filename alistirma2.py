"""
Programlama Ödevi - Temel Python Objeleri ve Veri Yapıları
Tebrikler! Bölümü başarıyla bitirdiniz. Şimdi, öğrendiklerinizin akılda kalması için ödevinizi yapma zamanı!

Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.

Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

Problem 4
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

Problem 5
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

Problem 6
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""


"1"

a=int(input("Birinci sayi : "))
b=int(input("İkinci sayi  : "))
c=int(input("Üçüncü sayi  : ")) 
print("{} * {} * {} = {}\n\n".format(a,b,c,a*b*c))

"2"

boy=float(input("Boyu giriniz  : "))
kilo=int(input("Kiloyu giriniz :"))
endeks=kilo /(boy ** 2)
print("Beden kitle endeksi :",endeks,"\n\n")

"3"

yakit=float(input("Arac km başına kaç tl yakar? :"))
km=int(input("Kac km yol yaptı :"))
print("Toplamda {} TL ödeme yapmanız gerekiyor.\n\n".format(km*yakit))

"4"

ad=input   ("Adınızı giriniz    : ")
soyad=input("Soyadınızı giriniz : ")
no=input   ("Numaranızı giriniz : ")
print("{}\n{}\n{}\n\n".format(ad,soyad,no))

"5"

x=input("x : ")
y=input("y : ")

print("x : {} y : {}\n".format(x,y))
x,y=y,x

print("x : {} y : {}\n".format(x,y))

"6"

kenar1=float(input("Birinci kenarın uzunluğunu giriniz :"))
kenar2=float(input("İkinci kenarın uzunluğunu giriniz  :"))

print("Hipotenüsün uzunluğu : {}\n\n".format((kenar1**2+kenar2**2) ** 0.5))


