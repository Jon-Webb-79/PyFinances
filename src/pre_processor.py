# Import necessary packages here
from read_files import ReadCSVFile
import numpy as np
import pandas as pd
import os
from typing import Tuple, List, Dict
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

    def read_total_expenses_csv(self, total_file: str) -> pd.DataFrame:
        """

        :param total_file: The name and location of the Total_Expenses.csv
                           file 

        This function opens the Total_Expenses.csv file and reads it 
        to a pandas dataframe 
        """
        headers = ['Date', 'Bar', 'Groceries', 'Misc', 'Gas', 'Restaurant']
        dat_type = [str, np.float32, np.float32, np.float32, 
                    np.float32, np.float32]
        df = self.read_csv_columns_by_headers(total_file, headers, dat_type)
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
        :return cum_bins: middle: A tuple containing the probability of finding a
                          value in a given bin as an array and the edges of
                          each bin as an array
        """
        bins, middle = self.continuous_pdf(n_bins, norm=norm)
        cum_bins = np.cumsum(bins)
        return cum_bins, middle
# ================================================================================
# ================================================================================


class CreateCDF(MakeDistribution, ReadCSVFile):
    """

    :param data_array: An array of pandas series containing numbers that
                       will be organized into a cdf for random sampling

    This class is tailered to accepr data from the Total_Expenses.csv
    class so it can transform the information into cdfs for sampling.  
    Future versions will also allow for the development of pdfs for
    plotting.
    """
    def __init__(self, data_array: np.ndarray):
        MakeDistribution.__init__(self, data_array)
# --------------------------------------------------------------------------------

    def create_cdf_file(self, hist_file_name: str, nbins: int) -> None:
        """

        :param hist_file_name: The name of the histogram file that data
                               will be written to 
        :param nbins: The number of bins to be used when creating a
                      cdf 
        :return None:

        This function will create a cumulative dsitribution file (cdf)
        with the information passed to the class and will write the
        data to a csv file
        """
        # Create the cdf
        bins, center = self.continuous_cdf(nbins, norm=True)
        # Write cdf to a pandas dataframe
        self._write_to_file(bins, center, hist_file_name)
# ================================================================================
# Private-Like Functions

    def _write_to_file(self, bins: np.float32, center: np.float32, 
                       hist_file_name: str) -> None:
        """

        :param bins: The probability associated with a bin 
        :param center: The center of each probability bin 
        :param hist_file_name: The name of the file that will be 
                               written to contain the cdf
        :return None:

        This function creates the csv file with the histogram data
        """
        headers = ['probability', 'center']
        dat_type = [np.float32, np.float32]
        information = {'probability': bins, 'center': center}
        df = pd.DataFrame(data=information)
        df = df.set_index("probability")
        df.to_csv(hist_file_name)
# ================================================================================ 
# ================================================================================ 


def hist_pre_processor(start_date: str, end_date: str, nbins: int, 
                       expense_file: str, total_file: str, 
                       file_path: str) -> None:
    # Create teh Total_Expenses.csv file 
    proc = ProcessDailyExpenseFile(expense_file)
    proc.group_expenses_by_date(start_date, end_date, total_file)

    # Read the Total_Expense.csv file for future processing
    df = proc.read_total_expenses_csv(total_file)
    
    # Instantiate CDF classes  
    bar = CreateCDF(df['Bar'])
    misc = CreateCDF(df['Misc'])
    rest = CreateCDF(df['Restaurant'])
    groc = CreateCDF(df['Groceries'])
    gas = CreateCDF(df['Gas'])

    # Create cdf files 
    bar.create_cdf_file(file_path + 'barcdf.csv', nbins)
    misc.create_cdf_file(file_path + 'misccdf.csv', nbins)
    rest.create_cdf_file(file_path + 'restcdf.csv', nbins)
    groc.create_cdf_file(file_path + 'groccdf.csv', nbins)
    gas.create_cdf_file(file_path + 'gascdf.csv', nbins)
# ================================================================================
# ================================================================================


class ReadMonteCarloFiles(ReadCSVFile):
    """

    This class contains functions that read the PyFinances input files
    """
    def read_cdf_file(self, file_name: str) -> pd.DataFrame:
        """
        
        :param file_name: The namve of the cdf file to be read 
        :return df: A dataframe containing the cdf information

        This function reads cdf files that contain the cumulative 
        distribution functions for various spending categories.  The
        file headers are **probability** and **center**, which represent
        the probability of spending, and the spending amount that is 
        commiserate with the probability.
        """
        headers = ['probability', 'center']
        dat_type = [np.float32, np.float32]
        df = self.read_csv_columns_by_headers(file_name, headers, dat_type)
        return df
# --------------------------------------------------------------------------------

    def read_bills_file(self, file_name: str) -> pd.DataFrame:
        """

        :param file_nae: The name and location of the bills.csv file 
        :return df: A dataframe containing the bills information

        This function reads the bills.csv file which contains the following
        headers **Day**, **Checking_Addition**, **Checking_Debit**, 
        **Savings_Addition**, **Savings_Debit**, and **Description**.
        """
        headers = ['Day', 'Checking_Debit', 'Checking_Addition', 
                  'Savings_Debit', 'Savings_Addition', 'Description']
        dat_type = [int, np.float32, np.float32, np.float32, np.float32, str]
        df = self.read_csv_columns_by_headers(file_name, headers, dat_type)
        return df
# --------------------------------------------------------------------------------

    def read_planned_expenses(self, file_name: str) -> pd.DataFrame:
        """

        :param  file_name: The name and location of the planned_expense.csv
                           file
        :return df: A dataframe containing the planned expenses information 

        This function reads the planned_epenses.csv file, which contains the 
        following headers, **Date**, **Checking_Debit**, **Checking_Addition**, 
        **Savings_Debit**, **Savings_Addition**, and **Description**.
        """
        headers = ['Date', 'Checking_Debit', 'Checking_Addition', 
                   'Savings_Debit', 'Savings_Addition', 'Description']
        dat_type = [str, np.float32, np.float32, np.float32, np.float32, str]
        df = self.read_csv_columns_by_headers(file_name, headers, dat_type)
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        return df
# --------------------------------------------------------------------------------

    def read_deductions_file(self, file_name: str) -> pd.DataFrame:
        """

        :param file_name: The name and locations of the Deductions.csv 
                          file 
        :return df: A pandas dataframe containing the contents of the 
                    Deductions file.

        This function reads the Deductions.csv file, which contains 
        all paycheck deductions.  It is assumed that these debits are
        deduction from the check prior to distribution.
        """
        headers = ['Amount', 'Description']
        dat_type = [np.float32, str]
        df = self.read_csv_columns_by_headers(file_name, headers, dat_type)
        return df
# ================================================================================
# ================================================================================


class CreateDates:
    """

    This class contains member functions as classmethods that will produce a 
    pandas DatetimeIndex of dates to support Monte Carlo iteration and
    pay date assessment.
    """
    @ classmethod
    def make_dates(cls, start_date: str, end_date: str) -> pd.DatetimeIndex:
        """

        :param start_date: The first date in a datetime index 
        :param end_date: The last date in a datetime index 
        :return dates: A datetime index 

        This function creates a list of dates in one dat intervals starting from
        the start_date to the end_date.  The list is returned as a pandas
        datetime index.
        """
        dates = pd.date_range(start=start_date, end=end_date)
        return dates
# --------------------------------------------------------------------------------
 
    @classmethod
    def make_pay_dates(cls, first_pay_date: str, frequency: str, 
                       end_date: str) -> pd.DatetimeIndex:
        """

        :param first_pay_date: The firs pay date in the formay YYYY-MM-DD
        :param frquency: The frequency of paychecks, WEEKLY, BI-WEEKLY, or
                         MONTHLY
        :param end_date: The last date for pay allocation.  This day does not 
                         have to fall on a pay date and instead represents the 
                         last day for Monte Carlo iteration.
        :return dates: A pandas series of pay dates

        This function produces a pandas data series of dates, where each date 
        represents a pay date.
        """
        if frequency.upper() == 'WEEKLY':
            dates = pd.date_range(start=first_pay_date, end=end_date, freq='W-FRI')
        elif frequency.upper() == 'BI-WEEKLY':
            dates = pd.date_range(start=first_pay_date, end=end_date, freq = '2W-FRI')
        else:    
            dates = pd.date_range(start=first_pay_date, end=end_date, freq='M')
        return dates
# ================================================================================
# ================================================================================


class MCPreProcessor(ReadMonteCarloFiles, CreateDates):
    """

    This class integrates all data necessary to run the Monte Carlo
    portion of the PyFinances program
    """
    def validate_hist_files(self, files: List[str], hist_func, 
                            input_dict: Dict, 
                            hist_location: str) -> None:
        """

        :param files: A list of the file names and path-lenghts
                      to the cdf files.
        :param hist_func: The function that will create the cdf files 
        :param input_dict: A dictionary containing the contents of the 
                           RunOptions file.
        :param hist_location: The location of the cdf files.

        This function will determine if the cdf files exist at the specified
        location.  If not, the function will execute the histogram pre
        processor and create the files.
        """
        file_exists = self._verify_hist_files(files)
        if not file_exists:
            hist_func(input_dict['hist_start'], 
                      input_dict['hist_end'], 
                      input_dict['nbins'], 
                      input_dict['daily_expense_file'], 
                      input_dict['total_expense_file'], 
                      hist_location)
# --------------------------------------------------------------------------------

    def create_dates(self, start_date: str, end_date: str, first_pay_date: str, 
                     pay_frequency: str) -> Tuple[pd.DatetimeIndex, 
                                                  pd.DatetimeIndex]:
        """

        :param start_date: The first date for Monte Carlo iteration in the
                           format YYYY-MM-DD.
        :param end_date: The last date for Monte Carlo iteration in the 
                         format YYYY-MM-DD.
        :param first_pay_date: The date whena first paycheck is recieved 
                               in the format YYYY-MM-DD.
        :param pay_frequency: 'WEEKLY', 'BI-WEEKLY', or 'MONTHLY'
        :return iter_dates, pay_dates: A tuple where the first element is a
                                       list of every date in the Monte Carlo 
                                       iteration, and the second element is
                                       a list of every pay date

        This function will provide the user with a list of all dates used in 
        the Monte Carlo iteration and a list of all pay dates in the Monte
        Carlo iteration.
        """
        iter_dates = self.make_dates(start_date, end_date)
        pay_dates = self.make_pay_dates(first_pay_date, pay_frequency, end_date)
        return iter_dates, pay_dates
# --------------------------------------------------------------------------------

    def read_bills(self, file_name: str) -> pd.DataFrame:
        """

        :param file_name: The name and location of the bills.csv file.
        :return df: A pandas dataframe containing the contents of the bills
                    file
        """
        df = self.read_bills_file(file_name)
        return df
# --------------------------------------------------------------------------------

    def read_expenses(self, file_name: str) -> pd.DataFrame:
        """

        :param file_name: The name and location of the planned_expenses.csv 
                          file.
        :return df: A pandas dataframe containing the contents of the 
                    planned_expenses file
        """
        df = self.read_planned_expenses(file_name)
        return df
# --------------------------------------------------------------------------------

    def read_cdf(self, files: str) -> List[pd.DataFrame]:
        """

        :param files: A list of filenames with the path lengths to each of the 
                      cdf files
        :return df_list: A list of dataframes, where each dataframe contains
                         the contents of one of the cdf files.
        """
        df_list = [self.read_cdf_file(i) for i in files]
        return df_list
# --------------------------------------------------------------------------------

    def pay_allocation(self, file_name: str, salary: np.float32, 
                       pay_frequency: str) -> np.float32:
        """

        :param file_name: The name and location of the csv file containng the
                          pay deductions 
        :param salary: The annual salary before any pay deductions 
        :param pay_frequency: The frequency of pay allocation, can be 
                              WEEKLY, BI-WEEKLY, or MONTHLY
        :return deducted_salary: The salary after it has been divided by the 
                                 pay periods and all deductions have been made

        This function determines the actual pay allocation per pay period 
        after deductions have been made.
        """
        df = self.read_deductions_file(file_name)
        deductions = df['Amount'].sum()
        updated_salary = self._determine_alloc(salary, pay_frequency)
        deducted_salary = updated_salary - deductions 
        return deducted_salary
# ================================================================================

    def _verify_hist_files(self, files: List[str]) -> bool:
        """

        :param files: A list of the file names and path-lengths to the 
                      cdf files.

        This function will test to see if all of the cdf files exist
        at the locations were they are supposed to.  If all files 
        exist the function will return True, if not it wll return
        False.
        """
        for i in files:
            exists = os.path.isfile(i)
            if not exists:
                return False
        return True
# --------------------------------------------------------------------------------

    def _determine_alloc(self, salary: np.float32, 
                         pay_frequency: str) -> np.float32:
        """

        :param salary: Annual salary before any dedcutions
        :param pay_frequency: The frequency of pay allocation, can be WEEKLY, 
                              BI-WEEKLY, or MONTHLY
        :return updated_salary: The salary divided by the pay frequency

        This function determines the pay allocation prior to deductions based
        on the frequency of pay allocation
        """
        if pay_frequency.upper() == 'WEEKLY':
            updated_salary = salary / 52.0
        elif pay_frequency == 'BI-WEEKLY':
            updated_salary = salary / 26.0
        else:
            updated_salary = salary / 12.0
        return updated_salary
# ================================================================================
# ================================================================================
# eof
