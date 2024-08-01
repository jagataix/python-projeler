"""
Program 1
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.

Program 2
1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.
"""

"1"

class kareler():
    
    def __init__(self,maks):
       
        self.maks = maks
        self.sayı = 1
        
    def __iter__(self):
        
        return self

    def __next__(self):
        self.sayı
        if(self.sayı <= self.maks):
            
            sonuc = self.sayı ** 2
            
            self.sayı += 1
            
            return sonuc
        
        else:
            self.sayı = 1
            raise StopIteration

kare = kareler(4)

iteratorüm = iter(kare)

print(next(iteratorüm))
print(next(iteratorüm))
print(next(iteratorüm))
print(next(iteratorüm))

print("\n\n") 
   
"2"

def asal_bul():
    for x in range(2,1001):
        sonuc = 0
        for y in range(2,x):
            if x % y == 0:
                sonuc = 1
        if sonuc == 0 :
            yield x
            
                
for i in asal_bul():
    print(i)











  

