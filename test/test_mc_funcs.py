# Import necessary packages here
import sys
import numpy as np
import os
import platform
from math import isclose
sys.path.insert(0, os.path.abspath('../PyFinances'))

from monte_carlo import MCFunctions, MCEngine
from pre_processor import MCPreProcessor
# ================================================================================
# ================================================================================
# Date:    February 5, 2021
# Purpose: Describe the types of testing to occur in this file.
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
# Test MCFunctions class


def test_add_paycheck():
    """

    This function tests the ability of the add_paycheck function to properly
    determine if it is a pay date and add the pay allocation to the Checking
    account
    """
    mc_pre = MCPreProcessor()
    start_date = '2021-03-01'
    end_date = '2022-02-28'
    pay_frequency = 'weekly'
    first_pay_date = '2021-03-05'
    plat = platform.system()
    if plat == 'Darwin':
        bills_file = '../data/test/bills_test.csv'
        expenses_file = '../data/test/planned_expense_test.csv'
        deductions_file = '../data/test/deductions_test.csv'
    else:
        bills_file = r'..\data\test\bills_test.csv'
        expenses_file = r'..\data\test\planned_expense_test.csv'
        deductions_file = r'..\data\test\deductions_test.csv'

    iter_dates, pay_dates = mc_pre.create_dates(start_date, end_date,
                                                first_pay_date, pay_frequency)
    bills_df = mc_pre.read_bills(bills_file)
    expenses_df = mc_pre.read_expenses(expenses_file)
    pay_alloc = mc_pre.pay_allocation(deductions_file, 145000.0, pay_frequency)

    mcfunc = MCFunctions(pay_alloc, pay_dates, expenses_df, bills_df)
    new_value = mcfunc.add_paycheck(31000.0, iter_dates[4])
    assert isclose(new_value, 33073.37, rel_tol=1.0e-3)
# ================================================================================


def test_no_paycheck():
    """

    This function tests the ability of the add_paycheck function to properly
    determine if it is a pay date and add the pay allocation to the Checking
    account
    """
    mc_pre = MCPreProcessor()
    start_date = '2021-03-01'
    end_date = '2022-02-28'
    pay_frequency = 'weekly'
    first_pay_date = '2021-03-05'
    plat = platform.system()
    if plat == 'Darwin':
        bills_file = '../data/test/bills_test.csv'
        expenses_file = '../data/test/planned_expense_test.csv'
        deductions_file = '../data/test/deductions_test.csv'
    else:
        bills_file = r'..\data\test\bills_test.csv'
        expenses_file = r'..\data\test\planned_expense_test.csv'
        deductions_file = r'..\data\test\deductions_test.csv'

    iter_dates, pay_dates = mc_pre.create_dates(start_date, end_date,
                                                first_pay_date, pay_frequency)
    bills_df = mc_pre.read_bills(bills_file)
    expenses_df = mc_pre.read_expenses(expenses_file)
    pay_alloc = mc_pre.pay_allocation(deductions_file, 145000.0, pay_frequency)

    mcfunc = MCFunctions(pay_alloc, pay_dates, expenses_df, bills_df)
    new_value = mcfunc.add_paycheck(31000.0, iter_dates[3])
    assert isclose(new_value, 31000.0, rel_tol=1.0e-3)
# ================================================================================


def test_no_deduction_bills():
    """

    This function tests the ability of the deduct_bills() function properly
    realizes that it is not a bills deduction day and does not dedict a bill.
    """
    mc_pre = MCPreProcessor()
    start_date = '2021-03-01'
    end_date = '2022-02-28'
    pay_frequency = 'weekly'
    first_pay_date = '2021-03-05'
    plat = platform.system()
    if plat == 'Darwin':
        bills_file = '../data/test/bills_test.csv'
        expenses_file = '../data/test/planned_expense_test.csv'
        deductions_file = '../data/test/deductions_test.csv'
    else:
        bills_file = r'..\data\test\bills_test.csv'
        expenses_file = r'..\data\test\planned_expense_test.csv'
        deductions_file = r'..\data\test\deductions_test.csv'

    iter_dates, pay_dates = mc_pre.create_dates(start_date, end_date,
                                                first_pay_date, pay_frequency)
    bills_df = mc_pre.read_bills(bills_file)
    expenses_df = mc_pre.read_expenses(expenses_file)
    pay_alloc = mc_pre.pay_allocation(deductions_file, 145000.0, pay_frequency)

    mcfunc = MCFunctions(pay_alloc, pay_dates, expenses_df, bills_df)
    checking, savings = mcfunc.deduct_bills(31000.0, 4000.0, iter_dates[3])
    assert isclose(31000, checking, rel_tol=1.0e-3)
    assert isclose(4000.0, savings, rel_tol=1.0e-3)
# ================================================================================


def test_deduction_bills():
    """

    This function tests the ability of the deduct_bills() function properly
    realizes that it is a bills deduction day and does deduct a bill.
    """
    mc_pre = MCPreProcessor()
    start_date = '2021-03-01'
    end_date = '2022-02-28'
    pay_frequency = 'weekly'
    first_pay_date = '2021-03-05'
    plat = platform.system()
    if plat == 'Darwin':
        bills_file = '../data/test/bills_test.csv'
        expenses_file = '../data/test/planned_expense_test.csv'
        deductions_file = '../data/test/deductions_test.csv'
    else:
        bills_file = r'..\data\test\bills_test.csv'
        expenses_file = r'..\data\test\planned_expense_test.csv'
        deductions_file = r'..\data\test\deductions_test.csv'

    iter_dates, pay_dates = mc_pre.create_dates(start_date, end_date,
                                                first_pay_date, pay_frequency)
    bills_df = mc_pre.read_bills(bills_file)
    expenses_df = mc_pre.read_expenses(expenses_file)
    pay_alloc = mc_pre.pay_allocation(deductions_file, 145000.0, pay_frequency)

    mcfunc = MCFunctions(pay_alloc, pay_dates, expenses_df, bills_df)
    checking, savings = mcfunc.deduct_bills(31000.0, 4000.0, iter_dates[14])
    assert isclose(30925.0, checking, rel_tol=1.0e-3)
    assert isclose(4075.0, savings, rel_tol=1.0e-3)
# ================================================================================


def test_deduct_planned_expenses():
    """

    This function tests the ability of the deduct_expense() function properly
    realizes that it is a bills deduction day and does deduct a bill.
    """
    mc_pre = MCPreProcessor()
    start_date = '2021-05-01'
    end_date = '2022-02-28'
    pay_frequency = 'weekly'
    first_pay_date = '2021-03-05'
    plat = platform.system()
    if plat == 'Darwin':
        bills_file = '../data/test/bills_test.csv'
        expenses_file = '../data/test/planned_expense_test.csv'
        deductions_file = '../data/test/deductions_test.csv'
    else:
        bills_file = r'..\data\test\bills_test.csv'
        expenses_file = r'..\data\test\planned_expense_test.csv'
        deductions_file = r'..\data\test\deductions_test.csv'

    iter_dates, pay_dates = mc_pre.create_dates(start_date, end_date,
                                                first_pay_date, pay_frequency)
    bills_df = mc_pre.read_bills(bills_file)
    expenses_df = mc_pre.read_expenses(expenses_file)
    pay_alloc = mc_pre.pay_allocation(deductions_file, 145000.0, pay_frequency)
    mcfunc = MCFunctions(pay_alloc, pay_dates, expenses_df, bills_df)
    checking, savings = mcfunc.deduct_expenses(31000.0, 4000.0, iter_dates[13])
    assert isclose(30055.0, checking, rel_tol=1.0e-3)
    assert isclose(4000.0, savings, rel_tol=1.0e-3)
# --------------------------------------------------------------------------------


def test_no_deuct_planned_expenses():
    """

    This function tests the ability of the deduct_expense() function properly
    realizes that it is a bills deduction day and does deduct a bill.
    """
    mc_pre = MCPreProcessor()
    start_date = '2021-05-01'
    end_date = '2022-02-28'
    pay_frequency = 'weekly'
    first_pay_date = '2021-03-05'
    plat = platform.system()
    if plat == 'Darwin':
        bills_file = '../data/test/bills_test.csv'
        expenses_file = '../data/test/planned_expense_test.csv'
        deductions_file = '../data/test/deductions_test.csv'
    else:
        bills_file = r'..\data\test\bills_test.csv'
        expenses_file = r'..\data\test\planned_expense_test.csv'
        deductions_file = r'..\data\test\deductions_test.csv'

    iter_dates, pay_dates = mc_pre.create_dates(start_date, end_date,
                                                first_pay_date, pay_frequency)
    bills_df = mc_pre.read_bills(bills_file)
    expenses_df = mc_pre.read_expenses(expenses_file)
    pay_alloc = mc_pre.pay_allocation(deductions_file, 145000.0, pay_frequency)
    mcfunc = MCFunctions(pay_alloc, pay_dates, expenses_df, bills_df)
    checking, savings = mcfunc.deduct_expenses(31000.0, 4000.0, iter_dates[14])
    assert isclose(31000.0, checking, rel_tol=1.0e-3)
    assert isclose(4000.0, savings, rel_tol=1.0e-3)
# ================================================================================
# ================================================================================


def test_average_spending_estimate():
    plat = platform.system()
    if plat == 'Darwin':
        cdf_loc = '../data/test/'
    else:
        cdf_loc = r'..\data\test\ '.replace(" ", "")
    files = ['testbarcdf.csv', 'testgascdf.csv', 'testgroccdf.csv',
             'testmisccdf.csv', 'testrestcdf.csv']
    cdf_files = [cdf_loc + i for i in files]
    mc_pre = MCPreProcessor()
    cdf_df_list = mc_pre.read_cdf(cdf_files)
    np.random.seed(100)
    mc = MCEngine(cdf_df_list, 100)
    avg, std = mc.average_spending_estimate()
    assert isclose(88.79, avg, rel_tol=1.0e-3)
    assert isclose(96.41, std, rel_tol=1.0e-3)
# ================================================================================
# ================================================================================
# eof
