def asal_mi(sayi):
    if sayi <= 1:
        return False
    elif sayi <= 3:
        return True
    elif sayi % 2 == 0 or sayi % 3 == 0:
        return False
    i = 5
    while i * i <= sayi:
        if sayi % i == 0 or sayi % (i + 2) == 0:
            return False
        i += 6
    return True


sayi = int(input("Bir sayı gir: "))

if asal_mi(sayi):
    print(sayi, " asal sayıdır.")
else:
    print(sayi, " asal sayı değildir.")

