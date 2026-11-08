from random import sample

# list
bingo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e"]

my_tickets = [4, "d", 2, "e"]

# loop
plays = 0
won = False

while not won:
    drawn = sample(bingo, k=4)
    plays += 1

    if drawn == my_tickets:
        won = True

print(f"Selesai! Tiket kamu ({my_tickets}) berhasil menang.")
print(f"Total percobaan yang dibutuhkan sampai menang adalah: {plays} kali undian.")