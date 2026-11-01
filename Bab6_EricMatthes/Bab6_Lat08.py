#Pets
pet1 = {
    'kind': 'dog',
    'owner': 'kayla'
    }
pet2 = {
    'kind': 'cat',
    'owner': 'aan'
    }
pet3 = {
    'kind': 'bird',
    'owner': 'ahmad'
    }

#Pets list
pets = [pet1, pet2, pet3]

# print loop
for pet in pets:
    animal = pet ['kind']
    owner = pet ['owner']

    print (f"Hewan: {animal.title()}")
    print (f"Nama Pemilik: {owner.title()}")
    print ("===================================")