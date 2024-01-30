# Program ini digunakan untuk menghitung Indeks Massa Tubuh (BMI)

def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

berat = int(input("Masukkan Berat Badan(dalam centimeter) : "))
tinggi = int(input("Masukkan Tinggi Badan(dalam meter) : "))

hasil_bmi = hitung_bmi(berat, tinggi)

print(f"Berat: {berat} kg")
print(f"Tinggi: {tinggi} m")
print(f"BMI: {hasil_bmi}")

