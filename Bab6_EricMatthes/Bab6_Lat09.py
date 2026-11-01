#favorit places
favoritplaces = {
    'aan': ['baitul aqsa', 'mongolia'],
    'rizki': ['yogyakarta', 'batam', 'thepark'],
    'kayla': ['semarang']
}
#print loop
for person, places in favoritplaces.items():
    print (f"\n{person.title()} menyukai tempat tempat berikut:")
    for place in places:
        print(f"\t- {place.title()}")