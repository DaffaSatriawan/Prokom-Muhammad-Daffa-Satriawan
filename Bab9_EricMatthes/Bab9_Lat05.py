#class user
class User:
    def __init__(self, first_name, last_name, age_user
    , color_fav):
        self.first_name = first_name
        self.last_name = last_name
        self.age_user = age_user
        self.color_user = color_fav
        self.login_attempts = 0

    def describe_user (self):
        print(f"Hello {self.first_name}")
        print(f"Your Last name is {self.last_name}")
        print(f"Your age is {self.age_user}")
        print(f"Your favorit color is {self.color_user}")

    def greet_user (self):
        print(f"{self.first_name} Are you want to login in? ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts (self):
        self.login_attempts = 0
        print(f"login attempts is {self.login_attempts}")

        


user1 = User ('miu', 'mia', 80, 'blue')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"login attempt is {user1.login_attempts} ")
user1.reset_login_attempts()
print(f"jumlah percobaan logi setelah di reset: {user1.login_attempts}")