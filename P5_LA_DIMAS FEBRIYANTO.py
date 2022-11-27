def menulisData():
    file = open("Dimas.txt", "w")

    print("---Menulis Data---")
    nama = input("Masukkan Nama : ")
    kelas = input("Masukkan Kelas : ")
    npm = input("Masukkan NPM : ")
    hobi = input("Masukkan Hobi : ")
    makan = input("Masukkan Makanan Kesukaan : ")
    cita = input("Masukkan Cita-Cita : ")

    file.write(nama + "\n")
    file.write(kelas + "\n")
    file.write(npm + "\n")
    file.write(hobi + "\n")
    file.write(makan + "\n")
    file.write(cita + "\n")

    file.close()
    print("\n")
    print("Data berhasil ditulis")
    print("---------------------\n")

def bacaData():
    file = open("Dimas.txt", "r")
    
    readFile = file.read()
    print("---Baca Data---")
    print(readFile)
    file.close()
    print("Data berhasil dibaca\n")

def tambahData():
    file = open("Dimas.txt", "a")

    print("---Tambah Data---")
    angka1 = int(input("Masukkan angka 1 : "))
    angka2 = int(input("Masukkan angka 2 : "))

    file.write(str(angka1) + "\n")
    file.write(str(angka2) + "\n")

    file.close()
    print("\n")
    print("Data berhasil ditambah\n")

def main():
    menulisData()
    tambahData()
    bacaData()

main()