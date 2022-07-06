#!/usr/bin/env python3

""" MAIN SCRIPT runs program for bacteria analysis. """

# 1 package
import numpy as np
# 6 files
from displayMenu import displayMenu
from dataLoad import dataLoad
from dataStatistics import dataStatistics
from dataPlot import dataPlot
from bDetection import bDetection
from grateDetection import grateDetection


# Main menu greeting
print("Welcome to the program for bacteria analysis.")
print("Below you can see the Main Menu.")
while True:
    print("\n")
    main_Menu = np.array(["Load data",
                          "Filter data",
                          "Display statistics",
                          "Generate plots",
                          "Quit"])
    main_choice = displayMenu(main_Menu)

    # 1. Load data.
    if main_choice == 1:
        while True:
            try:
                filename = input("Please enter filename: ")
                print("\n")
                e_freedata = dataLoad(filename.lower())
                data = e_freedata
                break
            except IOError:
                print("IOError: file not found in path.")
                print("Please check filename is correct.")
                print("TIP: Don't forget to add '.txt' at the end.")
                pass

    # 2. Filter data.
    elif main_choice == 2:
        print("\n")
        filter_menu = np.array(["Filter by bacteria type",
                                "Range filter for growth rate",
                                "Disable all filters",
                                "Back to main menu"])
        filter_choice = displayMenu(filter_menu)

        # 2.1. Filter by bacteria type.
        if filter_choice == 1:
            while True:
                try:
                    print("\n")
                    data = e_freedata
                    bacteria_menu = np.array(["Salmonella enterica",
                                              "Bacillus cereus",
                                              "Listeria",
                                              "Brochothrix thermosphacta",
                                              "Back to main menu"])
                    bacteria_choice = displayMenu(bacteria_menu)
                    if bacteria_choice in (1, 2, 3, 4):
                        data = data[data[:, 2] == bacteria_choice]
                        bDetection(data)
                        break
                    # 2.5. Back to main menu.
                    if bacteria_choice == 5:
                        break
                except NameError:
                    print("NameError: filename not defined.")
                    print("TIP: Don't forget to load data.")
                    break
                    pass
                continue

        # 2.2. Range filter by growth rate.
        if filter_choice == 2:
            while True:
                try:
                    data = e_freedata
                    min_Growth = min(data[:, 1])
                    max_Growth = max(data[:, 1])

                    # Detailed instructions for 2.2.
                    print("\n")
                    print("E.g. 0.5 ≤ Growth rate ≤ 1.")
                    print("In example left condition is: 0.5",
                          "and right condition: is 1.")
                    print("For your file", filename, ":")
                    grateDetection(data)

                    # Ask the user for input to set the onditions.

                    # Lower threshold.
                    left_c = float(input("Please enter left condition: "))
                    if left_c < min_Growth:
                        print("TIP: your condition < minimum growth rate.")
                        print(left_c, "<", min_Growth)
                    data = data[data[:, 1] > left_c]

                    # Higher threshold,
                    right_c = float(input("Please enter right condition:"))
                    if right_c > max_Growth:
                        print("TIP: your condition > maximum growth rate.")
                        print(right_c, ">", max_Growth)
                    data = data[data[:, 1] < right_c]
                    break
                except ValueError:
                    print("ValueError: condition invalid.")
                    print("TIP: Look at the example again.")
                except NameError:
                    print("NameError: filename not defined.")
                    print("TIP: Don't forget to load data.")
                    break
                    pass
                continue
            grateDetection(data)

        # 2.3. Disable all filters.
        if filter_choice == 3:
            data = e_freedata
            bDetection(data)
            grateDetection(data)

        # 2.4. Back to main menu.
        if filter_choice == 4:
            pass
        continue

    # 3. Display statistics.
    elif main_choice == 3:
        while True:
            try:
                statistic_menu = np.array(["Mean Temperature",
                                           "Mean Growth rate",
                                           "Std Temperature",
                                           "Std Growth rate",
                                           "Rows",
                                           "Mean Cold Growth rate",
                                           "Mean Hot Growth rate",
                                           "Back to main menu"])
                statistic_choice = displayMenu(statistic_menu)
                if statistic_choice in (1, 2, 3, 4, 5, 6, 7):
                    bDetection(data)
                    grateDetection(data)
                    statistic = statistic_menu[statistic_choice-1]
                    print(statistic, "is :", dataStatistics(data, statistic))
                    print("\n")
                # 3.8. Back to main menu.
                if statistic_choice == 8:
                    break
            except NameError:
                print("NameError: filename not defined.")
                print("TIP: Don't forget to load data.")
                break
                pass
            continue

    # 4. Generate plots.
    elif main_choice == 4:
        while True:
            try:
                bDetection(data)
                grateDetection(data)
                dataPlot(data)
                break
            except NameError:
                print("NameError: filename not defined.")
                print("TIP: Don't forget to load data.")
                break
                pass
            continue

    # 5. Exit program.
    elif main_choice == 5:
        # Goodbye.
        print("\nThank you for using the program for bacteria analysis.")
        break
