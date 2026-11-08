from pathlib import Path

# Menentukan path file menggunakan pathlib
path = Path("Bab10_ExerciseEricMatthes/learning_python.txt")

print("--- Exercise 10-2: Learning C ---")

# Membaca file baris demi baris dan memodifikasinya
for line in path.read_text().splitlines():
  # Mengganti kata 'Python' dengan 'C'
  modified_line = line.replace("Python", "C")
  print(modified_line)