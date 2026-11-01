import random

#blok print
print ("============================================")
print (" SELAMAT DATANG DI GAME BATU GUNTING KERTAS ")
print ("============================================")

#daftar pilihan
pilihan_game = ["batu", "gunting", "kertas"]

#skor 
skor_pemain = 0
skor_komputer = 0

#looping keluar
while True:
    print(f"\n[ SKOR SEMENTARA ] Kamu: {skor_pemain} | Komputer: {skor_komputer}")
    pemain = input("\nPilih (batu, gunting, kertas) atau ketik 'keluar' untuk berhenti: ").lower()

    if pemain == "keluar":
        print ("terimakasih sudah bermain!")
        break

    #valid input
    if pemain not in pilihan_game:
        print("Pilihan tidak valid! Coba masukkan 'batu', 'gunting', atau 'kertas'.")
        continue

    #pilihan komputer
    komputer = random.choice(pilihan_game)
    print ("=========================================")
    print(f"Komputer memilih : {komputer}")
    print(f"Kamu memilih     : {pemain}")
    print ("=========================================")

    #menetukan menang kalah
    if pemain == komputer:
        print ("   Hasil:       SERI!!!")
    elif (pemain == "batu" and komputer == "gunting") or \
         (pemain == "gunting" and komputer == "kertas") or \
         (pemain == "kertas" and komputer == "batu"):
        print ("=========================================")
        print ("           SELAMAT! Kamu MENANG!         ")
        print ("=========================================")
        skor_pemain += 1

    else:
        print ("=========================================")
        print ("                MAAF KAMU KALAH          ")
        print ("=========================================")
        skor_komputer += 1

    #blok main lagi
    main_lagi = input("\nMau main lagi? (y/t): ").lower()

    if main_lagi != 'y':
        print("\n==========================================")
        print("          TERIMA KASIH SUDAH BERMAIN!     ")
        print(f"Skor Akhir -> Kamu: {skor_pemain} | Komputer: {skor_komputer}")
        print("==========================================")
        break


