#!/usr/bin/env python3

import numpy as np


def bDetection(data):
    """ bDetection counts the number of bacteria type (1, 2, 3, 4) ocurrences
    in a list. """

    # Usage: bDectection(data)
    #
    # Input         data            N x M (matrix), where N is number of rows
    # Output        on screen       message, e.g. Data contains 11 Listeria
    #
    # Author: Karen Loaiza, s181423@student.dtu.dk, 2018

    # Create an array of custom bacteria names.
    b_name = np.array(["Salmonella enterica.",
                       "Bacillus cereus.",
                       "Listeria.",
                       "Brochothrix thermosphacta."])
    # Data has 3 columns: 0, 1, 2.
    # Extract the bacteria column as an array and convert it to a list.
    b_list = list(map(int, data[:, 2]))
    # Count the bacteria type ocurrences and print a message with the
    # bacteria's name.
    for i in range(len(b_name)):
        count = b_list.count(i+1)
        if count > 0:
            print("Data contains", count, b_name[i])
