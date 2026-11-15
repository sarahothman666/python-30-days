import string
import secrets
characters = string.ascii_letters + string.digits + string.punctuation
while True:
    number_of_password = input("How many characters do you want? ")
    if not number_of_password.isdigit():
        print("Please enter numbers only.")
        continue
    number_of_password = int(number_of_password)
    if number_of_password < 6 or number_of_password > 20:
        print("Password length must be between 6 and 20.")
        continue
    password = ""
    for i in range(number_of_password):
        password += secrets.choice(characters)
    print("Your password is:", password)
    break