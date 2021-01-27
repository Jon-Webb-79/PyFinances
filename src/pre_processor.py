# Import necessary packages here
from read_files import ReadCSVFile
import numpy as np
import pandas as pd
from typing import Tuple, List
# ================================================================================
# ================================================================================ 
# Date:    January 26, 20211
# Purpose: The file contains functions that process data in order to 
#           support the PyFinances Monte Carlo program

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2021, Jon Webb Inc."
__version__ = "1.0"
# ================================================================================ 
# ================================================================================ 
# Insert Code here


class ProcessDailyExpenseFile(ReadCSVFile):
    """

    :param file_name: The name and path-length of the Daily_Expenses.csv
                      file 

    This class contains functions that process the Daily_Expenses.csv 
    file in different ways.
    """
    def __init__(self, file_name: str):
        self.file_name = file_name 
# --------------------------------------------------------------------------------

    def read_daily_expenses_csv(self) -> pd.DataFrame:
        """

        :return df: A pandas dataframe containing the relevant information from 
                    the daily_expenses.csv file 

        This function reads relevant information from the daily_expenses.csv vile into
        memory so it can use it for the creation of the total_expenses.csv file.
        """
        headers = ['Date', 'Checking_Debit', 'Checking_Addition', 'Savings_Debit', 
                  'Savings_Addition', 'Expense_Type']
        dat_type = [str, np.float32, np.float32, np.float32, np.float32, str]
        df = self.read_csv_columns_by_headers(self.file_name, headers, dat_type)
        return df
# --------------------------------------------------------------------------------


    def group_expenses_by_date(self, start_date: str, end_date: str, 
                               total_expense_file: str) -> None:
        """

        :param start_date: The initial day over which time a histogram
                           file is desired.
        :param end_date: The last day over which time a histogram file
                         is desired
        :param total_expense_file: The name and location which the histogram
                                   data is to be written

        This function reads the Daily_Expenses.csv file and transforms 
        its contents into a day by day breakdown for the total expendetures
        in each spending category.  The data is then written to a user
        defined csv file.  This file is necessary for creating a 
        pdf and cdf for monte carlo sampling.
        """
        df = self.read_daily_expenses_csv()
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        groceries = self._group_expenses_by_date(start_date, end_date, df, 'Groceries')
        misc = self._group_expenses_by_date(start_date, end_date, df, 'Misc')
        gas = self._group_expenses_by_date(start_date, end_date, df, 'Gas')
        restaurant = self._group_expenses_by_date(start_date, end_date, df, 
                                                  'Restaurant')
        bar = self._group_expenses_by_date(start_date, end_date, df, 'Bar')

        planned, date = self._group_expenses_by_date(start_date, end_date, df, 
                                                     'Planned Expense')
        information = {'Date': date, 'Bar': bar[0], 
                       'Groceries': groceries[0],
                       'Restaurant': restaurant[0], 
                       'Misc': misc[0],
                       'Gas': gas[0], 
                       'Planned': planned}
        df = pd.DataFrame(data=information)
        df = df.set_index("Date")
        df = df[::-1]
        df.to_csv(total_expense_file)
# ================================================================================
# Private-Like functions 

    def _group_expenses_by_date(self, start_date: str, end_date: str, 
                                df: pd.DataFrame, 
                                expense: str) -> Tuple[List[float], 
                                                       List[np.datetime64]]:
        """

        :param start_date: The start date in the format YYYY-MM-DD
        :param end_date: The end date in the format YYYY-MM-DD
        :param df: a pandas dataframe containing the expense history
        :param expense: The expense_type for which a histogram data
                        set is desired
        :return array, date: A tuple containing a list of daily expenses
                             and another list containing dates

        This function determines the total amount of money spend in a
        user defined `expense_type` category on each day over the user
        defined time-frame.  This data can be used for the development
        of a histogram in another function.
        """
        start_date = np.datetime64(start_date)
        end_date = np.datetime64(end_date)
        delta = np.timedelta64(1, 'D')
        array = []
        date = []
        while start_date <= end_date:
            new_df = df[(df['Date'] == start_date) & (df['Expense_Type'] == expense)]
            sum_num = new_df.Checking_Debit.sum()
            array.append(sum_num)
            date.append(start_date)
            start_date += delta
        return array, date
# ================================================================================
# ================================================================================


class MakeDistribution:
    """
    This class transforms a data array into discrete and continuous probability
    density functions and cumulative density functions
    """
    def __init__(self, data_array: np.ndarray):
        """

        :param data_array: The array of data to be transformed into
                           a pdf or cdf
        """
        self.data = data_array
# ---------------------------------------------------------------------------------------------

    def discrete_pdf(self, n_bins: int, normed=False) -> Tuple[np.ndarray, np.ndarray]:
        """

        :param n_bins: The number of histogram bins
        :param normed: True if the data is to be normalized
        :return bin_val, edges: A tuple containing the probability of finding a
                                value within a bin as an array of values and
                                the value of bin edges as an array of values
        """
        upper = max(self.data)
        lower = min(self.data)
        upper_num = np.sum(self.data == upper)
        edges = np.linspace(lower, upper, num=(n_bins + 1))
        bins = [[] for _ in range(n_bins)]
        for i in self.data:
            for j in range(n_bins):
                if edges[j] <= i < edges[j + 1]:
                    bins[j].append(float(1.0))
                    break
        bins[n_bins - 1].append(float(upper_num))
        if normed:
            bin_val = [np.sum(k) / len(self.data) for k in bins]
        else:
            bin_val = [np.sum(k) for k in bins]
      #  print(list(self.data))
      #  print(bin_val)
      #  print(edges)
        return np.array(bin_val, dtype=np.float64), edges
# ---------------------------------------------------------------------------------------------

    def continuous_pdf(self, n_bins: int, norm=False) -> Tuple[np.ndarray, np.ndarray]:
        """

        :param n_bins: The number of histogram bins
        :param norm: True if the data is to be normalized
        :return bin_val, middle: A tuple containing the probability of finding a
                                 value at a given point as an array and teh
                                 point where the value is found as an array.
        """
        bin_val, edges = self.discrete_pdf(n_bins, normed=norm)
        middle = [((edges[i + 1] - edges[i]) / 2.0) + edges[i] for i in range(len(edges) - 1)]
        return bin_val, np.array(middle, dtype=np.float64)
# ---------------------------------------------------------------------------------------------

    def discrete_cdf(self, n_bins: int, norm=False) -> Tuple[np.ndarray, np.ndarray]:
        """

        :param n_bins: The number of histogram bins
        :param norm: True if the data is to be normalized
        :return cum_bins, edges: A tuple containing the probability of finding a
                                 value in a given bin as an array and the edges of
                                 each bin as an array
        """
        bins, edges = self.discrete_pdf(n_bins, normed=norm)
        cum_bins = np.cumsum(bins)
        return cum_bins, edges
# ---------------------------------------------------------------------------------------------

    def continuous_cdf(self, n_bins: int, norm=False) -> Tuple[np.ndarray, np.ndarray]:
        """

        :param n_bins: The number of histogram bins
        :param norm: True if the data is to be normalized
        :return cum_bins, middle: A tuple containing the probability of finding a
                                 value in a given bin as an array and the edges of
                                 each bin as an array
        """
        bins, middle = self.continuous_pdf(n_bins, norm=norm)
        cum_bins = np.cumsum(bins)
        return cum_bins, middle
# ================================================================================ 
# ================================================================================ 
# eof
