#Dictionary Kullanimi

a = { "bir" : [ [1,2,3],[4,5,6],[7,8,9]], "iki" : "Emir"}

for k,v in a.items():   
    print(k,v)

#Degerlerin toplamini hesaplama
d = {"a": 5, "b": 10, "c": 3}
toplam =0

for i in d.values():
    toplam+=i


print(toplam)



#Anahtarin ve degerlerin yerlerini degistirme

d = {"a": 1, "b": 2, "c": 3}
swap = {}

for key,value in d.items():
    swap[value] = key

print(swap)




#Sözlükteki en yuksek degerli anahtari bulma 1.Yol


d = {"a": 5, "b": 10, "c": 3}

maximum = d["a"]

for i in d.keys():
    if(maximum < d[i]):
        maximum = d[i]
print(maximum)


#Sözlükteki en yuksek degerli anahtari bulma 2.Yol


d = {"a": 5, "b": 10, "c": 3}

maxValue= max(d.values())
maxKey = None

for k,v in d.items():
    if ( maxValue == v):
        maxKey = k
        break
print(maxKey)




#Sözlük Değerlerinin Kaç Kez Tekrar Ettiğini Sayma

d= ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}

for i in d:
    if ( i in frequency):
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)



#İki sozlugu birlestirme

d1 = {"a": 5, "b": 10, "c": 3}
d2 = {"b": 7, "c": 4, "d": 8}
d3=d1.copy()

for k,v in d2.items():
    if ( k in d3):
        d3[k]+=v
    else:
        d3[k]=v
print(d3)






















    





















