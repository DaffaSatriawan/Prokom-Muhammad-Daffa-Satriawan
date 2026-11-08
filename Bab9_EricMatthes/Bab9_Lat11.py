from Bab9_Lat11Module import Admin

admin1 = Admin("iki", "santoso", 25, "black")

admin1.describe_user()
admin1.greet_user()

print(f"\nAdmin: {admin1.first_name.title()}")
admin1.privileges.show_privileges()

