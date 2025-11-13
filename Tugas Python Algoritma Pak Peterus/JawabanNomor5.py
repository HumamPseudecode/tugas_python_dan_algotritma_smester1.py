bilangan_pertama = int(input("Masukan Bilangan Pertama: "))
bilangan_kedua = int(input("Masukan Bilangan Kedua: "))
bilangan_ketiga = int(input("Masukan Bilanga Ketiga: "))

if bilangan_pertama > bilangan_kedua and bilangan_ketiga:
    print(f"bilangan {bilangan_pertama} adalah bilangan terbesar dari pada bilangan {bilangan_kedua} dan bilangan {bilangan_ketiga} ")
elif bilangan_kedua > bilangan_pertama and bilangan_ketiga:
    print(f"bilangan {bilangan_kedua} adalah bilangan terbesar dari pada bilangan {bilangan_pertama} dan bilangan {bilangan_ketiga} ")
elif bilangan_ketiga > bilangan_pertama and bilangan_kedua:
    print(f"bilangan {bilangan_ketiga} adalah bilangan terbesar dari pada bilangan {bilangan_kedua} dan bilangan {bilangan_pertama} ")
    
else:
    print("anda salah input paok")