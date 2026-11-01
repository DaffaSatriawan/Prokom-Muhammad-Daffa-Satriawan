#Dream vacation
responses = {}

polling_active = True

while polling_active:
    name = input("\nMasukkan nama Anda: ")
    response = input("Jika Anda bisa mengunjungi satu tempat di dunia, kemana Anda ingin pergi? ")

    # Simpan jawaban dalam dictionary
    responses[name] = response

    repeat = input("Apakah ada orang lain yang ingin menjawab? (ya/tidak) ")
    if repeat.lower() == 'tidak':
        polling_active = False

# Menampilkan hasil polling
print("\nHasil polling:")
for name, response in responses.items():
    print(f"{name} ingin mengunjungi {response}.")
