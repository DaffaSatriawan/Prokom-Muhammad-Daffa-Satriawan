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