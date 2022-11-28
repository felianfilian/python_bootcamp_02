
def high_score():
    print("high score")
    scores = [41, 78, 56, 68, 33]
    highscore = 0
    for score in scores:
        if score > highscore:
            highscore = score
    print(f"The highscore is: {highscore}")