#!/usr/bin/env python3

def grateDetection(data):
    """ GRATEDETECTION detects and displays the minimum and maximum values for
    the growth rate in data as a screen message. Also prompts an error message
    if there is no bacteria in that range. """

    # Usage: grateDetection(data)
    #
    # Input         data            N x 3 (matrix), where N is number of rows
    # Output        on screen       message, e.g. Data has bacteria growth..
    #                               error message, e.g. Please try again..
    #
    # Author: Karen Loaiza, s181423@student.dtu.dk, 2018

    while True:
        try:
            # Data has 3 columns: 0, 1, 2.
            # Extract growth column and calculate minimum and maximum values.
            min_Growth = min(data[:, 1])
            max_Growth = max(data[:, 1])
            # Messages:
            print("\n")
            print("Data has bacteria growth in range",
                  min_Growth, "<= Growth rate <=", max_Growth)
            break
        except ValueError:
            print("\n")
            print("Please try filters again.")
            print("Bacteria in data don't grow in that range.")
            break
