print("**********\nKullanıcı Girişi\n**********\n")

# Kullanıcı Adı Girişi örneğinin gerçek versiyonunu PyQT5 derslerinde bulabilirsiniz.

sys_kul_adı = "mmurat" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Kullanıcı Adı

sys_parola  = "12345" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Parola

giriş_hakkı = 3
while True: # Kullanıcı Doğru Giriş Yaptığında ve Giriş Hakkı bittiğinde sona erecek.
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if (kullanıcı_adı != sys_kul_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ", giriş_hakkı)
    elif (kullanıcı_adı == sys_kul_adı and parola != sys_parola):
        print("Parola Hatalı...")
        giriş_hakkı -= 1

        print("Giriş Hakkı: ", giriş_hakkı)
    elif (kullanıcı_adı != sys_kul_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ", giriş_hakkı)

    else:
        print("Başarıyla Giriş Yaptınız...")
        break
    if (giriş_hakkı == 0 ):

        print("Giriş Hakkınız Bitti...")
        break




