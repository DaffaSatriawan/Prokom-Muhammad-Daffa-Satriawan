import json
from pathlib import Path

# Meminta input nomor favorit dari pengguna
favorite_number = input("Berapa nomor favorit Anda? ")

# Tentukan path file json
path = Path("favorite_number.json")

# Menggunakan json.dumps() untuk mengubah data menjadi string JSON, lalu simpan dengan write_text()
contents = json.dumps(favorite_number)
path.write_text(contents, encoding="utf-8")

print("Nomor favorit Anda telah disimpan!")