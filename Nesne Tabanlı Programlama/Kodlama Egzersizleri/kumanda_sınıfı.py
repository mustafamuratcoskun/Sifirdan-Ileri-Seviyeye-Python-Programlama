import time
import random
print("""
televizyonda yaptığınız değişikliklerin kayıt olması için aynı işlem sayısını tekrar giriniz.
TELEVİZYON KAPALIYKEN YAPILAN İŞLEMLERDE TELEVİZYON OTOMATİK OLARAK AÇILIR
DİKKAT SAYI GİRİN YERİNE SADECE İŞLEM SIRALARINDAKİ SAYILARI GİRİN AKSİ TAKDİRDE UYGULAMA SONA ERER
""")
print("""
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısı Görme
6. Rastgele Kanal Açma
7. Televizyon Bilgileri
Çıkmak için 'q' ya basın.
""")

class kumanda():
    def __init__(self,tv_durum = "kapalı",tv_ses = 0,kanal_listesi = ["trt"],kanal = "trt",r_kanal=""):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
        self.r_kanal=r_kanal
    def tv_ac(self):
        if self.tv_durum=="açık":
            print("televizyon zaten açık...")
        else:
            print("televizyon açılıyor...")
            time.sleep(0.2)
            print("televizyon açıldı")
            self.tv_durum="açık"
    def tv_kapat(self):
        if self.tv_durum=="kapalı":
            print("televizyon zaten kapalı...")
        else:
            print("televizyon kapandı")
            self.tv_durum="kapalı"
    def ses_ayarları(self):
        while True:
            cevap=input("ses arttırmak için '>'\nses azaltmak için '<'düğmelerine basın\n (çıkış için herhangibir tuşa basınız): ")
            if cevap=="<":
                if self.tv_ses!=0:
                    self.tv_ses-=1
                    print("Ses:", self.tv_ses)
            elif cevap==">":
                if self.tv_ses!=30:
                    self.tv_ses+=1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses Güncelleniyor...")
                time.sleep(0.2)
                print("Ses Güncellendi.",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ekle):
        self.kanal_listesi.append(kanal_ekle)
        self.kanal=self.kanal_listesi
    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.r_kanal = self.kanal_listesi[rastgele]
        print("Şu anki Kanal:", self.r_kanal)

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "durum: {}\nses: {}\neklenen kanal sayısı: {}\nkanallar: {}".format(kumanda1.tv_durum,kumanda1.tv_ses,len(kumanda1),kumanda1.kanal)

    def tv_bilgiler(self):
        print(kumanda1)
kumanda1=kumanda()

while True:
    cevap=input("sayı girin: ")
    if cevap=="1":
        kumanda1.tv_ac()
    elif cevap=="2":
        kumanda1.tv_kapat()
    elif cevap=="3":
        kumanda1.ses_ayarları()
    elif cevap=="4":
        kumanda1.kanal_ekle(kanal_ekle=input("eklemek istediğiniz kanal adını giriniz: "))

        print("kanal ekleniyor..")
        time.sleep(0.2)
        print("kanal eklendi..")
    elif cevap=="5":
        print("kanal sayısı: ",len(kumanda1))
    elif cevap == "6":
        kumanda1.rastgele_kanal()
    elif cevap=="7":
        kumanda1.tv_bilgiler()
    elif cevap=="q" or cevap=="Q":
        print("çıkış yapılıyor: ")
        break

    else:
        print("Geçersiz İşlem......")
