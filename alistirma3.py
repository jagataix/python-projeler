print("""
***********************
      
Hesap Makinesi Programı

İşlemler:

1.Toplama İşlemi 

2.Çıkarma İşlemi    

3.Çarpma İşlemi    

4.Bölme İşlemi
         
***********************      
        
""")

a=int(input("Birinci sayıyı giriniz :"))
b=int(input("İkinci sayıyı giriniz :"))

c=input("İşlemi seçiniz :")

if c=="1":
    print("{} + {} = {}\n\n".format(a,b,a+b))
elif c=="2":
    print("{} - {} = {}\n\n".format(a,b,a-b))
elif c=="3":
    print("{} x {} = {}\n\n".format(a,b,a*b))
elif c=="4":
    print("{} / {} = {}\n\n".format(a,b,a/b))
else:
    print("Yanlış seçim yaptınız!\n\n")
    

print("""
**********************
Kullanıcı Girişi
********************** 
      """)
      
kullanıcı_adı="CAGATAY"
parola="2468"

ad_giris=    input("Kullanıcı Adı :")
parola_giris=input("Parola        :")

if(ad_giris == kullanıcı_adı and parola!=parola_giris):
    print("Parola hatalı!")
elif(ad_giris != kullanıcı_adı and parola==parola_giris):
    print("Kullanıcı adı hatalı!")
elif(ad_giris != kullanıcı_adı and parola!=parola_giris):
    print("Kullanıcı adı ve parola hatalı!")
else:
    print("Sisteme giriş yapıldı")
          
      
      
      
      
      
      
      
      
      
      
      
      
      