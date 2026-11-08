from random import choices

#list
bingo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 
"a", "b", "c", "d", "e"]

winning_ticket = choices(bingo, k=4)

#print
print("=============================")
print(f"bingo ticket kamu adalah {winning_ticket}")
print("Notes: tiket yang cocok dengan 4 angka/huruf menang")