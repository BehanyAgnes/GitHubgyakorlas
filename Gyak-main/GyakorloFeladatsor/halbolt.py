print("Üdvözöljük a halboltban!")
print("Kétféle hal kapható \n Lazac - 3000 Ft/kg \n Pisztráng - 2500 Ft/kg")

hal = input("Kérem, válassza ki a halat (lazac/pisztráng): ")
mennyiseg = int(input("Kérem, adja meg, hány kilogrammot szeretne vásárolni: "))

if hal == "lazac":
    osszeg = mennyiseg * 3000
    print(f"A választott hal: {hal} \n Mennyiség: {mennyiseg} \n Az összeg: {osszeg} Ft")
elif hal == "pisztráng":
    osszeg = mennyiseg * 2500
    print(f"A választott hal: {hal} \n Mennyiség: {mennyiseg} \n Az összeg: {osszeg} Ft")


