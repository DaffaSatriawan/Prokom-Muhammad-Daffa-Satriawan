#Extensions
pet1 = {
    'kind': 'dog',
    'owner': 'kayla',
    'age': 2,
    'food': 'daging',
    }
pet2 = {
    'kind': 'cat',
    'owner': 'aan',
    'age': 1,
    'food': 'ikan',
    }
pet3 = {
    'kind': 'bird',
    'owner': 'ahmad',
    'age': 3,
    'food': 'benih'
    }

#Pets list
pets = [pet1, pet2, pet3]

# print loop
for pet in pets:
    animal = pet ['kind']
    owner = pet ['owner']
    age = pet ['age']
    food = pet ['food']

    print ("===================================")
    print (f"Hewan: {animal.title()}")
    print (f"Nama Pemilik: {owner.title()}")
    print (f"Usia: {age}")
    print (f"Makanan: {food}")
    print ("===================================")