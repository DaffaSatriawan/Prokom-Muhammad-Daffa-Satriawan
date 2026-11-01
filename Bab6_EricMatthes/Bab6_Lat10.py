#favorit places
person = {
    'aan': ['1', '4'],
    'kayla': ['2', '6'], 
    'nay': ['3', '7', '9'], 
    'iki': ['4'], 
    'adib': ['5', '10'] 
}

#looping print
for persons, number in person.items():
    print (f"Angka favorit {persons.title()} adalah: ")
    for number in number:
        print (f"\t- {number}")
