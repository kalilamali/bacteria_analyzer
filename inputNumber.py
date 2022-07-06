#!/usr/bin/env python3

def inputNumber(prompt):
    """ INPUTNUMBER Prompts user to input a number. """

    # Usage: num = inputNumber(prompt)
    #
    # Displays prompt and asks user to input a number
    # Repeats until user inputs a valid number
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    # Modified by Karen Loaiza, s181423@student.dtu.dk, 2018

    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Please enter a number. TIP: See the menu options.")
            pass
    return num
