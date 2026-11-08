class User:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(
            f"User: {self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}"
        )

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")


class Privileges:

    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can reset password",
        ]

    def show_privileges(self):
        print("Daftar Hak akses untuk admin adalah:")
        for privilege in self.privileges:
            print(f" - {privilege}")


class Admin(User):

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
