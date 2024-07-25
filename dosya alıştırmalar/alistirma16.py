

def not_hesapla(x):
    x = x[:-1]
    
    ayir = x.split(",")
    
    
    
    ad = ayir[0]
    not1 = int(ayir[1])
    not2 = int(ayir[2])
    not3 = int(ayir[3])
    
    ortalama = not1 * 0.3 + not2 * 0.3 + not3 * 0.4
    
    if ortalama >= 90:
        harf="AA"
    elif ortalama >= 85:
        harf="BA"
    elif ortalama >= 80:
        harf="BB"
    elif ortalama >= 75:
        harf="CB"
    elif ortalama >= 70:
        harf="CC"
    elif ortalama >= 65:
        harf="DC"
    elif ortalama >= 60:
        harf="DD"
    elif ortalama >= 55:
        harf="FD"
    else:
        harf="FF"
    
    return ad + " --------> " + harf + "\n"


with open(r"C:\Users\cagat\OneDrive\Desktop\python projeleri\alıştırmalar\alistirma16\metin.txt","r",encoding = "utf-8") as dosya:

    listem = []
    
    for x in dosya:
        listem.append(not_hesapla(x))

print(listem) 

with open(r"C:\Users\cagat\OneDrive\Desktop\python projeleri\alıştırmalar\alistirma16\notlar.txt","w",encoding="utf-8") as dosya:
   
    for x in listem:
        dosya.write(x)




                                                                                                                                    