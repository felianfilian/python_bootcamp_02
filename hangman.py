import random


def hangman():
    print("hangman")
    word_list = ["carmageddon", "braveheart", "crystalball"]
    pick_word = random.choice(word_list)

    empty_word = ""

    for char in pick_word:
        empty_word += "_"

    letter = input("Guess a letter").lower()

    for char in pick_word:
        if char == letter:
            print("right")


    print(empty_word)