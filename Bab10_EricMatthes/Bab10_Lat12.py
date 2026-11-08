import json
from pathlib import Path

# Tentukan path file penyimpanan
path = Path("favorite_number.json")

# Memeriksa apakah file sudah ada sebelumnya
if path.exists():
  contents = path.read_text(encoding="utf-8")
  favorite_number = json.loads(contents)
  print(f"I know your favorite number! It’s {favorite_number}")
else:
  # Jika belum ada, minta input dari pengguna
  favorite_number = input("Berapa nomor favorit Anda? ")
  contents = json.dumps(favorite_number)
  path.write_text(contents, encoding="utf-8")
  print("Nomor favorit Anda telah disimpan!")