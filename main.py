import random

def guess_number():
    try:
        max = int(input("Enter the maximum number for the game: "))
        random_num = random.randint(1, max)
        while True:
            try:
                user_num = int(input(f"Enter your guess between 1 and {max}. To exit the game enter 0: "))
                if user_num == 0:
                    print("Thank you for playing!")
                    break
                elif user_num == random_num:
                    print("You guessed it right!")
                    break
                elif user_num > random_num:
                    print("Your guess is too high!")
                else:
                    print("Your guess is too low!")
            except ValueError:
                print("Please enter a valid integer!")
    except ValueError:
        print("Please enter a valid integer for the maximum number!")
guess_number()