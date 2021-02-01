# Import necessary packages here
import pytest
from math import isclose
import os
import sys
import platform
sys.path.insert(0, os.path.abspath('../src'))
from monte_carlo import MonteCarloExec
# ================================================================================
# ================================================================================
# Date:    January 1, 2021
# Purpose: This file contains tests for all of the functions and classes in
#          the monte_carlo.py file
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


def test_give_name_here():
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/deductions_one.csv'
    else:
        file_name = r'..\data\test\deductions_one.csv'
    obj = MonteCarloExec()
    pay = obj.determine_pay_allocation(135000.0, 'weekly', file_name)
    assert isclose(1881.06, pay, rel_tol=1.0e-3)
# ================================================================================
# ================================================================================
# eof
