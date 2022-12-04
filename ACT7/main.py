import numpy as np

class lingkaran:
    def luas(self, jari):
        self.jari = jari
        return np.pi * (jari ** 2)

class segitiga:
    def inputSeg(self):
        self.alas = int(input("Masukkan Alas: "))
        self.tinggi = int(input("Masukkan Tinggi: "))

    def luas(self):
        self.hasilSeg = (self.alas * self.tinggi) / 2

class trapesium:
    def inputTra(self):
        self.sisiSatu = int(input("Masukkan Sisi 1: "))
        self.sisiDua = int(input("Masukkan Sisi 2: "))
        self.tinggi = int(input("Masukkan Tinggi: "))

    def luas(self):
        self.hasilTra = (self.sisiSatu * self.sisiDua) * self.tinggi / 2

class jajar(segitiga):
    def luasJar(self):
        self.hasilJar = self.alas * self.tinggi

def menu():
    
    print("")

    isRunning = True
    while isRunning == True:
        
        menu = ["Lingkaran", "Segitiga", "Trapesium", "Jajar Genjang"]
    
        print("====Menu Pilihan====")
        i = 0
        for item in menu:
            i = i + 1
            print(str(i) + ".", item)
        print("====================")

        pilih = int(input("Masukkan Pilihan Menu: "))
        
        print()
        if pilih == 1:
            print("Menghitung Luas Lingkaran")
            hasil = lingkaran()

            jari = int(input("Masukkan Jari Jari: "))

            print()
            print("Luas Lingkaran adalah: ", hasil.luas(jari))
        elif pilih == 2:
            print("Menghitung Luas Segitiga")
            hasil = segitiga()
            hasil.inputSeg()
            hasil.luas()
            print()
            print("Luas Segitiga adalah: ", hasil.hasilSeg)
        elif pilih == 3:
            print("Menghitung Luas Trapesium")
            hasil = trapesium()
            hasil.inputTra()
            hasil.luas()
            print()
            print("Luas Trapesium adalah ", hasil.hasilTra)
        elif pilih == 4:
            print("Menghitung Luas Jajargenjang")
            hasil = jajar()
            hasil.inputSeg()
            hasil.luasJar()
            print("Luas Jajargenjang adalah", hasil.hasilJar)
        else:
            print("Masukkan Pilihan yang benar")
    
        needNext = input("Need Next? [Y/T] ? ")
        

        print(needNext)        
        if needNext.upper() == "T":
            isRunning = False

menu()