#people
person1 = {
    'first_name': 'kayla', 
    'last_name': 'Hani',
    'age' : 26,
    'city': 'semarangs',}
person2 = {
    'first_name': 'aan', 
    'last_name': 'ghani',
    'age' : 25,
    'city': 'magelang',}
person3 = {
    'first_name': 'ahmad', 
    'last_name': 'rizki',
    'age' : 27,
    'city': 'yogyakarta',}

#people list
people = [person1, person2, person3]

# print loop
for person in people:
    print (f"Haloo namaku {person ['first_name']}")
    print (f"Nama belakangku {person ['last_name']}")
    print (f"Umur ku {person ['age']}")
    print (f"Asalku dari {person['city']}")
    print ("=================================================")