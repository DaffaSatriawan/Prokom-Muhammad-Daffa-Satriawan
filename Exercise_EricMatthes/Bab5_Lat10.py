# checking usernames
current_users = ['aan', 'kayla', 'rizki', 'nayla', 'bjorcup']
new_users = ['aan', 'KAYLA', 'mia', 'none', 'kik', 'kis']

# list baru
current_user_lower = [user.lower() for user in current_users]

# loop
for newsu in new_users:
    if newsu.lower() in current_user_lower:
        print(f"maaf username '{newsu}' sudah digunakan, silahkan masukkan yang lain")
    else:
        print(f"username '{newsu}' tersedia")