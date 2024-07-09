
not_degeri = float(input("Notu girin: "))

if not_degeri >= 90:
    harf_notu = "A"
elif not_degeri >= 80:
    harf_notu = "B"
elif not_degeri >= 70:
    harf_notu = "C"
elif not_degeri >= 60:
    harf_notu = "D"
else:
    harf_notu = "F"


print("Harf notu:", harf_notu)
