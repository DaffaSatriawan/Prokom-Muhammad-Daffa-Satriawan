# Fungsi Tarif parkir kendaraan di bandara
def hitung_parkir(jenis, durasi):
    if durasi <= 0:
        return 0

    if jenis.lower() == "motor":
        tarif_pertama = 1000
        tarif_berikutnya = 1000
        tarif24jam = 12000
    elif jenis.lower() == "mobil":
        tarif_pertama = 3000
        tarif_berikutnya = 3000
        tarif24jam = 24000
    else:
        return "Jenis kendaraan tidak valid!"

#Perhitungan tarif parkir
if durasi == 1:
    total_tarif = tarif_pertama
elif: 
    durasi >= 24
    total_tarif = tarif24jam
else:
     total_tarif = tarif_pertama + ((durasi - 1) * tarif_berikutnya)
return total_tarif