import random



secret_number = random.randint(1, 100)
attempts = 0
while True:
    choosen_number = int(input("Please young one enter the number think: "))
    attempts += 1
    if choosen_number > secret_number:
        print("too high")
    elif choosen_number < secret_number:
        print("too low")
    else:
        print(f"you got it in {attempts}")
        break
