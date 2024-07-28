"""
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

*İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık.*
"""


cümle = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

sözlük = dict()

for x in cümle:
    if(x in sözlük):
        sözlük[x] += 1
    else:
        sözlük[x] = 1
    
for x,y in sözlük.items():
    print("{} harfi {} defa kullanılmıştır.".format(x,y))
