#More conditional tests
buah= 'mangga'

#tes kesamaan dan ketidaksamaan
print("Is buah == 'mangga'? I predict True.")
print(buah == 'mangga')

print("\nIs buah == 'apel'? I predict False.")
print(buah == 'apel')

#tes menggunakan lower
print("\nIs buah == 'MANGGA'? I predict True.")
print(buah.lower() == 'mangga')

#tes numerik
age = 20
print("\nIs age == 20? I predict True.")
print(age == 20)

print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 20? I predict True.")
print(age >= 20)

print("\nIs age <= 18? I predict False.")
print(age <= 18)

print("\nIs age != 18? I predict True.")
print(age != 18)

#tes pakai keyword and operator

x = 10
y = 5

#tes menggunakan operator and
print(x > 5 and y < 10) 
print(x > 15 and y < 10)  

#tes menggunakan operator or
print(x > 5 or y < 10)
print(x > 15 or y < 10)

#tes apakah suata item ada di dalam list
my_list = ['apel', 'jeruk', 'pisang']
print('apel' in my_list)
print('mangga' in my_list)

#tes apakah suatu item tidak ada di dalam list
kamar = ['kasur', 'lemari', 'meja']
notinkamar = 'kursi'

print(notinkamar not in kamar)
print('kasur' not in kamar)

