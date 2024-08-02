import sys

x = int(input("x :")) 
y = int(input("y :")) 

#sys.exit()

z = int(input("z :"))

sys.stderr.write("Bu bir hata mesajı\n")

sys.stderr.flush()

sys.stdout.write("Bu normal bir mesaj\n")


print(sys.argv)


