import random


def hangman():
    print("hangman")
    word_list = ["carmageddon", "braveheart", "crystalball"]
    pick_word = random.choice(word_list)

    empty_word = []
    lives = 3


    for char in pick_word:
        empty_word.append("_")

    while "_" in empty_word:
        letter = input("Guess a letter:\n").lower()
        for i in range(len(empty_word)):
            if letter == pick_word[i]:
                empty_word[i] = letter

        if not letter in empty_word:
            lives -= 1
        if lives <= 0:
            print("YOU LOOSE")
            break
        print(empty_word)
        print(lives)

    print("finished")
