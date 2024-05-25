#Iki setin ortak elemanlarinin toplami 
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
kesisim = set()
toplam = 0

for i in set1:
    if ( i in set2):
        kesisim.add(i)

for i in set2:
    if ( i in set1):
        kesisim.add(i)

for i in kesisim:
    toplam+=i
print(toplam)






