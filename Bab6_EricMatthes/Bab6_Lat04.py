#glossary
# Membuat dictionary glosarium berisi 5 istilah pemrograman
glossary = {
    'dictionary': 'Struktur data di Python yang menyimpan data dalam pasangan key-value.',
    'string': 'Deretan karakter yang diapit oleh tanda petik.',
    'loop': 'Blok kode yang digunakan untuk menjalankan perulangan secara berulang-ulang.',
    'list': 'Kumpulan item yang disimpan secara berurutan dalam satu variabel.',
    'comment': 'Catatan dalam kode yang diabaikan oleh Python dan diawali dengan tanda pagar (#).'
}

#loop
for word, meaning in glossary.items():
    print(f"\n{word.title()}:\n{meaning}")