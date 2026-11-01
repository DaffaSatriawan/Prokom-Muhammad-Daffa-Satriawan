#styling function

"""Program untuk menampilkan buku favorit menggunakan fungsi."""

#Bab 8 - Latihan 2
def favorite_book(title):
    """Mencetak pesan tentang buku favorit."""
    print(f"One of my favorite books is {title}.")


# Memanggil fungsi
favorite_book("Alice in Wonderland")

#Bab 8 - Latihan 4
"""Program untuk membuat pesanan kaos dengan ukuran dan teks tertentu."""


def make_shirt(size='large', message='I love Python'):
    """Merangkum ukuran kaos dan pesan yang tercetak di atasnya."""
    print(f"Membuat kaos ukuran {size.title()} dengan tulisan: '{message}'")


# Memanggil fungsi menggunakan berbagai kombinasi argumen
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='Keep Coding!')

#Bab 8 - Latihan 14
"""Program untuk menyimpan informasi detail mobil ke dalam dictionary."""


def make_car(manufacturer, model, **car_info):
    """Membangun dictionary yang berisi informasi lengkap tentang sebuah mobil."""
    car_info['manufacturer'] = manufacturer.title()
    car_info['model'] = model.title()
    return car_info


# Memanggil fungsi dengan parameter wajib dan tambahan keyword arguments
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Menampilkan hasil
print(car)
