sayi1 = float(input("1 ci sayıyı ver"))
sayi2 =float (input("ikinci sayıyı ver"))
islem = input("İŞLEMİ GİR HEMEN!!!!")
print("Hala girmedinmi GİR ARTIKK")
if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 + sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem =="/":
    if sayi2 == 0:
       sonuc = "sıfıra bölünmez"
    else:
       sonuc = sayi1 / sayi2
else:
    sonuc = "geçersiz terim"
print("sonuc",sonuc)