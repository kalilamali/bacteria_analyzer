import matplotlib.pyplot as plt
import numpy as np


def dataPlot(data):
    """ DATAPLOT displays 2 plots from data. """

    # Usage: dataPlot(data)
    #
    # Input         data            N x 3 (matrix), where N is number of rows
    # Output        on screen       Number of bacteria (1 bar plot)
    #                               Growth rate by temperature (1 scatter plot)
    #
    # Author: Karen Loaiza, s181423@student.dtu.dk, 2018
                          
    # Create arrays of custom colors and labels for each bacteria.
    colors = np.array(['#800080', '#3D59AB', '#8FBC8F', '#FFD700'])
    bacteria = np.array(['S. enterica', 
                         'B. cereus', 
                         'Listeria', 
                         'B. thermosphacta'])

    
    # Number of bacteria(1 bar plot).

    # Data has 3 columns: 0, 1, 2. 
    # Extract the bacteria column as an array and convert it to a list.
    b_list = list(map(int, data[:, 2]))
    # Count the bacteria type ocurrences in a list.
    freq_b1 = b_list.count(1)
    freq_b2 = b_list.count(2)
    freq_b3 = b_list.count(3)
    freq_b4 = b_list.count(4)
    # Plot.
    # plt.bar(bacteria type, frequency, bar width, color, x-label/x-tick)
    bar1 = plt.bar(1, freq_b1, width=0.8, color = colors[0], tick_label = 1)
    bar2 = plt.bar(2, freq_b2, width=0.8, color = colors[1], tick_label = 2)
    bar3 = plt.bar(3, freq_b3, width=0.8, color = colors[2], tick_label = 3)
    bar4 = plt.bar(4, freq_b4, width=0.8, color = colors[3], tick_label = 4)
    # Create custom legends.
    plt.legend((bar1[0], bar2[0], bar3[0], bar4[0]), (bacteria),
               loc = 'upper left')
    plt.title('Number of bacteria')
    plt.xlabel("Bacteria types")
    plt.ylabel("Frequency")
    ind = np.arange(5) 
    plt.xticks(ind,('', '1', '2', '3', '4'))
    plt.show()


    # Growth rate by temperature(1 scatter plot).

    # Filter all the data by bacteria type(1, 2, 3, 4).
    B1 = data[data[:, 2] == 1]
    B2 = data[data[:, 2] == 2]
    B3 = data[data[:, 2] == 3]
    B4 = data[data[:, 2] == 4]
    # Transpose all the data for plotting.
    x1,y1,z1 = B1.T
    x2,y2,z2 = B2.T
    x3,y3,z3 = B3.T
    x4,y4,z4 = B4.T
    # Plot.
    # plt.scatter(temperature, growth rate, dot size, color, star shape, 
    # bacteria name)
    plt.scatter(x1, y1, s = 50, c = colors[0], marker = (5, 1),
                label = bacteria[0])
    plt.scatter(x2, y2, s = 50, c = colors[1], marker = (5, 1), 
                label = bacteria[1])
    plt.scatter(x3, y3, s = 50, c = colors[2], marker = (5, 1), 
                label = bacteria[2])
    plt.scatter(x4, y4, s = 50, c = colors[3], marker = (5, 1), 
                label = bacteria[3])
    # Create custom legends.
    plt.legend(loc = 'upper left')
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.axis([10, 60, 0, 1])
    plt.show()
    