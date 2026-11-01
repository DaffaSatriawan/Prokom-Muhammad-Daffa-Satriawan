#Movies Ticket
age = input("Masukkan usia anda: ")
age = int(age)

if age < 3:
    print("Tiket gratis.")
elif age <= 12:
    print("Harga tiket $10.")
else:
    print("Harga tiket $15.")