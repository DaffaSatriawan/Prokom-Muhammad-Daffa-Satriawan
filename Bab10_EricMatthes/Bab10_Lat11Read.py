import json
from pathlib import Path

# Tentukan path file json yang sama
path = Path("favorite_number.json")

try:
  # Membaca isi file teks
  contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
  print("File penyimpanan tidak ditemukan.")
else:
  # Menggunakan json.loads() untuk membaca data kembali
  favorite_number = json.loads(contents)
  print(f"I know your favorite number! It’s {favorite_number}")