from pathlib import Path

# Daftar file path yang ingin dibaca (sengaja kita selipkan file yang tidak ada)
filenames = [
    Path("cats.txt"),
    Path("dogs.txt"),
    Path("rabbits.txt")
]
print("--- Program Cats and Dogs (Exercise 10-8) ---\n")

for path in filenames:
  try:
    contents = path.read_text(encoding="utf-8")
  except FileNotFoundError:
    print(f"[Error] Maaf, file '{path.name}' tidak ditemukan.")
  else:
    print(f"--- Isi dari {path.name} ---")
    print(contents.strip())
    print()