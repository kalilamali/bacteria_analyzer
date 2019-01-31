import numpy as np


def dataStatistics(data, statistic):
    """ DATASTATISTICS calculates 1 out of 7 possible statistics for the data. """

    # Usage: result = dataStatistics(data, statistic)
    #
    # Input         data            N x 3 (matrix), where N is number of rows 
    #               statistic       to be calculated (string), e.g. "Rows"
    # Output        result          result of calculated statistic (scalar)
    #
    # Author: Karen Loaiza, s181423@student.dtu.dk, 2018

    # Sort the data by columns: 
    # (T) Temperature, (G) Growth rate, and (B) Bacteria.
    T = data[:,0]
    G = data [:,1]
    B = data [:,2]
    
    # Calculate the corresponding statistic on the sorted columns.
    if statistic == "Mean Temperature":  # Average T.
        result = np.mean(T)
    elif statistic == "Mean Growth rate":  # Average G.
        result = np.mean(G)
    elif statistic == "Std Temperature":  # Standard deviation of T.
        result = np.std(T)
    elif statistic == "Std Growth rate":  # Standard deviation of G.
        result = np.std(G)
    elif statistic == "Rows":  # Total number of rows in data.
        result = len(data)
    elif statistic == "Mean Cold Growth rate":  # Average G when T < 20 degrees.
        result = np.mean(T[T<20])
    elif statistic == "Mean Hot Growth rate":  # Average G when T > 50 degrees.
        result = np.mean(T[T>50])
    return result

