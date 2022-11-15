nolist = []
genap = []
ganjil = []

data = int(input("Berapa banyak elemen dalam list: "))
for i in range(data):
    elm = int(input("Masukkan nilai element: "))
    nolist.append(elm)

for j in range(data):
    if (nolist[j] % 2 == 0):
        genap.append(nolist[j])
    else:
        ganjil.append(nolist[j])

print()
print("Element-elemen dalam list:", nolist)
print("Element ganjil dalam list: ", ganjil)
print("Element genap dalam list: ", genap)

