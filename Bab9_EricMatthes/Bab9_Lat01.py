#class
class Restaurant:
    def __init__(self, resto_name, resto_cuisine):
        self.resto_name = resto_name
        self.resto_cuisine = resto_cuisine

    def describe_restaurant(self):
        print(f"Nama Restauran adalah {self.resto_name}")
        print(f"Jenis Masakan adalah {self.resto_cuisine}")

    def open(self):
        print(f"{self.resto_name} Restauran Is Open")

restaurant = Restaurant ('Karisma Bahari', 'italian')
print(restaurant.resto_name)
print(restaurant.resto_cuisine)
print()

restaurant.describe_restaurant()
restaurant.open()

