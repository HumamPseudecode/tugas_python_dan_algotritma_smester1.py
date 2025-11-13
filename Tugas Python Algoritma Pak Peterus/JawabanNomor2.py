Nama = input("Masukan Nama: ")
Gol = input("Masukan Gol (1-3?): ")
Status = input("Masukan Status (B Belum Kawin / K Kawin) Harus Huruf Besar Yah:  ")
Jumlah_Anak = int(input("Masukan Jumlah Anak: "))

if Gol == "1":
    Gaji = 2500000
elif Gol == "2":
    Gaji = 3000000
elif Gol == "3":
    Gaji = 3500000
else:
    print("Angka tidak valid")


if Status == "K":
    Tunjangan_Istri = 500000
elif Status == "B":
    Tunjangan_Istri = 0
else:
    print("Status Tidak Valid")

if Jumlah_Anak <= 3:
    Tunjangan_Anak = 0.3 * Gaji
else:
    print("Maaf, Anak Mu Kebanyakan")

print("\n=== HASIL PERHITUNGAN GAJI ===")
print("Nama Anda: ", Nama)
print("Golongan Anda: ", Gol)
print("Status Anda: ", Status)
print("Gaji Pokok: Rp", Gaji)
print("Jumlah Anak Anda: ", Jumlah_Anak)
print("Tunjangan Istri: Rp", Tunjangan_Istri)
print("Tunjangan Anak: Rp", Tunjangan_Anak)
print("Total Gaji: Rp", Gaji + Tunjangan_Istri + Tunjangan_Anak)
