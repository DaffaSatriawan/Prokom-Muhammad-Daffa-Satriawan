import json
from pathlib import Path


def get_stored_username(path):
  """Mendapatkan username yang tersimpan jika file ada."""
  if path.exists():
    contents = path.read_text(encoding="utf-8")
    return json.loads(contents)
  return None


def get_new_username(path):
  """Meminta input username baru dan menyimpannya ke dalam file."""
  username = input("Masukkan nama Anda: ")
  contents = json.dumps(username)
  path.write_text(contents, encoding="utf-8")
  return username


def greet_user():
  """Menyapa pengguna dengan memverifikasi identitasnya terlebih dahulu."""
  path = Path("username.json")
  username = get_stored_username(path)

  if username:
    # Meminta konfirmasi apakah username yang tersimpan sudah benar
    correct = input(f"Apakah Anda adalah {username}? (y/n): ")
    if correct.lower() == "y":
      print(f"Selamat datang kembali, {username}!")
    else:
      username = get_new_username(path)
      print(f"Kami akan mengingat Anda saat kembali nanti, {username}!")
  else:
    username = get_new_username(path)
    print(f"Kami akan mengingat Anda saat kembali nanti, {username}!")


print("--- Program Verify User (Exercise 10-14) ---")
greet_user()