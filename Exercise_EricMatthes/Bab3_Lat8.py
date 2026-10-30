#list places in the world
list_places = ['Bali', 'Lombok', 'Raja Ampat', 'Labuan Bajo', 'Yogyakarta']
print("original list:")
print(list_places)

#ururtan asli
print("\nUrutan alfabetis (menggunakan sorted()):")
print(sorted(list_places))

#ururtan sorted tapi alfabetis tanpa mengubah list asli
print("\nUrutan asli setelah sorted():")
print(list_places)

#pakai sorted tapi ururtan terbalik tanpa mengubah list asli
print("\nUrutan terbalik (menggunakan sort(reverse=True)):")
print(sorted(list_places, reverse=True))

#list menunjukan bahwa masih dalam urutan asli
print("\nUrutan asli sekali lagi:")
print(list_places)

#Menggunakan reverse() sekali lagi untuk mengembalikannya ke urutan asli
list_places.reverse()
print("\nUrutan asli setelah reverse():")
print(list_places)

#Menggunakan sort() agar list tersimpan dalam urutan alfabetis
list_places.sort()
print("\nUrutan alfabetis setelah sort():")
print(list_places)

#Menggunakan sort() dengan reverse=True agar list tersimpan dalam urutan terbalik
list_places.sort(reverse=True)
print("\nUrutan terbalik setelah sort(reverse=True):")
print(list_places)



