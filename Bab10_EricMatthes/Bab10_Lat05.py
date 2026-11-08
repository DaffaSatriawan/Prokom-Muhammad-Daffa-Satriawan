from pathlib import Path

path = Path('guest_book.txt')

names = []

while True:
    name = input("masuka nama anda (ketik quit): ")

    if name.lower() == "quit":
        break

    print(f"Selamat datang, {name}")
    names.append(name)

file_contents = "\n".join(names) + "\n"

path.write_text(file_contents)