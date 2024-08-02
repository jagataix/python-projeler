from datetime import *

import locale

locale.setlocale(locale.LC_ALL,"")

şuan = datetime.now()

print(şuan.year)
print(şuan.month)
print(şuan.microsecond)
print(şuan.hour)

print(datetime.ctime(şuan))

print(datetime.strftime(şuan,"%Y"))
print(datetime.strftime(şuan,"%B"))
print(datetime.strftime(şuan,"%D"))
print(datetime.strftime(şuan,"%D %B"))
print(datetime.strftime(şuan,"%A %B %Y"))

şimdi = datetime.now()


saniye = datetime.timestamp(şimdi)

print(saniye)

şimdi2 = datetime.fromtimestamp(saniye)

print(şimdi2)

şimdi3 = datetime.fromtimestamp(0)

print(şimdi3)

tarih = datetime(2019,11,5)

şimdi4 = datetime.now()

print(şimdi4 - tarih)
