alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def crypt(plain_text, shift_amount, type):
    cipher_text = ""
    shift_amount = shift_amount % len(alphabet)
    if type == 1:
        shift_amount *= -1
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(cipher_text)

def start():
    print("Caesar Cipher")
    print("Encode")
    text = input("message:\n").lower()
    shift = int(input("shift number:\n"))
    crypt(text, shift, 0)
    print("Decode")
    text = input("message:\n").lower()
    shift = int(input("shift number:\n"))
    crypt(text, shift, 1)