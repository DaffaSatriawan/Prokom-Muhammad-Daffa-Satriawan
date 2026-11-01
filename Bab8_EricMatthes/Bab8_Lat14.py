#Cars
def make_car(manufacturer, model, **car_info):
    """Return a dictionary representing a car."""
    car = {
        'manufacturer': manufacturer.title(),
        'model': model.title()
    }
    for key, value in car_info.items():
        car[key] = value
    return car

#print
car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)