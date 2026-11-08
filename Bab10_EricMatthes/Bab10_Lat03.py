from pathlib import Path

path = Path("learning_python.txt")

# Tanpa variabel sementara 'lines', langsung loop dari .splitlines()
for line in path.read_text().splitlines():
  print(line)