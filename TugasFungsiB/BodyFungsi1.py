import ModulFungsi1 as mf1

# Body Program 
print("===================================")
print("    PROGRAM HITUNG TARIF PARKIR    ")
print("===================================")

kendaraan = input("masukan jenis kendaraan (motor/mobil): ")
jammasuk = int(input("masukan jam masuk(jam): "))
jamkeluar = int(input("masukan jam keluar(jam): "))
jam = jamkeluar - jammasuk

total = mf1.hitung_parkir(kendaraan, jam)

if type(total) == int:
    print(f"Total biaya parkir untuk {kendaraan} selama {jam} jam adalah: Rp {total}")
else:
    print(total)

print("============================")
print("      Program Selesai       ")
print("============================")