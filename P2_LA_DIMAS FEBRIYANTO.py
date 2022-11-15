def biodata():
    print("         Program Biodata Mahasiswa          ")
    print("--------------------------------------------")
    nama = input("Masukkan Nama Anda \t: ")
    kelas = input("Masukkan Kelas Anda \t: ")
    npm = input("Masukkan NPM Anda \t: ")
    print("============================================")
    print("Nama Anda adalah ", nama)
    print("Nama Anda adalah ", kelas)
    print("Nama Anda adalah ", npm)
    print()

def luasLingkaran():
    print("     Program Menghitung Luas Lingkaran      ")
    print("--------------------------------------------")
    phi = 3.14
    jariJari = float(input("Masukkan Jari-Jari Lingkaran: "))
    luasLingkaran = phi * jariJari * jariJari
    print("============================================")
    print(f"Luas Lingkaran adalah {luasLingkaran:.2f} cm2")

def main():
    print("--------------------------------------------")
    print("                 Activity                   ")
    print("--------------------------------------------")
    biodata()
    print("--------------------------------------------")
    luasLingkaran()

main()