from Bab9_Lat12User import User

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
