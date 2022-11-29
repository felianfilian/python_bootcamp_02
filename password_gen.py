import random

def password_gen():
    print("Password Generator")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_count = int(input("how many letters:\n"))
    numbers_count = int(input("how many numbers:\n"))
    symbol_count = int(input("how many symbols:\n"))

    password = []

    for sign in range (1, numbers_count + 1):
        password.append(random.choice(numbers))
    for sign in range(1, symbol_count + 1):
        password.append(random.choice(symbols))
    for sign in range(1, letter_count + 1):
        password.append(random.choice(letters))

    random.shuffle(password)
    pass_out = ""

    for char in password:
        pass_out += char

    print("Your Password:\n" + str(pass_out))