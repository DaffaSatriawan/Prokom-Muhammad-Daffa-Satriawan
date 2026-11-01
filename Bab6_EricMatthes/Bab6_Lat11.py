#cities
cities = {
    'SOLO': {
        'country': 'indonesia',
        'population': 500,
        'fact': 'punya raja',
    },

    'RIODEJENARIO': {
        'country': 'brazil',
        'population': 300,
        'fact': 'punya patung tertinggi ',
    },

    'PARIS': {
    'country': 'prancis',
    'population': 100,
    'fact': 'punya menara eifel',   
    }
}

#print blok looping
for city, cities_info in cities.items():
    print(f"\n {city}")
    Country = f"{cities_info['country']}"
    population = cities_info['population']
    fact = cities_info['fact']

    print(f"\t- Country: {Country.title()}")
    print(f"\t- Population: {population}")
    print(f"\t- Fact: {fact.title()}")
    print ("=================================================")
