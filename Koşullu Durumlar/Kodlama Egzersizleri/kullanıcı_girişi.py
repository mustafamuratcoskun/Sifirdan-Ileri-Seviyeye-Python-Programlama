print("**********\nKullanıcı Girişi\n**********\n")

# Kullanıcı Adı Girişi örneğinin gerçek versiyonunu PyQT5 derslerinde bulabilirsiniz.

sys_kul_adı = "mmurat" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Kullanıcı Adı

sys_parola  = "12345" # Sistemde Kayıtlı Olduğunu Düşündüğümüz Parola

kullanıcı_adı = input("Kullanıcı Adını Giriniz:") # Kullanıcı Adını input ile alıyoruz.

parola =  input("Parolanızı Giriniz:")

if (kullanıcı_adı != sys_kul_adı and parola == sys_parola):
    print("Kullanıcı Adı Hatalı...")
elif (kullanıcı_adı == sys_kul_adı and parola != sys_parola):
    print("Parola Hatalı...")

elif (kullanıcı_adı != sys_kul_adı and parola != sys_parola):
    print("Kullanıcı Adı ve Parola Hatalı...")

else:
    print("Başarıyla Giriş Yaptınız...")

