#buffet
buffet_foods = ('pizza', 'pasta', 'salad', 'soup', 'dessert')

#looping untuk menampilkan daftar makanan di buffet
print("Makanan di buffet adalah: ")
for food in buffet_foods:
    print(food)

#mencoba mengubah salah satu item dalam tuple tetapi akan menghasilkan error
#buffet_foods[0] = 'burger'  # This will raise an error

#mengganti seluruh tuple dengan tuple baru
buffet_foods = ('burger', 'fries', 'steak', 'ice cream', 'fruit')

print("\nMakanan di buffet setelah diganti adalah: ")
for food in buffet_foods:
    print(food)
    