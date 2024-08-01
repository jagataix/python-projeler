"""
Program
1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.                                       
"""

def mukemmel(f):
    
    def dön(sayılar):
        
        mükemmel = []
        
        for x in sayılar:
            toplam = 0
            for y in range(1,x):
                if (x % y == 0):
                    toplam += y
                    
            
            if toplam == x:
                mükemmel.append(x)
                
        
        print("Mükemmel sayılar : ",mükemmel)
        f(sayılar)
    return dön
                                                                                           

@mukemmel
def asalmı(sayılar):
    
    
    
    for x in sayılar:
        sonuc = 0
        
        for y in range(2,x):
            if (x % y == 0):
                sonuc = 1
                break
        if sonuc == 0:
            print(x)
        
                
asalmı(range(2,1001))

