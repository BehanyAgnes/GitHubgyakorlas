mertekegyseg = input("Milyen mértékegységről szeretne átváltani? (liter/dl):")
mennyiseg = int(input("Adja meg az átváltandó mennyiséget: "))

if mertekegyseg == "liter":
    osszeg = mennyiseg * 10
elif mertekegyseg == "dl":
    osszeg = mennyiseg /10

print(f"{mennyiseg} deciliter = {osszeg} liter")