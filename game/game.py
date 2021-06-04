from .draw import draw_banana, draw_happyface, draw_sadface

def print_score(score):
    print("Current score: %s" % score)


def print_lives(lives):
    print("Lives left: %s" % lives)


def ask_range():
    print("From which to which whole numbers you would like to multiply?")

    while True:
        val_1 = input("From: ")

        try:
            val_1 = int(val_1)
        except ValueError:
            print("'%s' is not a whole number. Try again :-)." % val_1)
            continue

        if val_1 < 0:
            print("Positive integers only please. Try again :-).")
            continue

        break

    while True:
        val_2 = input("To: ")

        try:
            val_2 = int(val_2)
        except ValueError:
            print("'%s' is not a whole number. Try again :-)." % val_2)
            continue

        if val_2 < 0:
            print("Positive integers only please. Try again :-).")
            continue

        if val_1 >= val_2:
            print("Your second number must be bigger than or equal to"
                    + "your first! Try again :-).")
            continue

        break

    return (val_1, val_2)

#MAIN PROGRAM
#===============================================================================
import random
import sys

def run() -> None:
    lives = 3
    score = 0

    print("\nWELCOME TO BAD BANANA!\n")

    name = input("What's your name? ")

    print("\nHi " + name + "!\n")

    tuple_int = ask_range()
    min_int, max_int  = tuple_int[0], tuple_int[1]

    print("\nOk then :-)!\n")
    print("Try to multiply whole numbers between %s and %s." % (min_int, max_int))
    print("To play, just answer the following questions.")
    print("If you get a question right, you get one point.")
    print("If you get a question wrong, you lose a life.")
    print("Lose three lives and you're a BAD BANANA :-p!")
    print("Type q at a question if you want to quit.\n")

    print_score(score)
    print_lives(lives)

    while True:
        x = random.randint(min_int, max_int)
        y = random.randint(min_int, max_int)

        while True:
            ans = input("\nWhat is %s*%s? " % (x,y))

            if ans == 'q':
                print ("\nThanks for playing Bad Banana. See you next time"
                    + " :-D!\n")
                sys.exit(0)

            try:
                ans = int(ans)
            except ValueError:
                print("'%s' is not a whole number. Try again :-)." % ans)
                continue

            break

        right_answer = x * y

        if ans == right_answer:
            score = score + 1

            draw_happyface()
            print("\nAwesome stuff!!!")


        else:
            lives = lives - 1

            if lives == 0:
                draw_banana()
                print("Ahhh!!! You lost all your lives! You're a BAD BANANA!!!")
                print("Better luck next time :-P!\n")
                sys.exit(0)

            draw_sadface()
            print("\nAck!! Wrong answer!")

        print_score(score)
        print_lives(lives)
