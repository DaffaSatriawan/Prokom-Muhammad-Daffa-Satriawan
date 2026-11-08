from random import randint


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

#bermata 6 melempar 10 kali
print("===Lempar 6 sisi 10 kali")
d6 = Die(6)
for i in range(10):
    d6.roll_die()

#bermata 10 melempar 10 kali
print("===Lempar 6 sisi 10 kali")
d10 = Die(10)
for i in range(10):
    d10.roll_die()

#bermata 6 melempar 10 kali
print("===Lempar 20 sisi 10 kali")
d20 = Die(20)
for i in range(10):
    d20.roll_die()