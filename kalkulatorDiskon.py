# Program ini digunakan untuk menghitung harga setelah diskon

def hitung_diskon(harga_awal, persen_diskon):
    diskon = harga_awal * (persen_diskon / 100)
    harga_setelah_diskon = harga_awal - diskon
    return harga_setelah_diskon

harga_awal = int(input("Masukkan Harga Barang : "))
persen_diskon = int(input("Masukkan Persentase Diskon : "))

harga_setelah_diskon = int(hitung_diskon(harga_awal, persen_diskon))

print(f"Harga Awal: {harga_awal}")
print(f"Total Diskon: {persen_diskon}%")
print(f"Harga Setelah Diskon: {harga_setelah_diskon}")

