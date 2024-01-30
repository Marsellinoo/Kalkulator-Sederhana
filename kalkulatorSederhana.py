# Program ini adalah kalkulator sederhana

def penjumlahan(angka1, angka2):
    return angka1 + angka2

def pengurangan(angka1, angka2):
    return angka1 - angka2

def perkalian(angka1, angka2):
    return angka1 * angka2

def pembagian(angka1, angka2):
    if angka2 != 0:
        return angka1 / angka2
    else:
        return "Tidak dapat dibagi (Angka 2 tidak boleh nol)"

angka1 = int(input("Masukkan angka pertama : "))
angka2 = int(input("Masukkan angka pertama : "))

hasil_penjumlahan = penjumlahan(angka1, angka2)
hasil_pengurangan = pengurangan(angka1, angka2)
hasil_perkalian = perkalian(angka1, angka2)
hasil_pembagian = int(pembagian(angka1, angka2))
print("===============================================================================")
print(f"Hasil Penjumlahan: {hasil_penjumlahan}")
print(f"Hasil Pengurangan: {hasil_pengurangan}")
print(f"Hasil Perkalian: {hasil_perkalian}")
print(f"Hasil Pembagian: {hasil_pembagian}")
print("===============================================================================")
