#No Pastrami
sandwich_orders = [
'tuna', 'pastrami', 'ham', 'pastrami', 
'turkey', 'pastrami', 'veggie']
finished_sandwiches = []

#deli kehabisan pastrami
print("Maaf, kami kehabisan pastrami hari ini.")

#while
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#memproses sisa
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

#menampilkan semua
print("\nSemua sandwich yang telah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")