# Import necessary packages here
import numpy as np
import pandas as pd
from typing import List
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


class MCEngine:
    """

    This class is used to produce a random sample of daily spending using a
    discrete sampling methodology
    """
    def __init__(self, cdf_files: List[str], sample_size: np.int32):
        self.cdf_files = cdf_files
        self.sample_size = sample_size
# --------------------------------------------------------------------------------

    def average_spending_estimate(self) -> np.float32:
        """

        :return avg, sigma: The average estimate for daily spending and the 
                            standard deviation for the estimate
        """
        samples = [self._daily_spending_estimate() for i in range(self.sample_size)]
        avg = np.average(samples)
        std = np.std(samples)
        return avg, std 
# ================================================================================
# Private-like functions here

    def _daily_spending_estimate(self) -> np.float:
        """

        :retun sum: The summation of the random spending average_spending_estimate
        """
        sample = [self._random_sample(i) for i in self.cdf_files]
        return np.sum(sample)
# --------------------------------------------------------------------------------

    def _random_sample(self, cdf: pd.DataFrame) -> np.float32:
        """

        :param cdf: A pandas dataframe containing a center and probability
                    column
        :return rand_val: A random value sampled from the dataframe
        """
        prob = np.array(list(cdf.probability), dtype=np.float32)
        r = np.random.random_sample()
        first_val = prob[prob >= r][0]
        indice = np.argwhere(prob == first_val)[0][0]
        sample = cdf.center[indice]
        return sample
# ================================================================================
# ================================================================================


def mcfunc(mcfunction, mcengine, dates: pd.DatetimeIndex, checking: np.float32, 
           savings: np.float32) -> pd.DataFrame:
    """

    :param mcfunction: An instantiated object of the MCFunction class 
    :param mcengine: An Instantiated object of the MCEngine class
    :param dates: A list of dates in the format YYYY-MM-DD
    :param checking: The initial value of the checking account
    :param savings: The initial value of the savings account
    :return df: A datrame containing the day by day estimations for 
                the value of the checing and savings accounts with 
                statistica; uncertainties
    """
    checking_act = []
    savings_act = []
    upper = []
    lower = []
    for i in dates:
        print(i)
        checking = mcfunction.add_paycheck(checking, i)
        checking, savings = mcfunction.deduct_bills(checking, savings, i)
        checking, savings = mcfunction.deduct_expenses(checking, savings, i)
        avg, sigma = mcengine.average_spending_estimate()
        checking -= avg
        checking_act.append(checking - avg)
        savings_act.append(savings)
        upper.append(checking + 2 * sigma)
        lower.append(checking - 2 * sigma)
    # Create dataframe and csv file
    outp = {'Date': dates, 'Checking_Mean': checking_act, 'Upper': upper, 
            'Lower': lower, 'Savings': savings_act}
    df = pd.DataFrame.from_dict(outp)
    return df
# ================================================================================
# ================================================================================
# eof
