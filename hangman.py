import random


def hangman():
    print("hangman")

    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

    word_list = ["carmageddon", "braveheart", "crystalball"]
    pick_word = random.choice(word_list)

    empty_word = []
    lives = 6

    for char in pick_word:
        empty_word.append("_")

    while "_" in empty_word:
        print(stages[lives])
        if lives <= 0:
            print("YOU LOOSE")
            break
        print(empty_word)
        print("LIVES: " + str(lives))
        letter = input("Guess a letter:\n").lower()
        for i in range(len(empty_word)):
            if letter == pick_word[i]:
                empty_word[i] = letter
        if not letter in empty_word:
            lives -= 1

    if not "_" in empty_word:
        print("YOU WON")
    print("finished")
