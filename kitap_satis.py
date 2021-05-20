def sifir():
    with open("kitap_sifir.txt","r+",encoding="utf-8") as file:
        print("         *****Sıfır Kitaplar*****")
        sayac1=1
        fiyat=[]
        toplam=0
        for i in file:
            liste1=i.split(",")
            fiyat.append(int(liste1[3]))
            print(f"""
            *{sayac1}.no kitap*
            kitap adı: {liste1[0]}
            yazar adı: {liste1[1]}
            basım yılı: {liste1[2]}
            fiyat: {liste1[3]}
            """,end="")
            sayac1+=1
        sorgu1=int(input("kitap almak için-1 çıkmak için-0\ntuşlayınız: "))
        if sorgu1==1:
            while True:
                secim=int(input("almak istediginiz kitap no: "))
                toplam+=fiyat[(secim-1)]
                sorgu2=input("almaya devam etmek için-1 çıkmak için-0 tuşlayınız:")
                if sorgu2=="0":
                    break
        print("toplam tutar: ",toplam,"tl")

def ikinciel():
    with open("kitap_ikinciel.txt","r+",encoding="utf-8") as dosya:
        print("         *****İkinci El Kitaplar*****")
        sayac2=1
        fiyat2=[]
        toplam2=0
        for j in dosya:
            liste2=j.split(",")
            fiyat2.append(int(liste2[3]))
            print(f"""
            *{sayac2}.no kitap*
            kitap adı: {liste2[0]}
            yazar adı: {liste2[1]}
            basım yılı: {liste2[2]}
            fiyat: {liste2[3]}
            """, end="")
            sayac2+=1
        sorgu1 = int(input("kitap almak için-1 çıkmak için-0\ntuşlayınız: "))
        if sorgu1 == 1:
            while True:
                secim = int(input("almak istediginiz kitap no: "))
                toplam2+=fiyat2[(secim-1)]
                sorgu2=input("almaya devam etmek için-1 çıkmak için-0 tuşlayınız:")
                if sorgu2 == "0":
                    break
        print("toplam tutar: ", toplam2, "tl")