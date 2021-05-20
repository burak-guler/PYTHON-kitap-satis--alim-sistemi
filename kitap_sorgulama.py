def yazar_sifir(x):
    with open("kitap_sifir.txt","r+",encoding="utf-8") as file:
        sayac=0
        print("***Sıfır Kitaptan yazar sorgulama***")
        for i in  file:
            liste1 = i.split(",")
            if liste1[1]==x:
                sayac+=1
                print(f"kitap adı: {liste1[0]} - yazar: {liste1[1]} - basım yılı: {liste1[2]} - fiyat: {liste1[3]}tl\n")
        if sayac==0:
            print("!Böyle bir sonuç bulunamadı...\n")
def yazar_ikinciel(y):
    with open("kitap_ikinciel.txt","r+",encoding="utf-8") as file2:
        sayac = 0
        print("***İkinci El Kitaptan yazar sorgulama***")
        for j in file2:
            liste2=j.split(",")
            if liste2[1]==y:
                sayac += 1
                print(f"kitap adı: {liste2[0]} - yazar: {liste2[1]} - basım yılı: {liste2[2]} - fiyat: {liste2[3]}tl\n")
        if sayac==0:
            print("!Böyle bir sonuç bulunamadı...\n")
def kitap_sifir(z):
    with open("kitap_sifir.txt","r+",encoding="utf-8") as f:
        sayac = 0
        print("***Sıfır Kitap sorgulama***")
        for k in f:
            book=k.split(",")
            if book[0]==z:
                sayac += 1
                print(f"kitap adı: {book[0]} - yazar: {book[1]} - basım yılı: {book[2]} - fiyat: {book[3]}tl")
        if sayac==0:
            print("!Böyle bir sonuç bulunamadı...")
def kitap_ikinciel(w):
    with open("kitap_ikinciel.txt","r+",encoding="utf-8") as dosya:
        sayac = 0
        print("***İkinci El Kitap sorgulama***")
        for l in dosya:
            book2=l.split(",")
            if book2[0]==w:
                sayac += 1
                print(f"kitap adı: {book2[0]} - yazar: {book2[1]} - basım yılı: {book2[2]} - fiyat: {book2[3]}tl")
        if sayac==0:
            print("!Böyle bir sonuç bulunamadı...\n")



