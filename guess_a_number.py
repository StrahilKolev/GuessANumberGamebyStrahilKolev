import random

computer_number = random.randint(1, 100)

while True:
    print("Guess the number (1 to 100): ")
    player_number = input()
    if not player_number.isdigit():
        print("Invalid input! Try again... ")
        continue
    player_number = int(player_number)

    if player_number == computer_number:
        print("You are right!!!")
        break

    elif player_number > computer_number:
        print("Too high!")

    else:
        print("Too low!")
