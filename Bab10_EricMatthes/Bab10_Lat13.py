import json
from pathlib import Path

# Tentukan path file penyimpanan
path = Path("user_profile.json")

print("--- Program Pendaftaran Profil Pengguna (Exercise 10-13) ---")

# Meminta beberapa informasi tambahan tentang pengguna
username = input("Masukkan nama pengguna: ")
age = input("Masukkan usia Anda: ")
hobby = input("Masukkan hobi utama Anda: ")

# Menyimpan seluruh informasi ke dalam sebuah dictionary
user_dict = {"username": username, "age": age, "hobby": hobby}

# Menulis dictionary ke file menggunakan json.dumps()
contents = json.dumps(user_dict)
path.write_text(contents, encoding="utf-8")
print("\nData profil berhasil disimpan ke file!")

# Membaca kembali data dari file menggunakan json.loads()
if path.exists():
  read_contents = path.read_text(encoding="utf-8")
  loaded_dict = json.loads(read_contents)

  # Mencetak ringkasan informasi yang diingat oleh program
  print("\n--- Ringkasan Profil yang Tersimpan ---")
  print(f"Nama Pengguna : {loaded_dict['username']}")
  print(f"Usia          : {loaded_dict['age']}")
  print(f"Hobi          : {loaded_dict['hobby']}")