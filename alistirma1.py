print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takım = input("Oyuncunun Takımı:")

bilgiler=[ad,soyad,takım]

print("Bilgiler Kaydediliyor...")

print("Oyuncunun Adı: {}\nOyuncunun Soyadı: {}\nOyuncunun Takımı: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler kaydedildi..\n\n")

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta= b ** 2 - 4 * a * c 

x1= (-b - delta ** 0.5) / (2*a)
x2= (-b + delta ** 0.5) / (2*a)

print("Birinci kök :",x1)
print("İkinci kök :",x2)

 
