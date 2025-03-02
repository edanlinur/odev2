def hesap_makinesi():
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    islem = input("İşlem türünü girin (+, -, *, /): ")

    if (islem=="+"):
        print("Çıktı: "+str(sayi1+sayi2))
    elif (islem=="-"):
        print("Çıktı: "+str(sayi1-sayi2))
    elif (islem=="/"):
        if sayi2==0:
         print("Bölme işlemi için ikinci sayı 0 olamaz.")
        else:
         print("Çıktı: "+str(sayi1/sayi2))
    elif (islem=="*"):
     print("Çıktı: "+str(sayi1*sayi2))
    else:
         print("Çıktı: Geçersiz işlem türü!")        
hesap_makinesi()