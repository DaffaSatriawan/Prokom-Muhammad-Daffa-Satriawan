#three classes
class Restaurant:
    def __init__(self, resto_name, resto_cuisine):
        self.resto_name = resto_name
        self.resto_cuisine = resto_cuisine

    def describe_restaurant(self):
        print(f"Nama Restauran adalah {self.resto_name}")
        print(f"Jenis Masakan adalah {self.resto_cuisine}")

    def open(self):
        print(f"{self.resto_name} Restauran Is Open")

restoran_pertama = Restaurant('Sate Padang', 'Nusantara')
restoran_kedua = Restaurant('Pizza Hut', 'Fast Food')
restoran_ketiga = Restaurant('Bakso Malang', 'Indonesian')

#print
restoran_pertama.describe_restaurant()
restoran_kedua.describe_restaurant()
restoran_ketiga.describe_restaurant()