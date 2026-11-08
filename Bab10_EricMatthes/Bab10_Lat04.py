#Guest
from pathlib import Path

path = Path('guest.txt')

#program
guest = input("please input your name: ")
print (guest)

path.write_text(guest)