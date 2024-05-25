#Frekans hesaplama algoritmasi Yol1
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}

for i in items:
    if( i in frequency):
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)

#Frekans hesaplama algoritmasi Yol2
metin = "hello world"

frequency = {}

for i in metin:
    if ( i in frequency):
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)

#2 Sozlukteki Ortak Anahtarlari Bulup Baska Bir Sozluge Atma

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 3, "c": 4, "d": 5}
d3 = {}


for k1 in d1.keys():
    for k2 in d2.keys():
        if ( k1 == k2):
            d3[k1] = (d1[k1] ,d2[k2] )
print(d3)



#Sozlukteki Degerlerin Toplamini Bulma

d = {"a": 10, "b": 20, "c": 30}
toplam = 0

for v in d.values():
    toplam+=v
print("Degerlerin toplami = %d " % (toplam))


#Ogrencilerin Gecti Kaldi Durumunu Belirleme ( Gecme Notu 50'dir.)

ogrenciler = {
    "Ali": 45,
    "Ayşe": 76,
    "Fatma": 50,
    "Mehmet": 39
}

sonuc = {}
for k,v in ogrenciler.items():
    if ( v >= 50):
        sonuc[k] = "Gecti"
    else:
        sonuc[k] = "Kaldi"
print(sonuc)


#Sozlukteki Degerlerin Karelerini Hesaplama

sayilar = {"a": 2, "b": 3, "c": 4}
yeniSozluk = {}

for k,v in sayilar.items():
    yeniSozluk[k] = v*v

print(f"Yeni sozluk = {yeniSozluk}")


#Sozlukteki Degerleri Ters Cevirme

kelimeler = {"kelime1": "hello", "kelime2": "world", "kelime3": "python"}
tersCevirme = {}

for k,v in kelimeler.items():
    tersCevirme[k] = v[::-1]
print(tersCevirme)





# Değerleri 5 artırran uygulama

notlar = {"Emir": 90, "Veli": 85, "Asli": 70}
artirilmis_notlar = {}

for k,v in notlar.items():
    artirilmis_notlar[k] = v + 5
print(artirilmis_notlar)




