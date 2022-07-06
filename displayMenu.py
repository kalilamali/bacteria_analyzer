#!/usr/bin/env python3

import numpy as np
from inputNumber import inputNumber


def displayMenu(options):
    """ DISPLAYMENU Displays a menu of options, ask the user to choose an item,
    and returns the number of the menu item chosen. """

    # Usage: choice = displayMenu(options)
    #
    # Input         options             Menu options (array of strings)
    # Output        choice              Chosen option (integer)
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    # Modified by Karen Loaiza, s181423@student.dtu.dk, 2018

    # Display the menu options.
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    # Get a valid menu choice.
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    return choice
