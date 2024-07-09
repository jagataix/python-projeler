import math


sayi = int(input("Bir sayı gir:"))


if sayi > 20:
    for i in range(sayi):
        if i <= 20:
            print(i ** 2)
        else:
            print(math.sqrt(i))
else:
    for i in range(sayi + 1):
        print("i ** 2:",i ** 2)
