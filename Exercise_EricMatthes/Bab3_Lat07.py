#nambah tamu
tamu = ['Dimas', 'Rizki', 'Fajar']
print("Kita akan mengundang tamu yang lebih banyak")

tamu.insert(0, 'Budi')

#nambah tamu middle
tamu.insert(2, 'Andi')

#nambah tamu akhir
tamu.append('Caca')

#maaf, kita hanya bisa mengundang 2 tamu
print("Maaf, kita hanya bisa mengundang 2 tamu")

#hapus tamu
popped_tamu = tamu.pop()
print(f"Maaf {popped_tamu}, kita tidak bisa mengundangmu")

popped_tamu = tamu.pop()
print(f"Maaf {popped_tamu}, kita tidak bisa mengundangmu")

popped_tamu = tamu.pop()
print(f"Maaf {popped_tamu}, kita tidak bisa mengundangmu")

popped_tamu = tamu.pop()
print(f"Maaf {popped_tamu}, kita tidak bisa mengundangmu")

#massage 2 tamu yang tersisa
print(f"yuk makan malam bersama {tamu[0]}")
print(f"ayo makan malam bersama {tamu[1]}")

del tamu[0]
del tamu[0]

print("daftar tamu sekarang:", tamu)

