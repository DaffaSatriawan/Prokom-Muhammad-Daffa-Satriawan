#favorit fruit
favorite_Fruits = ['mangga', 'sawo', 'semangka']

#if block
if 'mangga' in favorite_Fruits:
    print("kamu suka sekali dengan mangga ")

if 'sawo' in favorite_Fruits:
    print("kamu suka sama sawo?")

if 'semangka' in favorite_Fruits:
    print("kamu suka sekali dengan semangka")

if 'melon' not in favorite_Fruits:
    print("kamu gasuka sama melon")

if all(fruit in favorite_Fruits for fruit in ['mangga', 'sawo', 'semangka']):
    print(f"buah favorit mu adalah {favorite_Fruits}")