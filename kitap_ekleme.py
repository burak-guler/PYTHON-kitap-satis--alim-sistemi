class kitap():
    def __init__(self,kitap="",yazar="",yil="",fiyat=""):
        self.kitap=input("kitap adı: ")
        self.yazar=input("yazar adı: ")
        self.yil=input("basım yılı: ")
        self.fiyat=input("fiyat: ")
def kitap_sifir():
    sozluk={}
    while True:
        kitap1=kitap()
        liste=[kitap1.yazar,kitap1.yil,kitap1.fiyat]
        sozluk[kitap1.kitap]=liste
        with open("kitap_sifir.txt","a",encoding="utf-8") as file:
            file.write(f"{kitap1.kitap},{kitap1.yazar},{kitap1.yil},{kitap1.fiyat}\n")
        sorgu = input("kitap eklemeye devam edicekmisiniz evet-1 hayır-0\ntuşlayınız:")
        if sorgu == "0":
            break
def kitap_ikinciel():
    sozluk2={}
    while True:
        kitap2=kitap()
        liste2=[kitap2.yazar,kitap2.yil,kitap2.fiyat]
        sozluk2[kitap2.kitap]=liste2
        with open("kitap_ikinciel.txt","a",encoding="utf-8") as dosya:
                dosya.write(f"{kitap2.kitap},{kitap2.yazar},{kitap2.yil},{kitap2.fiyat}\n")
        sorgu2 = input("kitap eklemeye devam edicekmisiniz evet-1 hayır-0\ntuşlayınız:")
        if sorgu2 == "0":
            break


