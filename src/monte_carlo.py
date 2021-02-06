# Import necessary packages here
import numpy as np
import pandas as pd
# ================================================================================
# ================================================================================ 
# Date:    February 1, 2021
# Purpose: This file contains all functions and classes necessary to run
#          the Monte Carlo portion of the PyFinances software suite

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2021, Jon Webb Inc."
__version__ = "1.0"
# ================================================================================ 
# ================================================================================ 
# Insert Code here


class MCFunctions():
    """
 
    :param alloc_pay: The paycheck issued to the employee after all deductions.
    :param pay_date: A pandas datetimeindex of al pay dates
    :param expense_file: A pandas dataframe containing all planned expenses for
                         the iteration period
    :param bills_file: A pandas dataframe containing all bills to be paid and the
                       day the bills will be paid.

    This class contains all non-Monte Carlo related functions used during the 
    date iteration for the PyFinances software suite
    """
    def __init__(self, alloc_pay: np.float32, pay_dates: pd.DatetimeIndex, 
                 expenses_file: pd.DataFrame, bills_file: pd.DataFrame):
        self.alloc_pay = alloc_pay
        self.pay_dates = pay_dates
        self.expenses_file = expenses_file
        self.bills_file = bills_file
# --------------------------------------------------------------------------------

    def add_paycheck(self, checking_account: np.float32, 
                     date: pd.DatetimeIndex) -> np.float32:
        """

        :param checking_account: The current value of the checking account.
        :param date: The iteration date.
        :return checking_account: The value of the checking account after 
                                  adding the pay allocation
        """
        if date in self.pay_dates:
            checking_account += self.alloc_pay 
        return checking_account
# --------------------------------------------------------------------------------

    def deduct_bills(self, checking_account: np.float32, 
                     savings_account: np.float32, 
                     date: pd.DatetimeIndex) -> np.float32:
        """

        :param checking_account: The current value of the checking account.
        :param savings_account: The current value of the savings account
        :param date: The iteration date.
        :return checking_account, savings_account: The value of the checking
                                                   and savgins accounts after
                                                   bill deductions
        """
        # Format dates to match days
        new_date = str(date)
        new_day = np.int64(new_date[8:10]) 
        # Filter df to inly include entires on those days
        df = self.bills_file[(self.bills_file.Day == new_day)]
        checking = df['Checking_Addition'].sum() - df['Checking_Debit'].sum()
        savings = df['Savings_Addition'].sum() - df['Savings_Debit'].sum()
        # deduct bills
        checking_account += checking
        savings_account += savings
        return checking_account, savings_account
# --------------------------------------------------------------------------------

    def deduct_expenses(self, checking_account: np.float32, 
                        savings_account: np.float32, 
                        date: pd.DatetimeIndex) -> np.float32:
        """

        :param checking_account: The current value of the checking account.
        :param savings_account: The current value of the savings account.
        :param date: The iteration date.
        :return checking_account, savings_account: The value of the checking
                                                   and savings accounts after
                                                   planned expenses are 
                                                   deducted.
        """
        df = self.expenses_file[(self.expenses_file.Date == date)]
        
        checking = df['Checking_Addition'].sum() - df['Checking_Debit'].sum()
        savings = df['Savings_Addition'].sum() - df['Savings_Debit'].sum()
        # deduct bills
        checking_account += checking
        savings_account += savings
        return checking_account, savings_account
# ================================================================================ 
# ================================================================================
# eof
