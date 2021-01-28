# Import necessary packages here
import pytest
import math
import sys
import os
import numpy as np
import platform
sys.path.insert(0, os.path.abspath('../src'))
from pre_processor import MakeDistribution
from pre_processor import ProcessDailyExpenseFile
from pre_processor import CreateCDF, hist_pre_processor
from pre_processor import ReadCSVFile, ReadMonteCarloFiles
# ================================================================================
# ================================================================================
# Date:    January 26, 20211
# Purpose: This file will test functions anc classes associated with pre
#          processors
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
# Test ProcessDailyExpenseFile Class


def test_read_daily_expenses_csv():
    """

    This function tests the ProcessDailyExpenseFile.read_daily_expense_csv()
    function to determine if it correctly reads in the daily_expenses.csv file
    """
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/daily_expenses_one.csv'
    else:
        file_name = r'..\data\test\daily_expenses_one.csv'
    obj = ProcessDailyExpenseFile(file_name)
    df = obj.read_daily_expenses_csv()
    assert len(df) == 4349
    headers = ['Date', 'Checking_Debit', 'Checking_Addition',
               'Savings_Debit', 'Savings_Addition', 'Expense_Type']
    df_headers = list(df.columns.values)
    for i in headers:
        assert i in df_headers
# --------------------------------------------------------------------------------


def test_grouped_dataframe_expense():
    """

    This function tests the ability of
    ProcessDailyExpenseFile.group_expenses_by_date to read the
    Daily_Expense.csv file and transform its contents into another file
    containing a day by day breakdown of each expense type.

    """
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/daily_expenses_one.csv'
        total_expense = '../data/test/total_expense.csv'
    else:
        file_name = r'..\data\test\daily_expenses_one.csv'
        total_expense = r'../data/test/total_expense.csv'
    obj = ProcessDailyExpenseFile(file_name)
    start_date = '2015-03-01'
    end_date = '2016-02-28'
    obj.group_expenses_by_date(start_date, end_date, total_expense)
    assert os.path.isfile(total_expense)

    if os.path.isfile(total_expense):
        os.remove(total_expense)

# ================================================================================
# ================================================================================


np.random.seed(0)
mu = 120.0
sigma = 8.0
sample_size = 5000
n_bins = 10
values = np.random.normal(mu, sigma, sample_size)
dist = MakeDistribution(values)


def test_give_name_here():
    """

    This function tests the discrte_pdf function to ensure it returns
    the correct values when using normed=True
    """
    bins, edges = dist.discrete_pdf(n_bins, normed=True)
    exp_bins = np.array([0.0014, 0.0096, 0.0588, 0.1722,
                         0.2802, 0.2678, 0.1496, 0.051,
                         0.0086, 0.0008], dtype=np.float64)
    exp_edges = np.array([90.0791949, 96.11260358, 102.14601226,
                          108.17942094, 114.21282963, 120.24623831,
                          126.27964699, 132.31305567, 138.34646436,
                          144.37987304, 150.41328172], dtype=np.float64)
    for i, j in zip(exp_bins, bins):
        assert math.isclose(i, j, rel_tol=0.04)
    for i, j in zip(exp_edges, edges):
        assert math.isclose(i, j, rel_tol=1.0e-4)
# ------------------------------------------------------------------------------


def test_discrete_pdf_non_normed():
    """

    This function tests the discrte_pdf function to ensure it returns
    the correct values when using normed=False
    """
    bins, edges = dist.discrete_pdf(n_bins, normed=False)
    exp_bins = np.array([7.0,  48.0, 294.0, 861.0, 1401.0, 1339.0,
                         748.0, 255.0, 43.0, 4.0], dtype=np.float64)
    exp_edges = np.array([90.0791949, 96.11260358, 102.14601226,
                          108.17942094, 114.21282963, 120.24623831,
                          126.27964699, 132.31305567, 138.34646436,
                          144.37987304, 150.41328172], dtype=np.float64)
    for i, j in zip(exp_bins, bins):
        assert math.isclose(i, j, rel_tol=0.04)
    for i, j in zip(exp_edges, edges):
        assert math.isclose(i, j, rel_tol=1.0e-4)
# ------------------------------------------------------------------------------


def test_continuous_pdf_normed():
    """

    This function tests the dcontinuous_pdf function to ensure it returns
    the correct values when using normed=True
    """
    prob, middle = dist.continuous_pdf(n_bins, norm=True)
    exp_prob = np.array([0.0014, 0.0096, 0.0588, 0.1722,
                         0.2802, 0.2678, 0.1496, 0.051,
                         0.0086, 0.0008], dtype=np.float64)
    exp_middle = np.array([93.09589924, 99.12930792, 105.1627166, 111.19612528,
                           117.22953397, 123.26294265, 129.29635133, 135.32976001,
                           141.3631687,  147.39657738], dtype=np.float64)
    for i, j in zip(exp_prob, prob):
        assert math.isclose(i, j, rel_tol=0.04)
    for i, j in zip(exp_middle, middle):
        assert math.isclose(i, j, rel_tol=1.0e-4)
# ------------------------------------------------------------------------------


def test_continuous_pdf_non_normed():
    """

    This function tests the continuous_pdf function to ensure it returns
    the correct values when using normed=False
    """
    prob, middle = dist.continuous_pdf(n_bins, norm=False)
    exp_prob = np.array([7.0, 48.0, 294.0, 861.0, 1401.0, 1339.0,
                         748.0, 255.0, 43.0, 4.0], dtype=np.float64)
    exp_middle = np.array([93.09589924, 99.12930792, 105.1627166, 111.19612528,
                           117.22953397, 123.26294265, 129.29635133, 135.32976001,
                           141.3631687,  147.39657738], dtype=np.float64)
    for i, j in zip(exp_prob, prob):
        assert math.isclose(i, j, rel_tol=0.04)
    for i, j in zip(exp_middle, middle):
        assert math.isclose(i, j, rel_tol=1.0e-4)
# ------------------------------------------------------------------------------


def test_discrete_cdf_non_normed():
    """

    This function tests the discrete_cdf function to ensure it returns
    the correct values when using normed=False
    """
    prob, bins = dist.discrete_cdf(n_bins, norm=False)
    exp_prob = np.array([7.0, 55.0, 349.0, 1210.0, 2611.0, 3950.0,
                         4698.0, 4953.0, 4996.0, 5000.0], dtype=np.float64)
    exp_edges = np.array([90.0791949, 96.11260358, 102.14601226,
                          108.17942094, 114.21282963, 120.24623831,
                          126.27964699, 132.31305567, 138.34646436,
                          144.37987304, 150.41328172], dtype=np.float64)
    for i, j in zip(exp_prob, prob):
        assert math.isclose(i, j, rel_tol=0.04)
    for i, j in zip(exp_edges, bins):
        assert math.isclose(i, j, rel_tol=1.0e-4)
# ------------------------------------------------------------------------------


def test_discrete_cdf_normed():
    """

    This function tests the discrete_cdf function to ensure it returns
    the correct values when using normed=True
    """
    prob, bins = dist.discrete_cdf(n_bins, norm=True)
    exp_prob = np.array([0.0014, 0.011, 0.0698, 0.242, 0.5222, 0.79,
                         0.9396, 0.9906, 0.9992, 1.0], dtype=np.float64)
    exp_edges = np.array([90.0791949, 96.11260358, 102.14601226,
                          108.17942094, 114.21282963, 120.24623831,
                          126.27964699, 132.31305567, 138.34646436,
                          144.37987304, 150.41328172], dtype=np.float64)
    for i, j in zip(exp_prob, prob):
        assert math.isclose(i, j, rel_tol=0.04)
    for i, j in zip(exp_edges, bins):
        assert math.isclose(i, j, rel_tol=1.0e-4)
# ------------------------------------------------------------------------------


def test_continuous_cdf_non_normed():
    """

    This function tests the continuous_cdf function to ensure it returns
    the correct values when using normed=False
    """
    prob, middle = dist.continuous_cdf(n_bins, norm=False)
    exp_prob = np.array([7.0, 55.0, 349.0, 1210.0, 2611.0, 3950.0,
                         4698.0, 4953.0, 4996.0, 5000.0], dtype=np.float64)
    exp_middle = np.array([93.09589924, 99.12930792, 105.1627166,
                           111.19612528, 117.22953397, 123.26294265,
                           129.29635133, 135.32976001, 141.3631687,
                           147.39657738], dtype=np.float64)
    for i, j in zip(exp_prob, prob):
        assert math.isclose(i, j, rel_tol=0.04)
    for i, j in zip(exp_middle, middle):
        assert math.isclose(i, j, rel_tol=1.0e-4)
# ------------------------------------------------------------------------------


def test_continuous_cdf_normed():
    """

    This function tests the continuous_cdf function to ensure it returns
    the correct values when using normed=True
    """
    prob, middle = dist.continuous_cdf(n_bins, norm=True)
    exp_prob = np.array([0.0014, 0.011, 0.0698, 0.242, 0.5222, 0.79,
                         0.9396, 0.9906, 0.9992, 1.0], dtype=np.float64)
    exp_middle = np.array([93.09589924, 99.12930792, 105.1627166,
                           111.19612528, 117.22953397, 123.26294265,
                           129.29635133, 135.32976001, 141.3631687,
                           147.39657738], dtype=np.float64)
    for i, j in zip(exp_prob, prob):
        assert math.isclose(i, j, rel_tol=0.04)
    for i, j in zip(exp_middle, middle):
        assert math.isclose(i, j, rel_tol=1.0e-4)
# ================================================================================
# ================================================================================


def test_create_cdf():
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/daily_expenses_one.csv'
        total_file = '../data/test/total_expense_two.csv'
        cdf_file = '../data/test/cdf.csv'
    else:
        file_name = r'..\data\test\daily_expenses_one.csv'
        total_file = r'..\data\test\total_expenses_two.csv'
        cdf_file = r'..\data\test\cdf.csv'
    nbins = 60
    start_date = '2015-03-01'
    end_date = '2016-02-28'
    proc = ProcessDailyExpenseFile(file_name)
    proc.group_expenses_by_date(start_date, end_date, total_file)

    inp = ReadCSVFile()
    headers = ['Bar', 'Groceries', 'Restaurant', 'Misc', 'Gas']
    dat_type = [np.float32, np.float32, np.float32, np.float32, np.float32]
    df = inp.read_csv_columns_by_headers(total_file, headers,
                                         dat_type)
    bar = CreateCDF(df['Bar'])
    bar.create_cdf_file(cdf_file, nbins)
    assert os.path.isfile(cdf_file)
    if os.path.isfile(total_file):
        os.remove(total_file)
    if os.path.isfile(cdf_file):
        os.remove(cdf_file)
# ================================================================================
# ================================================================================


def test_hist_pre_processor():
    start_date = '2015-03-01'
    end_date = '2016-02-28'
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/daily_expenses_one.csv'
        total_file = '../data/test/total_expense_two.csv'
        cdf_file = '../data/test/'
    else:
        file_name = r'..\data\test\daily_expenses_one.csv'
        total_file = r'..\data\test\total_expenses_two.csv'
        cdf_file = r'..\data\test\ '
    nbins = 60
    hist_pre_processor(start_date, end_date, nbins,
                       file_name, total_file, cdf_file)
    assert os.path.isfile(total_file)
    assert os.path.isfile(cdf_file + 'barcdf.csv')
    assert os.path.isfile(cdf_file + 'misccdf.csv')
    assert os.path.isfile(cdf_file + 'gascdf.csv')
    assert os.path.isfile(cdf_file + 'groccdf.csv')
    assert os.path.isfile(cdf_file + 'restcdf.csv')

    os.remove(total_file)
    os.remove(cdf_file + 'barcdf.csv')
    os.remove(cdf_file + 'gascdf.csv')
    os.remove(cdf_file + 'misccdf.csv')
    os.remove(cdf_file + 'groccdf.csv')
    os.remove(cdf_file + 'restcdf.csv')
# ================================================================================
# ================================================================================
# Test functions from the ReadMonteCarloFiles class 


def test_read_cdf_files():
    """

    This function tests the read_cdf_file function to see if it corerctly
    reads a cdf file
    """
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/cdf_file.csv'
    else:
        file_name = r'..\data\test\cdf_file.csv'

    read = ReadMonteCarloFiles()
    df = read.read_cdf_file(file_name)
    prob = [0.215, 0.321, 0.415, 0.550, 0.640, 0.720, 0.840, 0.950, 1.000]
    cent = [8.75, 2.18, 8.95, 14.80, 17.89, 23.50, 32.50, 44.18, 51.20]
    for i in range(len(prob)):
        assert math.isclose(prob[i], df['probability'][i], rel_tol=1.0e-3)
        assert math.isclose(cent[i], df['center'][i], rel_tol=1.0e-3)
# --------------------------------------------------------------------------------


def test_read_bills():
    """

    This function tests the ability of the read_bills_file()
    function to correclty read the bills.csv file
    """
    plat = platform.system()
    if plat == 'Darwin':
        file_name = '../data/test/bills.csv'
    else:
        file_name = r'..\data\test\bills.csv'
    read = ReadMonteCarloFiles()
    df = read.read_bills_file(file_name)
    day = np.array([3, 15, 28], np.dtype(int))
    addition = np.array([35.0, 75.0, 131.0], np.dtype(np.float32))
    for i in range(len(day)):
        assert math.isclose(day[i], df['Day'][i])
        assert math.isclose(addition[i], df['Checking_Debit'][i], rel_tol=1.0e-3)
# ================================================================================
# ================================================================================
# eof
