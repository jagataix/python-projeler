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


sinir = int(input("hangi degere kadar kontrol edelim :"))

print("Asal sayılar:")
sayi = 2
while sayi <= sinir:
    if asal_mi(sayi):
        print(sayi)
    sayi += 1


