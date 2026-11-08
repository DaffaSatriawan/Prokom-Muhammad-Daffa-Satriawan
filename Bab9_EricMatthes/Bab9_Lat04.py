#class nambah
class Restaurant:
    def __init__(self, resto_name, resto_cuisine,):
        self.resto_name = resto_name
        self.resto_cuisine = resto_cuisine
        self.served = 0

    def describe_restaurant(self):
        print(f"Nama Restauran adalah {self.resto_name}")
        print(f"Jenis Masakan adalah {self.resto_cuisine}")

    def open(self):
        print(f"{self.resto_name} Restauran Is Open")

    def number_served(self):
        print(f"the restauran served right now is {self.served}")

    def set_number_served (self, number):
        self.number_served = number
        print(f"set number is {self.number_served}")

    def incriment_number_served (self, additional_served):
        self.number_served += additional_served
        print(f"incriment is {self.number_served}")
    
restaurant = Restaurant ('Karisma Bahari', 'italian')
restaurant.describe_restaurant()
restaurant.served = 29
restaurant.number_served()
restaurant.set_number_served(80)
restaurant.incriment_number_served(120)

