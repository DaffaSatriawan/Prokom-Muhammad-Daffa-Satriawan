# Fungsi Penggajian
def hitung_gaji (jabatan,lembur):
    if lembur <+ 0:
        return 0
    
    if jabatan.lower() == "staff":
        gaji_pokok= 2500000
        gaji_lembur= 100000
    elif jabatan.lower() == "manager":
        gaji_pokok= 5000000
        gaji_lembur=200000
    else:
        return "jabatan tidak valid"

    #Perhitungan gaji
    if lembur == 0:
        total_gaji= gaji_pokok
    else: 
        total_gaji= gaji_pokok + ((lembur-1)*gaji_lembur)

    return total_gaji

#Body Program
print("============================")
print("=== Program Hitung Gaji ====")
print("============================")
jabatan= input("Masukan Jenis Jabatan(staff/manager): ")
lembur= int(input("Masukan Jumlah Lembur(jam): "))

total= hitung_gaji(jabatan,lembur)

if type(total) == int:
    print(f"Total Gaji Karyawan untuk {jabatan} dan akumulasi {lembur} jam lembur adalah: Rp {total}")
else:
    print(total)

print("============================")
print("      Program Selesai       ")
print("============================")