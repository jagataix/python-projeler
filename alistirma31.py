class Kuvvet():
    
    def __init__(self,maks = 0):
       
        self.maks = maks
        self.kuvvet = 0
        
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        if(self.kuvvet <= self.maks):
            
            sonuc = 3 ** self.kuvvet
            
            self.kuvvet += 1
            
            return sonuc
        
        else:
            self.kuvvet = 0
            raise StopIteration
        
kuvvet = Kuvvet(7)

iteratorüm = iter(kuvvet)

for x in kuvvet:
    print(x)

for x in kuvvet:
    print(x)
 
print("\n\n\n")

def fibonacci():
    a = 1
    b = 1
    yield a
    yield b
    
    while True:
        
       a,b = b,a+b
       
       yield b
       
for x in fibonacci():
    
    if(x > 100000):
        break
    print(x)
    