title = {
    "1": "Menu Pilihan",
    "2": "Perulangan",
    "3": "Nilai Mahasiswa"
}

def lineEquals():
    print("=" * 30)

def menu():

    lineEquals()
    print("        " + title["1"] + "        ")
    lineEquals()

    menus = ["Nilai", "Perulangan", "Keluar"]
    i = 0
    for menu in menus:
        i += 1
        print(str(i) + ".", menu)
    lineEquals()


def perulangan():
    print("\n=========", title["2"], "=========")
    start = int(input("Masukkan Awal \t: "))
    end = int(input("Masukkan Akhir \t: "))
    kelipatan = int(input("Masukkan Kelipatan \t: "))

    for a in range(start, end, kelipatan):
        print(a)
    menu()

def nilai():
    lineEquals()
    print("      " + title["3"] +  "      ")
    lineEquals()
    input("Masukkan Nama \t:")
    input("Masukkan Kelas \t:")
    input("Masukkan NPM \t:")
    uts = int(input("Nilai UTS: "))
    uas = int(input("Nilai UAS: "))
    result = (uts + uas) / 2
    print("Rata-rata nilai", result)

    if result >= 90:
        print("GRADE A")
    elif result >= 80:
        print("GRADE B")
    elif result >= 70:
        print("GRADE C")
    else:
        print("Remedial")
    menu()

menu()

while True:
    print()
    selectMenu = int(input("Masukkan Pilihan: "))

    if selectMenu == 1:
        nilai()
    elif selectMenu == 2:
        perulangan()
    elif selectMenu == 3:
        lineEquals()
        print("Terima Kasih")
        break
    else:
        print("Maaf pilihan tidak terdaftar")
        print("Coba lagi [Y/N]")
        if input().upper() == "Y":
            menu()
        else:
            print("")
            break