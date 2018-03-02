#! /usr/bin/python

"""
This is the help function that is used to generate the basic information of the Pandas DataFrame. This function doesn't return anything, but print out
some basic information of the dataset.

Author: Charlie Dang
Date: March/01/2018

"""
import numpy as np
import pandas as pd

def get_info(Dataframe):
    """
    This function will generate a basic information of the Dataframe

    Parameters
    -----------
    Dataframe: A pandas DataFrame

    Returns
    -------
    None

    Print
    -----
    information
    """
    if not isinstance(Dataframe, pd.core.frame.DataFrame):
        raise Examption("Error Format! The input datatype must be Pandas' DataFrame!!")

    print ("The Dataset has %s columns, and %s observations." %(Dataframe.shape[1], Dataframe.shape[0]))
    print ("------------------------------------------------")
    print ("\n")
    print ("The features of the DataFrame are: ", Dataframe.columns.values)


def list_null(Dataframe):
    """
    This function will list the null information of the DataFrame.

    Parameters
    ----------
    Dataframe: A pandas Dataframe

    Returns
    -------
    None

    Print
    -----
    Information
    """
    if not isinstance(Dataframe, pd.core.frame.DataFrame):
        raise Examption("Error Format! The input datatype must be Pandas' DataFrame!!")

    print (Dataframe.shape[1],' columns: ')
    for i in Dataframe.columns.values:
        print (i, ": nan", Dataframe[i].isnull().sum(), ', ', Dataframe[i].dtypes)


def Pearson(X, Y):
    """
    This function calculate the Pearson correlation function. Here we use the unbiased version.
    The description of the coefficient could be refered here: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

    Parameters:
    -----------
    X: A numpy array, which has the dimension the same as the number of observations
    Y: A numpy array, which has the dimension the same as the number of observations
    len(X) == len(Y)

    Returns:
    --------
    float number, unbiased Pearson correlation number

    """
    if (len(X) != len(Y)):
        raise Exception("Cannot calculate the coefficient in this case. Please make sure len(X) == len(Y)!")

    ## convert list or np.array to numpy array
    X = np.array(X)
    Y = np.array(Y)

    ## Equation: (E(XY)-E(X)E(Y))/(Std(X)Std(Y))
    sumxy = np.dot(X, Y)

    return (sumxy - len(X)*np.mean(X)*np.mean(Y))/((len(X)-1)*np.std(X, ddof=1)*np.std(Y,ddof=1))
