print("--- Program Penjumlahan Dua Angka (Exercise 10-6) ---")

first_number = input("Masukkan angka pertama: ")
second_number = input("Masukkan angka kedua: ")

try:
  num1 = int(first_number)
  num2 = int(second_number)
  
except ValueError:
  print("\nError: Harap masukkan angka yang valid, bukan teks!")

else:
  total = num1 + num2
  print(f"\nHasil penjumlahan {num1} + {num2} adalah: {total}")