print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
-----------------------------------------------------------
""")
a = int(input("Birinci Sayı:")) # Birinci Sayıyı Alıyoruz.
b = int(input("İkinci Sayı:")) # İkinci Sayıyı Alıyoruz.

işlem =  input("İşlem Numarasını Giriniz:") # Buna göre koşullarımızı yazacağız.

if (işlem == "1"): # Toplama İşlemi

    print("{} ile {} 'nin toplamı {} dır.".format(a,b,a+b))
elif (işlem == "2"):

    print("{} ile {} 'nin farkı {} dır.".format(a, b, a - b))

elif (işlem == "3"):

    print("{} ile {} 'nin çarpımı {} dır.".format(a, b, a * b))

elif (işlem == "4"):

    print("{} 'nın {} 'e bölümü {} dır.".format(a, b, a / b))
else:

    print("Lütfen geçerli bir işlem giriniz...")