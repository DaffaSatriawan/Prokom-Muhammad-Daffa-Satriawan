#Membuat fungsi sendiri
def hitung_reamur(celcius):
    reamur = celcius * 4/5
    return reamur

celcius = 100
reamur = hitung_reamur(celcius)
nilaireamur = hitung_reamur(celcius)
print(nilaireamur)

#Fungsi 2.2
def statnilai(ListNilai):
    total= 0
    for nilai in ListNilai:
        total= total+ nilai
    rataan= total/ len(ListNilai)
    #rataan
    variansi= sum((x-rataan)**2 for x in ListNilai) / len(ListNilai)
    stdev= variansi **0.5
    return total, rataan, stdev

nilaiA= [80,90,50]

totalNIlai, rataanNilai, stdevNilai = statnilai(nilaiA)
print("Total Nilai Kelas : ", totalNIlai)
print("Rata-rata Nilai Kelas : ", rataanNilai)
print("Standar Deviasi Nilai Kelas : ", stdevNilai)
