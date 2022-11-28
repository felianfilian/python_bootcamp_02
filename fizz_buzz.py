def fizz_buzz():
    print("fizz buzz")
    # count numbers
    # every 3 is a fizz, every 5 is a buzz and both together is fizzbuzz
    for number in range(1, 21):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
