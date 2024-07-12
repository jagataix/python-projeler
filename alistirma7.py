
def asal_kontrol(x):
    if x==1:
        return False
    if x==2:
        return True
    
    for i in range(2,x):
        if x % i == 0:
            return False
        
    return True
    

sayi=int(input("Sayi giriniz :"))

if asal_kontrol(sayi):
    print(sayi,"asal bir sayidir.")
else:
    print(sayi,"asal bir sayi değildir.")
    
print("\n\n")

def tam_bolen(sayi):
    bolenler=[]
    for x in range(1,sayi+1):
    
        if sayi % x == 0:
           bolenler.append(x)
    
    return bolenler


sayim=int(input("Bir sayi giriniz :"))

liste=tam_bolen(sayim)

print(liste)



