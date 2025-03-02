sayi=int(input("sayı:"))
asal_mi=True

if sayi > 1:
    for i in range (2,sayi):
        if (sayi %i==0):
         asal_mi=False
        break
    else :
       asal_mi=False
if asal_mi:
    print(f"{sayi} bir asal sayıdır.") 
else:
    print(f"{sayi} bir asal sayı değildir.")


