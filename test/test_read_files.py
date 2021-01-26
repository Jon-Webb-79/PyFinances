# Import necessary packages here
import pytest
import sys
import os
import platform
import numpy as np
from math import isclose
sys.path.insert(0, os.path.abspath('../src'))

from read_files import ReadTextFileKeywords, ReadRunOptionsFile
# ================================================================================
# ================================================================================
# Date:    January 24, 2021
# Purpose: This code contains functions that test the functions and classes
#          in the read_files.py file.
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
# Test the ReadTextFilekeywords class


def test_file_not_found():
    """

    This function ensures that the ReadTextFileKeywords class fails
    correctly when the file cannot be found
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/not_file_found.txt'
    else:
        file = r'..\data\test\not_file_found.txt'
    with pytest.raises(SystemExit):
        ReadTextFileKeywords(file)
# --------------------------------------------------------------------------------


def test_read_double_list():
    """

    This function tests the ReadTextFileKeywords.read_double_list
    function to determine if it can properly read a variable
    as a list of double precision values
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    double_value = key.read_double_list('double list:')
    expected = [1.12321, 344.3454453, 21.434553]
    for i in range(len(double_value)):
        assert isclose(double_value[i], expected[i], rel_tol=1.0e-3)
        assert isinstance(double_value[i], np.float64)
# --------------------------------------------------------------------------------


def test_read_float():
    """

    This function tests the ReadTextFileKeywords.read_float function to
    determine if it correctly reads in a variable as a numpy.float32
    variable.
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    value = key.read_float('float:')
    assert isclose(value, 3.1415, rel_tol=1.0e-3)
    assert isinstance(value, np.float32)
# --------------------------------------------------------------------------------


def test_float_list():
    """

    This function tests the ReadTextFileKeywords.read_float_list
    function to determine if it can properly read a variable
    as a list of float values
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    float_value = key.read_float_list('float list:')
    expected = [1.2, 3.4, 4.5, 5.6, 6.7]
    for i in range(len(float_value)):
        assert isclose(float_value[i], expected[i], rel_tol=1.0e-3)
        assert isinstance(float_value[i], np.float32)
# --------------------------------------------------------------------------------


def test_read_integer():
    """

    This function tests the ReadTextFileKeywords.read_float function to
    determine if it correctly reads in a variable as a numpy.int32
    variable.
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    value = key.read_integer('Integer Value:')
    assert value == 3
    assert isinstance(value, np.int32)
# --------------------------------------------------------------------------------


def test_read_integer_list():
    """

    This function tests the ReadTextFileKeywords.read_float_list
    function to determine if it can properly read a variable
    as a list of float values
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    int_value = key.read_integer_list('integer list:')
    expected = [1, 2, 3, 4, 5, 6, 7]
    for i in range(len(int_value)):
        assert isclose(int_value[i], expected[i], rel_tol=1.0e-3)
        assert isinstance(int_value[i], np.int32)
# --------------------------------------------------------------------------------


def test_read_sentence():
    """

    This function tests the ReadTextFileKeywords.read_sentence
    function to determine if it can properly read a sentence as
    a string
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_sentence('sentence:')
    assert sentence == "This is a short sentence!"
    assert isinstance(sentence, str)
# --------------------------------------------------------------------------------


def test_read_string():
    """

    This function tests the ReadTextFileKeywords.read_string
    function to determine if it can properly read a variable
    as a single string
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_string('String:')
    assert sentence == "test"
    assert isinstance(sentence, str)
# --------------------------------------------------------------------------------


def test_read_string_list():
    """

    This function tests the ReadTextFileKeywords.read_string_list
    function to determine if it can properly read a variable
    as a list of string values
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_string_list('sentence:')
    assert sentence == ['This', 'is', 'a', 'short', 'sentence!']
    for i in sentence:
        assert isinstance(i, str)
# ================================================================================
# ================================================================================
# Test the ReadRunOptionsFile class


def test_read_hist_true_info():
    """
    This function tests the ReadRunOptionsFile class to see if it correctly
    reads an input file when Run Histogram: is True.
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/RunOptionsHist.txt'
    else:
        file = r'..\data\test\RunOptionsHist.txt'
    inp = ReadRunOptionsFile(file)
    inp_dict = inp.read_file()
    assert inp_dict['run_hist'] == 'True'
    assert inp_dict['nbins'] == 60
    assert inp_dict['hist_start'] == '03/01/2020'
    assert inp_dict['hist_end'] == '02/28/2021'
    assert inp_dict['daily_expense_file'] == \
        '../data/test/expense_file_one.csv'
# --------------------------------------------------------------------------------


def test_read_no_hist_info():
    """
    This function tests the ReadRunOptionsFile class to see if it correctly
    reads an input file when Run Histogram: is not listed.
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/RunOptionsnoHist.txt'
    else:
        file = r'..\data\test\RunOptionsnoHist.txt'
    inp = ReadRunOptionsFile(file)
    inp_dict = inp.read_file()
    assert inp_dict['run_hist'] == 'False'
    assert inp_dict['nbins'] == 60
    assert inp_dict['hist_start'] == '03/01/2020'
    assert inp_dict['hist_end'] == '02/28/2021'
    assert inp_dict['daily_expense_file'] == \
        '../data/test/expense_file_one.csv'
    assert inp_dict['sample_size'] == 1000
    assert inp_dict['start_date'] == '03/01/2021'
    assert inp_dict['end_date'] == '02/28/2022'
    assert isclose(inp_dict['checking_start_value'], 54000.0, rel_tol=0.0001)
    assert isclose(inp_dict['savings_start_value'], 4800.0, rel_tol=0.0001)
    assert isclose(inp_dict['annual_salary'], 145000.0, rel_tol=0.0001)
    assert inp_dict['pay_frequency'] == 'Weekly'
    assert inp_dict['first_pay_date'] == '03/05/2021'
    assert inp_dict['total_expense_file'] == '../data/test/total_expenses.csv'
    assert inp_dict['planned_expense_file'] == \
        '../data/test/planned_expenses.csv'
    assert inp_dict['bills_file'] == '../data/test/bills.csv'
    assert inp_dict['deductions_file'] == '../data/test/deductions.csv'
# --------------------------------------------------------------------------------


def test_read_false_hist_info():
    """
    This function tests the ReadRunOptionsFile class to see if it correctly
    reads an input file when Run Histogram: is False.
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/RunOptionsFalseHist.txt'
    else:
        file = r'..\data\test\RunOptionsFalseHist.txt'
    inp = ReadRunOptionsFile(file)
    inp_dict = inp.read_file()
    assert inp_dict['run_hist'] == 'False'
    assert inp_dict['nbins'] == 60
    assert inp_dict['hist_start'] == '03/01/2020'
    assert inp_dict['hist_end'] == '02/28/2021'
    assert inp_dict['daily_expense_file'] == \
        '../data/test/expense_file_one.csv'
    assert inp_dict['sample_size'] == 1000
    assert inp_dict['start_date'] == '03/01/2021'
    assert inp_dict['end_date'] == '02/28/2022'
    assert isclose(inp_dict['checking_start_value'], 54000.0, rel_tol=0.0001)
    assert isclose(inp_dict['savings_start_value'], 4800.0, rel_tol=0.0001)
    assert isclose(inp_dict['annual_salary'], 145000.0, rel_tol=0.0001)
    assert inp_dict['pay_frequency'] == 'Weekly'
    assert inp_dict['first_pay_date'] == '03/05/2021'
    assert inp_dict['total_expense_file'] == '../data/test/total_expenses.csv'
    assert inp_dict['planned_expense_file'] == \
        '../data/test/planned_expenses.csv'
    assert inp_dict['bills_file'] == '../data/test/bills.csv'
    assert inp_dict['deductions_file'] == '../data/test/deductions.csv'
# --------------------------------------------------------------------------------


def test_read_bad_freq():
    """
    This function tests the ReadRunOptionsFile class to see if it correctly
    determines that the pay_frequency was not entered correctly
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/RunOptionsbadfreq.txt'
    else:
        file = r'..\data\test\RunOptionsbadfreq.txt'
    inp = ReadRunOptionsFile(file)
    with pytest.raises(SystemExit):
        inp_dict = inp.read_file()
# --------------------------------------------------------------------------------


def test_read_pay_date():
    """
    This function tests the ReadRunOptionsFile class to see if it correctly
    determines that the pay_frequency was not entered correctly
    """
    plat = platform.system()
    if plat == 'Darwin':
        file = '../data/test/RunOptionsbadpaydate.txt'
    else:
        file = r'..\data\test\RunOptionsbadpaydate.txt'
    inp = ReadRunOptionsFile(file)
    with pytest.raises(SystemExit):
        inp_dict = inp.read_file()
# ================================================================================
# ================================================================================
# eof
