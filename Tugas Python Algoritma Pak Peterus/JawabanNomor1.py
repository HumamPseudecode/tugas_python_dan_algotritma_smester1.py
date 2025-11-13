Nama = input("masukan Nama: ")
Status = input("Masukan Status (B Belum Kawin / K Kawin) Harus Huruf Besar Yah:  ")
Gol = input("masukan Gol (1/2?): ")

if Gol == "1":
    Gaji = 2500000
elif Gol == "2":
        Gaji = 3000000
else:
    print("angka tidak valid")

if Status == "K":
    Tunjangan_Istri = 500000
elif Status == "B":
    Tunjangan_Istri = 0
else:
    print("Status Tidak Valid")


print("\n=== HASIL PERHITUNGAN GAJI ===")
print("Nama Anda: ", Nama)
print("Gaji Yang Di Peroleh: ", Gaji)
print("Golongan Anda: ", Gol)
print("Status Anda: ", Status)
print("Tunjangan Istri Yang Anda Dapatkan: ", Tunjangan_Istri)
print("Jumlah Total Gaji Yang Di Dapatkan Anda: ",Gaji + Tunjangan_Istri)