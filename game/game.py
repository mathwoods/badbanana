import random
import sys

from game import happyface, sadface, banana


def _show_status(score : int, lives : int) -> None:
    assert score >= 0 and lives >= 0, "Score and lives must be non-negative integers."
    print(f"Current score: {score}")
    print(f"Lives left: {lives}")
    

def play() -> None:
    lives = 3
    score = 0

    print("\nWELCOME TO BAD BANANA!\n")
    name = input("What's your name? ")
    print(f"\nHi {name}!\n")
   
    print("From which to which whole numbers you would like to multiply?")
    while True:
        try:
             min_int = int(input("From: "))
             max_int = int(input("To: "))
        except ValueError:
            print(f"Input values must be is not a whole number. Try again :-).")
            continue
        if max_int < 0 or min_int < 0:
            print("Positive integers only please. Try again :-).")
            continue
        if min_int >= max_int:
            print("Your second number must be bigger than your first! Try again :-).")
            continue
        break
    print("\nOk then :-)!\n")

    print(f"Try to multiply whole numbers between {min_int} and {max_int}.")
    print("Get a question right, get one point.")
    print("Get a question wrong, lose a life.")
    print("Lose three lives and you're a BAD BANANA :-p!")
    print("Type q at a question if you want to quit.\n")
    _show_status(score, lives)

    while True:
        x = random.randint(min_int, max_int)
        y = random.randint(min_int, max_int)

        while True:
            ans = input(f"\nWhat is {x} * {y}? ")
            if ans == 'q':
                print ("\nThanks for playing Bad Banana. See you next time :-D!\n")
                sys.exit()
            try:
                ans = int(ans)
            except ValueError:
                print(f"{ans}' is not a whole number. Try again :-).")
                continue
            break

        right_answer = x * y
        if ans == right_answer:
            score = score + 1
            print(happyface)
            print("\nAwesome stuff!!!")
        else:
            lives = lives - 1
            if lives == 0:
                print(banana, '\n')
                print("Ahhh!!! You lost all your lives! You're a BAD BANANA!!!")
                print("Better luck next time :-P!\n")
                sys.exit(0)
            else:
                print(sadface)
                print("\nAck!! Wrong answer!")

        _show_status(score, lives)
