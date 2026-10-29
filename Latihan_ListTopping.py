#Daftar topping yang tersedia
topping_tersedia = ['keju', 'coklat', 'kacang', 'pisang', 'ketan item']
pesanan_topping = []

print ("=== Selamat Datang di terang bulan aa anjay ===")
print ("Daftar Topping yang Tersedia:")

#Menampilkan pilihan toppping
print("Daftar Topping:", topping_tersedia)

print("================================================")

#2. Meminta pelanggan input untuk pemesanan topping
while True:
    pilihanpembeli = input("Masukan nama topping yang ingin dipesan: ")

    #jika pembeli mengetik 'selesai'
    if pilihanpembeli == 'selesai':
        break

    pesanan_topping.append(pilihanpembeli)

print("Topping yang kamu pesan:",  pesanan_topping)
