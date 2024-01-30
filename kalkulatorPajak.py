# Program ini digunakan untuk menghitung jumlah pajak yang harus dibayar

def hitung_pajak(penghasilan):
    if penghasilan <= 10000:
        tarif_pajak = 0.10
    elif penghasilan <= 50000:
        tarif_pajak = 0.15
    else:
        tarif_pajak = 0.20

    pajak = penghasilan * tarif_pajak
    return pajak, tarif_pajak

penghasilan = int(input("Berapa Penghasilan Anda : "))

jumlah_pajak, tarif_pajak = hitung_pajak(penghasilan)
print("=====================================================================")
print(f"Penghasilan: {penghasilan}")
print(f"Jumlah Pajak: {jumlah_pajak}")
print(f"Tarif Pajak: {tarif_pajak * 100}%")

