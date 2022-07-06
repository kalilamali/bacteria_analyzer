#!/usr/bin/env python3

import numpy as np


def dataLoad(filename):
    """ DATALOAD reads data from filename, propmts errors, and returns error
    free data matrix. """

    # Usage: data =  dataLoad(filename)
    #
    # Input         filename        name of file (string), e.g. "test.txt"
    # Output        data            N x 3 (matrix), where N is number of rows
    #               on screen       error messages
    #
    # Author: Karen Loaiza, s181423@student.dtu.dk, 2018

    # Load the file as a matrix of 3 columns.
    matrix = np.loadtxt(filename, usecols=range(3))
    for i in range(len(matrix)):
        # If the condition is not met, the value in matrix is an error:
        # Convert the error to nan value and display an error message.

        if matrix[i, 0] < 10:
            print("Row", i, "with value < 10. "
                  "Error: Temperature must be a number between 10 and 60.")
            matrix[i, 0] = np.nan

        if matrix[i, 0] > 60:
            print("Row", i, "with value > 60. "
                  "Error: Temperature must be a number between 10 and 60.")
            matrix[i, 0] = np.nan

        if matrix[i, 1] < 0:
            print("Row", i, "with value < 0. "
                  "Error: Growth rate must be a positive number.")
            matrix[i, 1] = np.nan

        if (matrix[i, 2] != 1) and (
                matrix[i, 2] != 2) and (
                        matrix[i, 2] != 3) and (
                                matrix[i, 2] != 4):
            print("Row", i, "with invalid value. "
                  "Error: Bacteria type must be 1, 2, 3, or 4.")
            matrix[i, 2] = np.nan

    # Create an error free data matrix without nan values.
    data = matrix[~np.isnan(matrix).any(axis=1)]
    return data
