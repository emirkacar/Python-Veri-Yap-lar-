#Liste,sözlük ve seti birlikte kullanan kavratıcı bir örnek
liste = [1, 2, 3, 4, 4, 5, 6, 6] #Liste
tekrarsiz = set() #Set
birKereTekrarEden = {} #Sözlük
for i in liste:
    if ( i not in birKereTekrarEden ):
        birKereTekrarEden[i]=1
    else :
        birKereTekrarEden[i]+=1
for k,v in birKereTekrarEden.items():
    if ( v == 1):
        tekrarsiz.add(k)
print(tekrarsiz)


#Union kullanimi.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set()

for i in set1:
    set3 = set1.union(set2)
print(set3)



 #2 kumedeki ortak elemanlari baska bir sete atma (1.Yol)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set()

for i in set1:
    if ( i in set2):
        set3.add(i)
print(set3)



 #2 kumedeki ortak elemanlari baska bir sete atma (2.Yol)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2)
print(set3)


#Kume farki (difference) (1.Yol)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set()

for i in set1:
    if ( i not in set2):
        set3.add(i)
print(set3)

#Kume farki (difference) (2.Yol)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.copy()
cikartilanElemenlar = set()
for i in set3:
    if (i in set2 ):
        cikartilanElemenlar.add(i)
print("Ortak elemanlar : " , cikartilanElemenlar)

for i in set1:
    if(i in cikartilanElemenlar):
        set3.remove(i)
print("Set3 'un son hali : ",set3)




#Setteki her elemani 3 kere alan ve tekrarlistesine atan algoritma
setim = {1, 2, 3}
tekrarSayisi = 3
tekrarListesi= []


for i in setim:
    for j in range(tekrarSayisi):
        tekrarListesi.append(i)

print("Tekrarlanan liste = ",tekrarListesi)


#Kumedeki asal sayilari ve asal olmayan sayilari bulan algoritma

kume = {2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
asalOlmayanlar = set()
asalOlanlar = set()

for i in kume:
    if(i <= 2):
        asalOlmayanlar.add(i)
    for j in kume:
        if ( i % j == 0):
            asalOlmayanlar.add(i)
            break
        else:
            asalOlanlar.add(i)
            break
print("Asal sayilar = ",asalOlanlar)
print()
print("Asal olmayan sayilar = ",asalOlmayanlar)



            






