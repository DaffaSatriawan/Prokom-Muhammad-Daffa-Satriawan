#restauran seating
seating = input("Berapa orang yang akan makan di restoran? ")
seating = int(seating)

#if statement
if seating > 8:
    print("Maaf, anda harus menunggu meja kosong")
else:
    print("Meja tersedia, silahkan masuk")