# Program ini digunakan untuk menghitung pembagian bulat dua angka

def pembagian_bulat(angka1, angka2):
    hasil_pembagian_bulat = angka1 // angka2
    return hasil_pembagian_bulat

angka1 = int(input("Masukkan Bilangan Pertama : "))
angka2 = int(input("Masukkan Bilangan Kedua : "))

hasil_pembagian_bulat = pembagian_bulat(angka1, angka2)
print("==========================================================================")
print(f"Hasil Pembagian Bulat dari {angka1} dan {angka2}: {hasil_pembagian_bulat}")
