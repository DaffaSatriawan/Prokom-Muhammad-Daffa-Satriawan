# Membuat list berisi beberapa nama kota
kota = ["Jakarta", "Bandung", "Surabaya"]

#  MEMBUAT ERROR SENGAJA (IndexError) 
# List di atas hanya memiliki 3 elemen (indeks 0, 1, dan 2).
# Jika kita mencoba mengakses indeks ke-5 seperti di bawah ini:
# print(kota[5])  # <-- Ini akan memunculkan error: IndexError: list index out of range

#  MEMPERBAIKI ERROR 
# Untuk memperbaikinya, pastikan indeks yang dipanggil berada dalam rentang yang valid (0, 1, atau 2)
print(f"Kota yang diakses dengan benar: {kota[2]}")
