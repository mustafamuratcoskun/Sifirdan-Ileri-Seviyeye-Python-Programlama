import random
import time

print("""************************

Sayı Tahmin Oyunu


1 ile 1000 arasında sayıyı tahmin edin.

************************""")

rastgele_sayı = random.randint(1,1000)
tahmin_hakkı = 10
while True:

    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin....")

        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin....")

        tahmin_hakkı -= 1
    else:
        print("Bilgiler Sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler! Sayımız",rastgele_sayı)
        break
    if (tahmin_hakkı == 0):
        print("Tahmin Hakkınız Bitti...")
        print("Sayımız:",rastgele_sayı)
        break




















