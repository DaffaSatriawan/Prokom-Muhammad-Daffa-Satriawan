#city names
def city_country(city, country):
    """Display a message about the city and its country."""
    return f"{city.title()}, {country.title()}"

#memanggil
place1 = city_country('semarang', 'indonesia')
place2 = city_country('rio de janeiro', 'brazil')
place3 = city_country('new york', 'usa')

#print
print(place1)
print(place2)
print(place3)