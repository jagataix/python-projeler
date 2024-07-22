"""
Problem 1
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.

Problem 2
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise *return* ile bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon *raise* ile *ValueError* hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""

"1"

liste = ["dlggndo3453","3453","flbgnf","43eg","4","983"]

for x in liste:
    try:
        print(int(x))
    except:
        continue

"2"

def tekmi_ciftmi(x):
    if x % 2 == 0 :
        return x
    else:
        raise ValueError("Bu sayı tektir")
            
a=int(input("Bir sayı giriniz :"))

print(tekmi_ciftmi(a))

