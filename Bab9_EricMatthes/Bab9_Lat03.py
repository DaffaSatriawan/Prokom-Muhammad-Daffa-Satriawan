#class user
class User:
    def __init__(self, first_name, last_name, age_user
    , color_fav):
        self.first_name = first_name
        self.last_name = last_name
        self.age_user = age_user
        self.color_user = color_fav

    def describe_user (self):
        print(f"Hello {self.first_name}")
        print(f"Your Last name is {self.last_name}")
        print(f"Your age is {self.age_user}")
        print(f"Your favorit color is {self.color_user}")

    def greet_user (self):
        print(f"{self.first_name} Are you want to login in? ")

user1 = User ('Aan', 'ghani', 80, 'blue')
user2 = User ('kayla', 'hani', 90,'pink')
users = [user1, user2]

for user in users:
    user.describe_user()
    user.greet_user()
    print("================================")