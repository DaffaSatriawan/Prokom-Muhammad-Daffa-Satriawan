#pizza toppings
prompt = "\nMasukkan topping pizza yang anda inginkan: "
prompt += "\n(Ketik 'quit' untuk keluar dari program) "

while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        print("\nTerima kasih! Pesanan pizza kamu sedang disiapkan.")
        break
    else:
        print(f"topping pizza yang anda pilih adalah {topping.title()}")
        print("=======================================================")