"""
Proje 2
"futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin. Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //
"""

with open("futbolcular.txt","r",encoding="utf-8") as dosya:
    liste = dosya.readlines()
    
  

with open("Galatasaray.txt","w",encoding="utf-8") as dosya2:

    for x in liste:
        ayirma = x.split(",")
       
        if(ayirma[1] == "Galatasaray\n"):
            dosya2.writelines(ayirma[0]+"\n")

with open("Fenerbahçe.txt","w",encoding="utf-8") as dosya2:

    for x in liste:
        ayirma = x.split(",")
       
        if(ayirma[1] == "Fenerbahçe\n"):
            dosya2.writelines(ayirma[0]+"\n")

with open("Beşiktaş.txt","w",encoding="utf-8") as dosya2:

    for x in liste:
        ayirma = x.split(",")
       
        if(ayirma[1] == "Beşiktaş\n"):
            dosya2.writelines(ayirma[0]+"\n")
                                                                                                                                                                                                                                                                                      