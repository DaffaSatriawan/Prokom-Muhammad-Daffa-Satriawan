def build_profile(first, last, **user_info):
    """Membangun dictionary yang berisi segala hal yang kita ketahui tentang seorang pengguna."""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

# Memanggil fungsi dengan nama dan 3 pasang key-value tambahan
my_profile = build_profile(
    'Muhammad Daffa', 
    'Satriawan',
    location='Surakarta',
    field_of_study='Fine Arts',
    hobby='Painting'
)

# Menampilkan hasil profil
print(my_profile)