# Every Function (Menggunakan daftar gunung)

# 1. Membuat list awal berisi beberapa nama gunung
gunung = ["Semeru", "Rinjani", "Kerinci", "Merapi", "Agung"]
print(f"Daftar gunung awal: {gunung}")

# 2. Menggunakan len() 
print(f"Jumlah gunung dalam list: {len(gunung)}")

# 3. Menggunakan append() 
gunung.append("Jayawijaya")
print(f"Setelah append('Jayawijaya'): {gunung}")

# 4. Menggunakan insert() untuk menyisipkan 
gunung.insert(1, "Bromo")
print(f"Setelah insert(1, 'Bromo'): {gunung}")

# 5. Menggunakan pop() untuk menghapus gunung terakhir
gunung_terhapus = gunung.pop()
print(f"Gunung yang dihapus dengan pop(): {gunung_terhapus}")
print(f"List sekarang: {gunung}")

# 6. Menggunakan perintah del untuk menghapus 
del gunung[0]
print(f"Setelah del elemen indeks ke-0: {gunung}")

# 7. Menggunakan sorted() untuk mencetak urutan abjad 
print(f"Urutan sorted() sementara (A-Z): {sorted(gunung)}")
print(f"List asli tidak berubah: {gunung}")

# 8. Menggunakan sorted() dengan reverse=True untuk urutan abjad terbalik sementara
print(f"Sorted sementara (Z-A): {sorted(gunung, reverse=True)}")

# 9. Menggunakan reverse() untuk membalikkan urutan list asli secara permanen
gunung.reverse()
print(f"Setelah reverse(): {gunung}")

# 10. Menggunakan reverse() lagi untuk mengembalikannya ke urutan semula
gunung.reverse()

# 11. Menggunakan sort()
gunung.sort()
print(f"Setelah sort() (Abjad A-Z): {gunung}")

# 12. Menggunakan sort(reverse=True) secara permanen (Z-A)
gunung.sort(reverse=True)
print(f"Setelah sort(reverse=True) (Abjad Z-A): {gunung}")