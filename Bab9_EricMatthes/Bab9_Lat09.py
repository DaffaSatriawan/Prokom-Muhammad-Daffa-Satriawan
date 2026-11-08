#Battery update
"""A set of classes that can be used to represent electric cars."""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"Battery size right now is {self.battery_size}")
        else:
            print("Kapasitas sudah penuh")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes of the parent class.

        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

print("--- Membuat Mobil Listrik Baru ---")
my_tesla = ElectricCar("tesla", "model s", 2024)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
print("Jarak tempuh awal: ")

my_tesla.battery.upgrade_battery()

print("Jarak tempuh setelah di upgrade: ")
my_tesla.battery.get_range()