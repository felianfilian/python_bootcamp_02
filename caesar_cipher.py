alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

def start():
    print("Caesar Cipher")
    print("Encode")
    text = input("message:\n").lower()
    shift = int(input("shift number:\n"))
    encrypt(text, shift)
    print("Decode")
    text = input("message:\n").lower()
    shift = int(input("shift number:\n"))
    decrypt(text, shift)