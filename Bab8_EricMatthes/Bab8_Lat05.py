#cities
def describe_city(city, country='Indonesia'):
    """Display a message about the city and its country."""
    print(f"{city.title()} is in {country.title()}.")


describe_city("semarang")
describe_city("jakarta")
describe_city("new york", "USA")
