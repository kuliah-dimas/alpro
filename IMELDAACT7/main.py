import numpy as np

hero = [
        {
            "name": "Imelda",
            "health": 100,
            "power": 20,
            "armor": 50
        }, 
        {
            "name": "Dimas", 
            "health": 100, 
            "power": 20, 
            "armor": 50
        },
        {
            "name": "Ucok", 
            "health": 100, 
            "power": 20, 
            "armor": 50
        },
    ]

isRun = True
while isRun:
    print(hero[0]["name"] + " menyerang " + str(hero[1]["name"]))
    print(hero[1]["name"] + " diserang " + str(hero[0]["name"]))
    nilaiSerang = int(input("Serangan terasa: "))

    print()

    hero[1]["health"] = hero[1]["health"] - nilaiSerang

    print("Sisa darah " + hero[1]["name"], str(hero[1]["health"]))

    print()    