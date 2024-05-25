
#update() Kullanimi.

ogrenciler = {}


adet = int(input("Kac adet ogrencinin bilgisini gireceksiniz? : "))

for i in range(adet):
    no = int(input("Ogrencinin numarasini giriniz: "))
    ad =  input("Ogrencinin adini giriniz: ")
    soyad = input("Ogrencinin soyadini giriniz: ")
    telNo= int(input("Ogrencinin telefon numarasini giriniz: "))
    ogrenciler.update({
        no: {
            "ad" : ad,
            "soyad" : soyad,
            "telNo" : telNo
        }
    })
print(ogrenciler)



notlar = {"Ayse" : 100, "Ali": 50, "Veli" : 75}

notlar.update({"Kemal" : 54})
print(notlar)



    





