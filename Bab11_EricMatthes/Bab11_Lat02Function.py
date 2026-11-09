def city_country(city, country, population=''):
  """Mengembalikan string seperti 'Santiago, Chile - population 5000000'."""
  if population:
    return f"{city.title()}, {country.title()} - population {population}"
  else:
    return f"{city.title()}, {country.title()}"