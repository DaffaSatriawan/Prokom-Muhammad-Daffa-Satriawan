from pathlib import Path

# Daftar file yang ingin dibaca langsung menggunakan namanya saja
filenames = [Path("cats.txt"), Path("dogs.txt"), Path("rabbits.txt")]

print("--- Program Silent Cats and Dogs (Exercise 10-9) ---\n")

for path in filenames:
  try:
    contents = path.read_text(encoding="utf-8")
  except FileNotFoundError:
    # Mengabaikan error secara diam-diam menggunakan pass
    pass
  else:
    print(f"--- Isi dari {path.name} ---")
    print(contents.strip())
    print()