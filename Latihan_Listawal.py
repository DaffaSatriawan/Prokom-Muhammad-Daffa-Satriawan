print("=== tugas 1 & 2 ===")

# input 3 angka dari pengguna dan disimpan ke list
angka = []
for i in range (3):
    val =float(input(f"Masukkan angka ke-{i+1}: "))
    angka.append(val)

# --- NOMOR 1: Hitung Total, Rata-rata, & Standar Deviasi Manual ---
total = 0
for x in angka:
    total = total + x

rata_rata = total/ len(angka)

# Rumus deviasi
selisih= 0
for x in angka:
    selisih= selisih + (x - rata_rata) ** 2

stdev = (selisih / len(angka)) ** 0.5

print("\n--- Hasil Nomor 1 ---")
print("Total       :", total)
print("Rata-rata   :", rata_rata)
print("St. Deviasi :", stdev)

# --- NOMOR 2: Cari Min & Max Manual ---
min_val = angka[0]
max_val = angka[0]

for x in angka:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x

print("--- Hasil Nomor 2 ---")
print("Nilai Minimum :", min_val)
print("Nilai Maksimum :", max_val)