#! /usr/bin/python

"""
This is the help function that is used to generate the basic information of the Pandas DataFrame. This function doesn't return anything, but print out
some basic information of the dataset.

Author: Charlie Dang
Date: March/01/2018

"""

import pandas as pd

def get_info(Dataframe):
    """
    This function will generate a basic information of the Dataframe
    """
    if not isinstance(Dataframe, pd.core.frame.DataFrame):
        raise Examption("Error Format! The input datatype must be Pandas' DataFrame!!")

    print ("The Dataset has %d columns, and %d observations.", %(Dataframe.shape[1], Dataframe.shape[0]))
    print ("------------------------------------------------")
    print ("\n")
    print ("The features of the DataFrame are: ", Dataframe.columns.values)


def list_null(Dataframe):
    """
    This function will list the null information of the DataFrame
    """
    if not isinstance(Dataframe, pd.core.frame.DataFrame):
        raise Examption("Error Format! The input datatype must be Pandas' DataFrame!!")

    print df.shape[1],' columns:'
    for i in df.columns.values:
        print i,': nan',df[i].isnull().sum(),', ',df[i].dtypes
