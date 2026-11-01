# Program Tiket Bioskop
print("Masukkan usia Anda (ketik 'quit' untuk keluar)")

while True:
    age_input = input("\nUsia Anda: ")
    
    # Cek apakah pengguna ingin keluar dari program
    if age_input.lower() == 'quit':
        print("\nTerima kasih! Silahkan datang kembali.")
        break
    
    # Ubah input string menjadi integer
    age = int(age_input)
    
    # Percabangan harga tiket berdasarkan usia
    if age < 3:
        print("Tiket gratis.")
    elif age <= 12:
        print("Harga tiket $10.")
    else:
        print("Harga tiket $15.")