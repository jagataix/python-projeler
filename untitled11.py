
yas = int(input("Yaşınızı girin: "))


if yas < 0:
    print("Lütfen geçerli bir yaş girin.")
    
    
    
    
    
elif yas < 18:
    print("gençsiniz.")
    if yas < 12:
        print("Ve aynı zamanda çocuksunuz.")
    elif yas < 15:
        print("ergensiniz.")
    else:
        print("Ve ergenlik döneminizi yaşıyorsunuz.")
elif yas < 65:
    print("yetişkin bir bireysiniz.")
    if yas < 25:
        print("genç yetişkin ")
    else:
        print("çalışma çağında olduğunuz için yetişkin bir bireysiniz.")
else:
    print("emeklisiniz.")
    if yas < 75:
        print("emeklilik döneminizin başlarında olduğunuz için aktifsiniz.")
    else:
        print("edinlenmeye başlamış olabilirsiniz.")
