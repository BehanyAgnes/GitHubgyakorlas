print("Üdvözöljük a gyümölcsboltban!")
print("Kétféle gyümölcs kapható:")

gyumolcs = input("Kérem válassza ki a gyümölcsöt (alma/körte): ")
mennyiseg = int(input("Kérem adja meg hány darabot szeretne vásárolni: "))

if gyumolcs == "alma":
    osszeg = mennyiseg * 150
    print(f"A választott gyümölcs: {gyumolcs}")
    print(f"Mennyiség: {mennyiseg} darab")
    print(f"Fizetendő összeg: {osszeg} Ft")
elif gyumolcs == "körte": 
    osszeg = mennyiseg * 200
    print(f"A választott gyümölcs: {gyumolcs}")
    print(f"Mennyiség: {mennyiseg} darab")
    print(f"Fizetendő összeg: {osszeg} Ft")



