import random


def hangman():
    print("hangman")

    word_list = [
        "carmageddon",
        "braveheart",
        "crystalball",
        "gothic"
    ]

    pick_word = random.choice(word_list)

    empty_word = []
    lives = 6

    for char in pick_word:
        empty_word.append("_")

    while "_" in empty_word:
        # print(stages[lives])
        if lives <= 0:
            print("YOU LOOSE")
            break
        print(empty_word)
        print("LIVES: " + str(lives))
        letter = input("Guess a letter:\n").lower()
        if letter in empty_word:
            print(f"the letter {letter} is already in the word")
        else:
            for i in range(len(empty_word)):
                if letter in pick_word:
                    empty_word[i] = letter
            if not letter in empty_word:
                lives -= 1
                print("letter is not in the word")

    if not "_" in empty_word:
        print("YOU WON")
    print("finished")
