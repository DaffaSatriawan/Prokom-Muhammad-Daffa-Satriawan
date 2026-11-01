#sandwich
def make_sandwich(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

#memanggil
make_sandwich('roti', 'selada', 'tomat', 'keju')
make_sandwich('roti', 'daging', 'mayones')
make_sandwich('roti', 'telur', 'bacon', 'keju', 'saus')
