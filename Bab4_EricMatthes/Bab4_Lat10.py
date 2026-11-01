#slices
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

#print first three items in the list
print("\nfavorit makananan saya adalah: ")
for food in my_foods[:3]:
    print(food)

#print three items from the middle of the list
print("\nfavorit makanaan saya adalah: ")
for food in my_foods[1:4]:
    print(food)

#print last three items in the list
print("\nfavorit makanan saya adalah: ")
for food in my_foods[-3:]:
    print(food)