#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which makes you guess a number.

import random


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    print("I am thinking of a number...")
    print(color.BOLD + color.GREEN + 'HINT: Its a number between 1-9!' +
          color.END)
    print("")

    while True:

        guessed_number_as_string = input(color.BOLD + color.YELLOW + 'Input' +
                                         ' your guess: ' + color.END)
        answer = random.randint(1, 8+1)

        try:
            guessed_number = int(guessed_number_as_string)

            if guessed_number > 0 and guessed_number < 10:
                if guessed_number == answer:
                    print("")
                    print("You did it, you won!")
                    break
                else:
                    print(color.BOLD + color.RED + 'Wrong, try again.'
                          + color.END + color.BOLD +
                          ' (It was {0}!)'.format(answer) + color.END)
                    print("")
            else:
                print('')
                print(color.PURPLE + color.UNDERLINE + 'Between 1-9 IDIOT!' +
                      ' Please re-input your guess...' + color.END)
                print("")
                print("")

        # This stops them from putting in something let bob and gets them to
        # re-input their age.
        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE +
                  'That is not a valid number.' +
                  ' Please re-input your guess...' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
