#ice cream stand

class Restaurant:
    def __init__(self, resto_name, resto_cuisine,):
        self.resto_name = resto_name
        self.resto_cuisine = resto_cuisine
    
    def describe_restaurant(self):
        print(f"Nama Restauran adalah {self.resto_name}")
        print(f"Jenis Masakan adalah {self.resto_cuisine}")

    def open(self):
        print(f"{self.resto_name} Restauran Is Open")

class IceCreamRestauran (Restaurant):
    def __init__(self, resto_name, resto_cuisine='ice cream'):
        super().__init__(resto_name, resto_cuisine)
        self.flavor = ["vanila","coklat","matcha","tiramissu"]

    def display (self):
        print(f"Daftar icecream: ")
        for flavor in self.flavor:
            print(f" - {flavor}")

my_toko = IceCreamRestauran("gelatoku")
my_toko.describe_restaurant()
my_toko.open()
my_toko.display()