import math
sayi = int(input("Bir sayı girin: "))


if sayi > 20:
    print("Girdiğiniz sayı 20'den büyük.")
    for i in range(sayi):
        if i <= 20:
            print("Karekök:", i ** 2)
        else:
            print("Karekök:", math.sqrt(i))
elif sayi < 10:
    print("Girdiğiniz sayı 10'dan küçük.")
    i = 0
    while i <= sayi:
        print("Karesi:", i ** 2)
        i += 1
else:
    print("Girdiğiniz sayı 10 ile 20 arasında.")
    for i in range(sayi + 1):
        print("Karesi:", i ** 2)
