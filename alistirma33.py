"""
Proje 1
Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın ve bunların nerede bulunduklarını ve isimlerini ayrı ayrı "pdf_dosyalari.txt","mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin.
"""

import os

with open("txt_dosyaları.txt","w",encoding = "utf-8") as dosya:
    
    for x,y,z in os.walk("C:/"):
      for n in z:
        if n.endswith(".txt"):
            
            liste = "Konumu :",x + "-------------------------->Dosya :",n
            dosya.writelines(liste)
            dosya.writelines("\n")
                 
with open("pdf_dosyaları.txt","w",encoding = "utf-8") as dosya:
    
    for x,y,z in os.walk("C:/"):
      for n in z:
        if n.endswith(".pdf"):
            
            liste = "Konumu :",x + "-------------------------->Dosya :",n
            dosya.writelines(liste)
            dosya.writelines("\n")
            
with open("mp4_dosyaları.txt","w",encoding = "utf-8") as dosya:
    
    for x,y,z in os.walk("C:/"):
      for n in z:
        if n.endswith(".mp4"):
            
            liste = "Konumu :",x + "-------------------------->Dosya :",n
            dosya.writelines(liste)
            dosya.writelines("\n")