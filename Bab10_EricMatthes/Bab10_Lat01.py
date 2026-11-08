from pathlib import Path

# Menentukan path file menggunakan pathlib
path = Path("learning_python.txt")

# 1. Membaca seluruh isi file sekaligus
print("--- 1. Membaca Seluruh File ---")
contents = path.read_text()
print(contents.strip())

# 2. Membaca baris demi baris menggunakan loop dari splitlines()
print("--- 2. Membaca Baris demi Baris ---")
for line in path.read_text().splitlines():
  print(line)


# 3. Menyimpan baris-baris file ke dalam list
print("--- 3. Menyimpan ke dalam List ---")
lines = path.read_text().splitlines()
for line in lines:
  print(line)