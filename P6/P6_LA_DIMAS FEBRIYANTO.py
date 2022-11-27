import persegi
import segitiga

def menu():
    
    isRunning = True
    while isRunning:
        print("Menu Menghitung Luas Persegi dan Segitiga")
        print("1. Luas Segitiga")
        print("2. Keliling Segitiga")
        print("3. Luas Persegi")
        print("4. Keliling Persegi")
        print("5. Keluar")
    
        select = int(input("\nKetik Menu Pilihan: "))

        if select == 1:
            alas = input("Masukkan Alas: ")
            tinggi = input("Masukkan Tinggi: ")
            print("Luas Segitiga adalah", segitiga.luas(alas, tinggi))
        elif select == 2:
            sisi = input("Masukkan Sisi: ")
            print("Keliling Segitiga adalah", segitiga.keliling(sisi))
        elif select == 3:
            sisi = input("Masukkan Sisi: ")
            print("Luas Persegi adalah", persegi.luas(sisi))
        elif select == 4:
            sisi = input("Masukkan Sisi: ")
            print("Keliling Persegi adalah", persegi.keliling(sisi))
        elif select == 5:
            print("See you next time!")
            break
        else:
            print("Menu tidak tersedia")

        print()

        needNext = input("Apakah ingin lanjut?[Y/T]")
        if needNext.upper() == "T":
            print("See you next time!")
            print()
            isRunning = False

        print()

def main():
    menu()

main()