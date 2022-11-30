import random

import hangman_words
import hangman_art

def hangman():
    print("hangman")
    print(hangman_art.logo)

    pick_word = random.choice(hangman_words.word_list)

    empty_word = []
    lives = 6
    gameover = False

    for _ in range(len(pick_word)):
        empty_word.append("_")

    while not gameover:
        print(hangman_art.stages[lives])
        print(empty_word)
        print("LIVES: " + str(lives))
        letter = input("Guess a letter:\n").lower()
        if letter in empty_word:
            print(f"the letter {letter} is already checked")
        else:
            for i in range(len(empty_word)):
                if letter == pick_word[i]:
                    empty_word[i] = letter
        if not letter in empty_word:
            lives -= 1
            print("letter is not in the word")
        if lives <= 0:
            print("YOU LOOSE")
            print(hangman_art.stages[lives])
            gameover = True
        if not "_" in empty_word:
            print("YOU WON")
            gameover = True

    print("finished")
