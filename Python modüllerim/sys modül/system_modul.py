import sys

def kök_al(x,y,z):
    delta = y ** 2 - 4 * x * z

    if (delta < 0):
       print("Reel Kök Yok")
    else:
        a1 = (-y - delta ** 0.5)/(2 * x)
        a2 = (-y + delta ** 0.5)/(2 * x)

        return (a1,a2)


if len(sys.argv) == 4:
    print("Kökler",kök_al(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler giriniz!")
    sys.stderr.flush()

#terminalden çalıştır