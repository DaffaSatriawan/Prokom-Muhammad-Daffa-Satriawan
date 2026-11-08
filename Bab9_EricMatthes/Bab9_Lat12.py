#main
from Bab9_Lat12ModuleAdmin import Admin

admin1 = Admin("iki", "santoso", 25, "male")

admin1.describe_user()
admin1.greet_user()

print(f"\nAdmin: {admin1.first_name.title()}")
admin1.privileges.show_privileges()