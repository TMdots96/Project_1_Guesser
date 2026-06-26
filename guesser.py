import random



secret_number = random.randint(1, 100)
attempts = 0
while True:
    try:
        choosen_number = int(input("Please young one enter secret number: "))
    except ValueError:
        print("Please enter a number dip shit")
        continue
    attempts += 1
    if choosen_number > secret_number:
        print("too high")
    elif choosen_number < secret_number:
        print("too low")
    else:
        print(f"you got it in {attempts}")
        break
