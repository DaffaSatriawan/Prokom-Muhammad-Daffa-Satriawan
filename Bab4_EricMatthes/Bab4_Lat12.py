#More loops
my_foods = ['pizza', 'falafel', 'carrot cake']

#friend's favorite foods
friend_foods = my_foods[:]

#add new food to the list
my_foods.append('cannoli')
friend_foods.append('ice cream')

#looping untuk menampilkan daftar favorit makanan saya
print("favorit makanan saya adalah: ")
for food in my_foods:
    print(food)

#looping untuk menampilkan daftar favorit makanan teman saya
print("\nfavorit makanan teman saya adalah: ")
for food in friend_foods:
    print(food)
    