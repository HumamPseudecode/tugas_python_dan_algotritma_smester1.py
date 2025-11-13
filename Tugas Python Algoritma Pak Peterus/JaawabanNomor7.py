jumlah_barang = int(input("Masukan Jumlah Barang: "))
harga_satuan = int(input("Masukan Jumlah Harga Satuan: "))

total_pembelian = harga_satuan * jumlah_barang

if total_pembelian >= 500000 and jumlah_barang > 5:
    print("anda mendapatkan strika")
elif total_pembelian >= 100000 and jumlah_barang > 3:
    print("anda mendapatkan payung")
elif total_pembelian >= 50000 and jumlah_barang > 2:
    print("anda mendapatkan BallPoint")

else:
    print("anda tidak mendapatkan Bonus")