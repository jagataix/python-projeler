
ogrenci_bilgileri = {}


while True:
    ogrenci_adi = input("Öğrenci adını girin (Çıkmak için 'q' tuşuna basın): ")
    if ogrenci_adi.lower() == 'q':
        break
    
    ogrenci_numarasi = input(f"{ogrenci_adi} adlı öğrencinin numarasını girin: ")
    

    ogrenci_bilgileri[ogrenci_adi] = ogrenci_numarasi


while True:
    sorgulanan_ogrenci = input("Bilgilerini sorgulamak istediğiniz öğrencinin adını girin (Çıkmak için 'q' tuşuna basın): ")
    if sorgulanan_ogrenci.lower() == 'q':
        break
    

    if sorgulanan_ogrenci in ogrenci_bilgileri:
        print(f"{sorgulanan_ogrenci} adlı öğrencinin numarası: {ogrenci_bilgileri[sorgulanan_ogrenci]}")
    else:
        print(f"{sorgulanan_ogrenci} adlı öğrenci bulunamadı.")
