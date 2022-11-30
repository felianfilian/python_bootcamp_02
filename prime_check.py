def check_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        print("its a PRIME")
    else:
        print("its NOT a prime")

def start():
    print("prime number checker")
    number = int(input("check this number:\n"))
    check_prime(number)
