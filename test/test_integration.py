# Import necessary packages here
import os
import sys
import platform
import pandas as pd
sys.path.insert(0, os.path.abspath('../PyFinances'))

from pyfinances import pyfinances
# ================================================================================
# ================================================================================
# Date:    February 4, 2021
# Purpose: This file contains regression tests that validate the functionality
#          of the PyFinances software suite
# Instruction: This code can be run in hte following ways
#              - pytest # runs all functions beginnning with the word test in
#                         the directory
#              - pytest file_name.py # Runs all functions in file_name
#                                      beginning with the word test
#              - pytest file_name.py::test_func_name # Runs only the function
#                                                      titled test_func_name in
#                                                      the file_name.py file
#              - pytest -s # Runs tests and displays when a specific file
#                            has completed testing, and what functions failed.
#                            Also displays print statments
#              - pytest -v # Displays test results on a function by function
#                            basis
#              - pytest -p no:warnings # Runs tests and does not display
#                                        warning messages
#              - pytest -s -v -p no:warnings # Displays relevant information
#                                              and supports debugging
#              - pytest -s -p no:warnings # Run for record

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2021, Jon Webb Inc."
__version__ = "1.0"
# ================================================================================
# ================================================================================
# Insert Code here


def test_create_cdf_files():
    """

    This function tests the PyFinances ability to produce a series of cdf
    files in its run configuration
    """
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/RunOptionsTest.txt'
        total_file = '../data/test/total_expenses.csv'
        file_loc = '../data/hist/'
    else:
        file_name = r'..\data\test\RunOptionsTest.txt'
        file_loc = r'..\data\hist\ '
        total_file = r'..\data\test\total_expenses.csv'
    pyfinances(file_name)
    files = ['barcdf.csv', 'gascdf.csv', 'groccdf.csv', 'misccdf.csv',
             'restcdf.csv']
    for i in files:
        assert os.path.isfile(file_loc + i)

    for i in files:
        os.remove(file_loc + i)
    os.remove(total_file)
# --------------------------------------------------------------------------------


def test_no_cdf_files_exist():
    """

    This function tests teh PyFinances ability to create cdf files if they
    do not exist and execute all Monte Carlo pre-processor functions
    """
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/RunOptionsTest.txt'
        total_file = '../data/test/total_expenses.csv'
        file_loc = '../data/hist/'
        csv_file = '../data/test/estimate.csv'
        png_file = '../data/test/estimate.png'
    else:
        file_name = r'..\data\test\RunOptionsTest.txt'
        file_loc = r'..\data\hist\ '
        total_file = r'..\data\test\total_expenses.csv'
        csv_file = r'..\data\test\estimate.csv'
        png_fil = r'..\data\test\estimate.png'
    files = ['barcdf.csv', 'gascdf.csv', 'groccdf.csv', 'misccdf.csv',
             'restcdf.csv']

    for i in files:
        if os.path.isfile(file_loc + i):
            os.remove(file_loc + i)
    pyfinances(file_name)

    for i in files:
        assert os.path.isfile(file_loc + i)

    for i in files:
        os.remove(file_loc + i)
    os.remove(csv_file)
    os.remove(png_file)
# ================================================================================
# ================================================================================
# eof
