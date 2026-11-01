#conditional test
car= 'cherry'

#5 tests yang berhasil dan true
print("Is car == 'cherry'? I predict True.")
print(car == 'cherry')

print("\nIs car == 'apple'? I predict True.")
print(car != 'apple')

print("\nIs car == 'CHERRY'? I predict True.")
print(car.lower() == 'cherry')

print("\nIs car == 'CHERRY'? I predict True.")
print(car.upper() == 'CHERRY')

#5 tests yang gagal dan false
print("\nIs car == 'banana'? I predict False.")
print(car == 'banana')

print("\nIs car == 'grape'? I predict False.")
print(car == 'grape')

print("\nIs car < 'banana'? I predict False.")
print(car < 'banana')

print("\nIs car > 'grape'? I predict False.")
print(car > 'grape')

print("\nIs car == 'CHERRY'? I predict False.")
print(car.lower() == 'CHERRY')