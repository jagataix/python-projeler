print("""
*************************
Kullanıcı Girişi Programı
*************************      
      """)
      
kullanıcı_adı="CAGATAY"

parola ="123456"

giris_hakkı=0

while True:
    giris_ad=input("Kullanıcı adı :")
    giris_parola=input("Şifre :")
    if(kullanıcı_adı == giris_ad and parola != giris_parola):
        print("Parola hatalı!")
    elif(kullanıcı_adı != giris_ad and parola == giris_parola):
        print("Kullanıcı adı hatalı!")
    elif(kullanıcı_adı != giris_ad and parola != giris_parola):
        print("Kullanıcı adı ve parola hatalı!")
    else:
        print("Sisteme giriş yapıldı.")
        break
    giris_hakkı+=1
    if(giris_hakkı==3):
        print("Çok fazla hatalı işlem yaptınız sonra bir daha deneyiniz.")
        break
    
print("\n\n")

print("""
**************************
ATM MAKİNESİNE HOŞGELDİNİZ
**************************
İşlemeler:
    1.Bakiye Sorgulama
    
    2.Para Yatırma
    
    3.Para Çekma
    
Programdan çıkmak icin 'q' tuşuna basınız.
      """)
     
bakiye=0

while True:
    secim=input("İşleminizi seçiniz :")
    if secim=="1":
        print("Bakiyeniz :",bakiye)
    elif secim=="2":
        print("Bakiyeniz :",bakiye)
        para=int(input("Yatırmak istediğiniz miktarı giriniz :"))
        bakiye+=para
        print("Para hesaba yatırıldı.")
        print("Bakiyeniz :",bakiye)
    elif secim=="3":
        if(bakiye==0):
             print("Bakiyeniz boş para çekemezsiniz.")
        else:
             print("Bakiyeniz :",bakiye)
             para=int(input("Çekmek istediğiniz miktarı giriniz :"))
             if(para>bakiye):
                 print("Bakiyeniz bu miktar için yetersiz.")
             else:
                 bakiye-=para
                 print("Para hesaptan çekildi.")
                 print("Bakiyeniz :",bakiye)
    elif secim=="q":
        print("İyi Günler...")
        break
    else:
        print("Hatalı işlem girişi!Tekrar deneyiniz.")

print("\n\n")
while True:
    
   sayi=input("Faktoriyelini alacağınız sayıyı giriniz :")

   if sayi=="q":
    print("Çıkış yapıldı")
    break
   else:
    
    sayi=int(sayi)
    
    faktoriyel=1

    for x in range(1,sayi+1):
        faktoriyel*=x
    
    print("{}! = {}".format(sayi,faktoriyel))

    print("\n")


print("\n\n")

ilk=1
ikinci=1



sayi=int(input("Dizini kaç elemanı yazılsın? :"))

print(ilk)
print(ikinci)

for x in range(1,sayi-1):
    ucuncu=ilk+ikinci
    print(ucuncu)
    ilk=ikinci
    ikinci=ucuncu
    
    
a=1
b=1

fibonacci =[a,b]

for x in range(20):
    
    a,b=b,a+b
   
    fibonacci.append(b)

print(fibonacci)




     