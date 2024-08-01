def ekstra(f):
    
    def dön(sayılar):
        çiftler = 0
        çift_toplam = 0
        tekler = 0
        tek_toplam = 0
        
        for x in sayılar:
            
            if(x % 2 == 0):
                çift_toplam += x 
                çiftler += 1
            else:
                tek_toplam += x 
                tekler += 1
        print("Teklerin ortalaması :",tek_toplam/tekler)
        print("Çiftlerin ortalaması :",çift_toplam/çiftler)                                                                                       
        
        f(sayılar)
    return dön

@ekstra
def ortalama(sayılar):
    
    toplam = 0
    
    for x in sayılar:
        toplam += x
    
    print("Ortalama :",toplam/len(sayılar))
    


ortalama([6,8,2,7,90,35,24])






