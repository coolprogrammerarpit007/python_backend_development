username = input("Enter Username: ")
password = input("Enter Password: ")

password_length = len(password)
print(f"Your username is {username}, and your password {password_length * '*' } length is {password_length}")