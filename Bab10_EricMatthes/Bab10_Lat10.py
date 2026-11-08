from pathlib import Path

print("--- Program Common Words (Exercise 10-10) ---\n")

path = Path("alice.txt")

try:
  contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
  print(f"Maaf, file '{path.name}' tidak ditemukan.")
else:
  # Mengubah seluruh teks ke huruf kecil agar pencarian tidak bersifat case-sensitive
  lower_contents = contents.lower()

  # Menghitung kemunculan kata 'the' (termasuk yang menjadi bagian dari kata lain seperti 'then' atau 'there')
  count_the = lower_contents.count("the")

  # Menghitung kemunculan kata 'the ' (menggunakan spasi di belakang agar lebih akurat menghitung kata mandiri)
  count_the_space = lower_contents.count("the ")

  print(f"File yang dianalisis: {path.name}")
  print(f"Jumlah kemunculan 'the' (substring): {count_the}")
  print(f"Jumlah kemunculan 'the ' (persis kata): {count_the_space}")