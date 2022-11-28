def even_numbers():
    print("even numbers")
    total = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total += number
    print(f"all even number total: {total}")
