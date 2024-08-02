import os

from datetime import *

os.chdir(r"C:/Users\cagat\OneDrive\Desktop\python projeleri\alıştırmalar\Python modüllerim")

print(os.getcwd())

for x in os.listdir():
    print(x)

#os.mkdir("Klasörüm1")

#os.makedirs("Klasörüm2/Klasörüm3")

#os.rmdir("Klasörüm2/Klasörüm3")

#os.removedirs("Klasörüm2/Klasörüm3")

#os.rename("test.txt","test2.txt")

#print(os.stat("test2.txt"))

print("Dosyanın değiştirilme zamanı",datetime.fromtimestamp(os.stat("test2.txt").st_mtime))


for x,y,z in os.walk("C:/Users\cagat\OneDrive\Desktop"):
    print("Klasör Yolu :",x)
    print("Klasör İsmi :",y)
    print("Dosya İsmi  :",z)
    print("-------------------------------")
    
for x,y,z in os.walk("C:/Users\cagat\OneDrive\Desktop"):
    for n in z:
        print(n)
print("-------------------------------")        
for x,y,z in os.walk("C:/Users\cagat\OneDrive\Desktop"):
    for n in z:
        if n.endswith(".txt"):
            print(n)
print("-------------------------------")
