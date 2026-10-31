#code review bab 4

#bab 4.1
#list favorit pizza
list_favorit_pizza = ['pepperoni', 'margherita', 'hawaiian', 'bbq chicken', 'veggie']

#looping untuk menampilkan daftar favorit pizza
for pizza in list_favorit_pizza:
    print(f" saya suka pizza dengan topping {pizza}")

#diluar loop
print("Saya benar-benar menyukai pizza!")

#bab 4.2
#list animal
list_animal = ['kucing', 'anjing', 'kelinci', 'hamster', 'burung']

#statemnt untuk menampilkan daftar animal
for animal in list_animal:
    print(f" saya suka hewan peliharaan {animal}")

#common statement
print("hewan hewan ini cocok dipelihara!")

#Bab 4.11
#List pizza
friend_pizzas = ['pepperoni', 'margherita', 'hawaiian', 'bbq chicken', 'veggie']
my_favorite_pizzas = ['pepperoni', 'margherita', 'hawaiian', 'bbq chicken', 'veggie']

#add new pizza to the list
my_favorite_pizzas.append('meat lovers')

#add a different pizza to the list
friend_pizzas.append('cheese')

#looping untuk menampilkan daftar favorit pizza
for pizza in my_favorite_pizzas:
    print(f" saya suka pizza dengan topping {pizza}")

#looping untuk menampilkan daftar favorit pizza teman
for pizza in friend_pizzas:
    print(f" teman saya suka pizza dengan topping {pizza}")


#Indentasi 4 spasi
#Panjang baris di bawah 80 karakter: Pastikan tidak ada baris kode yang terlalu panjang. 
#Baris kosong secukupnya