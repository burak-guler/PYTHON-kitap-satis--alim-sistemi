import kitap_sorgulama as sorgulama
import time
import kitap_satis as satis
import kitap_ekleme as ekle
def kapat():
    print("sistem kapatılıyor")
    for i in range(0,3):
        print(".")
        time.sleep(1)
def giris():
    print("*****Sisteme Giriş*****")
    kullanici_ad="burak guler"
    parola="123456789"
    while True:
        ad=input("kullanıcı adı: ")
        sifre=input("parola: ")
        if kullanici_ad==ad and parola==sifre:
            print("Giriş Başarılı...")
            break
        elif kullanici_ad!=ad and  parola!=sifre:
            print("Kullanıcı adınız ve Parolanız yanlış..")
        elif kullanici_ad!=ad:
            print("! Kullanıcı adınız yanlış..")
        elif parola!=sifre:
            print("! Parolanız yanlış..")
def menu():
    print("""       *****MENÜ*****
    1-Kitap sorgulama işlemi
    2-kitap satış işlemi
    3-sisteme kitap ekleme işlemi
    4-sistemi kapat
    """)
    sorgu=int(input("işlem numarasını giriniz: "))
    return sorgu
giris()
while True:
    sorgu=menu()
    if sorgu==1:
        print("""
        1-yazar adı ile sorgulama
        2-kitap adı ile sorgulama
        """)
        secim=int(input("sorgulama türünü seçmek için numara giriniz: "))
        if secim==1:
            yazar_ad=input("sorgulanacak yazar adı: ")
            sorgulama.yazar_ikinciel(yazar_ad)
            sorgulama.yazar_sifir(yazar_ad)
        elif secim==2:
            kitap_ad=input("sorgulanacak kitap adı: ")
            sorgulama.kitap_sifir(kitap_ad)
            sorgulama.kitap_ikinciel(kitap_ad)
        print("""
        sistemi kapatmak için-0
        menüye gitmek için-1  
        """)
        secim1=int(input("tuşlayınız: "))
        if secim1==0:
            kapat()
            break
    elif sorgu==2:
        print("""
        sıfır kitap-1
        ikinci el kitap-2
        """)
        secim2=input("hangi türden kitap alacaksınız tuşlayınız: ")
        if secim2=="1":
            satis.sifir()
        elif secim2=="2":
            satis.ikinciel()
        print("""
        sistemi kapatmak için-0
        menüye gitmek için-1  
        """)
        secim1 = int(input("tuşlayınız: "))
        if secim1 == 0:
            kapat()
            break
    elif sorgu==3:
        print("""
                sıfır kitap ekleme-1
                ikinci el kitap ekleme-2
                """)
        secim3 = input("hangi türden kitap alacaksınız tuşlayınız: ")
        if secim3 == "1":
            ekle.kitap_sifir()
        elif secim3 == "2":
            ekle.kitap_ikinciel()
        print("""
        sistemi kapatmak için-0
        menüye gitmek için-1  
        """)
        secim1 = int(input("tuşlayınız: "))
        if secim1 == 0:
            kapat()
            break
    elif sorgu==4:
        kapat()
        break
