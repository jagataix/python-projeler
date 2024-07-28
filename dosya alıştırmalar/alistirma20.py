class dosyam():
    
   def __init__(self):
       
       with open("paragraf.txt","r",encoding = "utf-8") as dosya:
           
           yazi = dosya.read()
           
           kelimeler =yazi.split()
           
           self.salt_kelimeler = list()
           
           for x in kelimeler:
               x = x.strip("\n")
               x = x.strip(" ")
               x = x.strip(".")
               x = x.strip(",")
               x = x.strip(":")
               x = x.strip("”")
               x = x.strip("“")
               x = x.strip("…")
               
               self.salt_kelimeler.append(x)
               
   def tüm_kelimeler(self):
       küme=set()
       
       for x in self.salt_kelimeler:
           küme.add(x)
       
       print("Tüm kelimeler :")
       print("----------")
       for x in küme:
           print(x)
           print("----------")
           
   def kelime_say(self):
       sözlük = dict()
       
       for x in self.salt_kelimeler:
           if(x in sözlük):
               sözlük[x] +=1
           else:
               sözlük[x] = 1
       for kelime,tekrar in sözlük.items():
           print("{} kelimesi {} kere geçiyor.".format(kelime,tekrar))
           print("----------------")
                 
dosyacım =dosyam() 

dosyacım.tüm_kelimeler()

dosyacım.kelime_say()