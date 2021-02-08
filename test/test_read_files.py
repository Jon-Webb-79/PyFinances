# Import necessary packages here
import pytest
import sys
import os
import platform
import numpy as np
from math import isclose
sys.path.insert(1, os.path.abspath('PyFinances'))
from PyFinances.read_files import ReadTextFileKeywords, ReadRunOptionsFile
from PyFinances.read_files import ReadCSVFile
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
    assert inp_dict['hist_start'] == '2020-03-01'
    assert inp_dict['hist_end'] == '2021-02-28'
    assert inp_dict['daily_expense_file'] == \
        '../data/test/daily_expenses_one.csv'
    assert inp_dict['hist_location'] == \
        '../data/test/'
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
    assert inp_dict['hist_start'] == '2020-03-01'
    assert inp_dict['hist_end'] == '2021-02-28'
    assert inp_dict['daily_expense_file'] == \
        '../data/test/expense_file_one.csv'
    assert inp_dict['sample_size'] == 1000
    assert inp_dict['start_date'] == '2021-03-01'
    assert inp_dict['end_date'] == '2022-02-28'
    assert isclose(inp_dict['checking_start_value'], 54000.0, rel_tol=0.0001)
    assert isclose(inp_dict['savings_start_value'], 4800.0, rel_tol=0.0001)
    assert isclose(inp_dict['annual_salary'], 145000.0, rel_tol=0.0001)
    assert inp_dict['pay_frequency'] == 'Weekly'
    assert inp_dict['first_pay_date'] == '2021-03-05'
    assert inp_dict['total_expense_file'] == '../data/test/total_expenses.csv'
    assert inp_dict['planned_expense_file'] == \
        '../data/test/planned_expenses.csv'
    assert inp_dict['bills_file'] == '../data/test/bills.csv'
    assert inp_dict['deductions_file'] == '../data/test/deductions.csv'
    assert inp_dict['hist_location'] == '../data/test/'
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
    assert inp_dict['hist_start'] == '2020-03-01'
    assert inp_dict['hist_end'] == '2021-02-28'
    assert inp_dict['daily_expense_file'] == \
        '../data/test/expense_file_one.csv'
    assert inp_dict['sample_size'] == 1000
    assert inp_dict['start_date'] == '2021-03-01'
    assert inp_dict['end_date'] == '2022-02-28'
    assert isclose(inp_dict['checking_start_value'], 54000.0, rel_tol=0.0001)
    assert isclose(inp_dict['savings_start_value'], 4800.0, rel_tol=0.0001)
    assert isclose(inp_dict['annual_salary'], 145000.0, rel_tol=0.0001)
    assert inp_dict['pay_frequency'] == 'Weekly'
    assert inp_dict['first_pay_date'] == '2021-03-05'
    assert inp_dict['total_expense_file'] == \
        '../data/test/total_expenses.csv'
    assert inp_dict['planned_expense_file'] == \
        '../data/test/planned_expenses.csv'
    assert inp_dict['bills_file'] == '../data/test/bills.csv'
    assert inp_dict['deductions_file'] == '../data/test/deductions.csv'
    assert inp_dict['hist_location'] == '../data/test/'
# --------------------------------------------------------------------------------
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
# Test read csv functions


def test_read_csv_by_headers():
    """

    This function tests the read_csv_columns_by_headers function to ensure
    it properly reads in a csv file with the headers placed at the top
    of the file
    """
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/test1.csv'
    else:
        file_name = r'..\data\test\test1.csv'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    obj = ReadCSVFile()
    df = obj.read_csv_columns_by_headers(file_name, headers, dat)
    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ================================================================================
# ================================================================================
# eof
