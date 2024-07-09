
sayi = int(input("Bir sayı girin: "))


if sayi <= 1:
    print(sayi, "bir asal sayı değildir.")
else:
    asal_mi = 1 
    
    for i in range(2, sayi):
        if sayi % i == 0:
            print(sayi, "bir asal sayı değildir.")
            asal_mi = 0
            break  #bak
    if asal_mi:
        print(sayi, "bir asal sayıdır.")
