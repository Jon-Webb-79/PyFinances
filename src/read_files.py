# Import necessary packages here
import os
import sys
from calendar import monthrange
import numpy as np
from typing import List, Dict, Tuple
import pandas as pd
# ================================================================================
# ================================================================================
# Date:    January 24, 2021
# Purpose: This file contains classes and functions that assist in reading
#          ASCII based text files and databases

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2021, Jon Webb Inc."
__version__ = "1.0"
# ================================================================================
# ================================================================================
# Insert Code here


class ReadTextFileKeywords:
    """
    A class to find keywords in a text file and the the variable(s)
    to the right of the key word.  This class must inherit the
    ``FileUtilities`` class


    :param file_name: The name of the file being read to include the
                      path-link

    For the purposes of demonstrating the use of this class, assume
    a text file titled ``test_file.txt`` with the following contents.


    .. code-block:: text

        sentence: This is a short sentence!
        float: 3.1415 # this is a float comment
        double: 3.141596235941 # this is a double comment
        String: test # this is a string comment
        Integer Value: 3 # This is an integer comment
        float list: 1.2 3.4 4.5 5.6 6.7
        double list: 1.12321 344.3454453 21.434553
        integer list: 1 2 3 4 5 6 7
    """
    def __init__(self, file_name: str):
        self.file_name = file_name
        if not os.path.isfile(file_name):
            sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name,
                                     ' does not exist'))
# ----------------------------------------------------------------------------

    def read_double(self, key_words: str) -> np.float64:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The float value following the **key_word** on the
                      text file.  This variable is returned as a
                      np.float64 data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the first data point following the key word(s) on the text file as a
        float value.  The text file can also contain a comment line
        following the variable being read.  For example we could use this
        class to read the double value 3.141596235941 in the following manner.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > double_data = dat.read_double('double:')
            > print(double_data)
            3.141596235941
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.float64(values[0])
# ----------------------------------------------------------------------------

    def read_double_list(self, key_words: str) -> List[np.float64]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      string values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the data points following the key word(s) on the text file as a
        numpy.float64 value. The text file can also contain a comment
        line following the variable being read.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > str_data = dat.read_double_list('double list:')
            > print(str_data)
            [1.12321, 344.3454453, 21.434553]
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [np.float64(value) for value in values]
        return values
# ----------------------------------------------------------------------------

    def read_float(self, key_words: str) -> np.float32:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The float value following the **key_word** on the
                      text file.  This variable is returned as a
                      np.float32 data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the first data point following the key word(s) on the text file as
        a float value. The text file can also contain a comment line
        following the variable being read.  For example we could use this
        class to read the float value 3.1415 in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > float_data = dat.read_float('float data:')
           > print(float_data)
           3.1415
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.float32(values[0])
# ----------------------------------------------------------------------------

    def read_float_list(self, key_words: str) -> List[np.float32]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      numpy.float32 values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the data points following the key word(s) on the text file as a
        float value. The text file can also contain a comment line following
        the variable being read.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > float_data = dat.read_float_list('float list')
            > print(float_data)
            [1.2, 3.4, 4.5, 5.6, 6.7]
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [np.float32(value) for value in values]
        return values
# ----------------------------------------------------------------------------

    def read_integer(self, key_words: str) -> np.int32:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The integer value following the **key_word** on the
                      text file.  This variable is returned as a np.int32
                      data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the first data point following the key word(s) on the text file as
        a integer value. The text file can also contain a comment line
        following the variable being read.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > int_data = dat.read_float('Integer Value')
           > print(int_data)
           3
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.int32(values[0])
# ----------------------------------------------------------------------------

    def read_integer_list(self, key_words: str) -> List[np.int32]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      numpy.float32 values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the data points following the key word(s) on the text file as an
        integer value. The text file can also contain a comment line following
        the variable being read.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > float_data = dat.read_integer_list('integer list:')
            > print(float_data)
            [1, 2, 3, 4, 5, 6, 7]
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [np.int32(value) for value in values]
        return values
# ----------------------------------------------------------------------------

    def read_sentence(self, key_words: str) -> str:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The data following the **key_word** on the text file.
                      The data is returned as a continuous string value

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the data following the key word(s) on the text file as a continuous
        string. The text file can also contain a comment line following the
        variable being read.  For example we could use this class to read
        the integer value `This is a short sentence!` in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > str_data = dat.read_float('sentence:')
           > print(str_data)
           'This is a short sentence!'
        """
        input_words = key_words.split()
        with open(self.file_name) as Input_File:
            lines = Input_File.readlines()
            for line in lines:
                variable = line.split()
                counter = 0
                for i in range(len(input_words)):
                    if input_words[i] != variable[i]:
                        break
                    else:
                        counter += 1
                if counter == len(input_words):
                    start = len(input_words)
                    end = len(variable)
                    word = ''
                    for i in range(start, end):
                        word = word + ' ' + variable[i]
                    return word.lstrip()
        sys.exit('{}{}{}'.format(key_words, " Keywords not found in ",
                                 self.file_name))
# ----------------------------------------------------------------------------

    def read_string(self, key_words: str) -> str:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string value following the **key_word** on the
                      text file.  This variable is returned as a str
                      data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the first data point following the key word(s) on the text file
        as a string value. The text file can also contain a comment line
        following the variable being read.  For example we could use this
        class to read the string value `test` in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > str_data = dat.read_float('String:')
           > print(str_data)
           'test'
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return str(values[0])
# ----------------------------------------------------------------------------

    def read_string_list(self, key_words: str) -> List[str]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      string values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the data points following the key word(s) on the text file as a
        string value. The text file can also contain a comment line following
        the variable being read.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > str_data = dat.read_string_list('sentence:')
            > print(str_data)
            ['This', 'is', 'a', 'short', 'sentence!']
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [str(value) for value in values]
        return values
# ================================================================================
# ================================================================================


class ReadRunOptionsFile(ReadTextFileKeywords):
    """

    :param file_name: The name of the file containing keywords that will
                      be read by this class.  The file_name must be input
                      with the path length to the file.

    This class will read a RunOptions.txt file containing all information
    describing how the PyFinances software package should run.
    """
    def __init__(self, file_name: str):
        self.file_name = file_name
        ReadTextFileKeywords.__init__(self, file_name)
# --------------------------------------------------------------------------------

    def read_file(self) -> Dict:
        """

        :return input_dict: A dictionary containing all information necessary
                            to run the PyFinances software package.

        This function reads the RunOptions.txt file to determine
        how the software package fill function.
        """
        # Dictionary will act as a container to pass between programs
        input_dict = {'run_hist': 'False',
                      'nbins': 20,
                      'hist_start': 'False',
                      'hist_end': 'False',
                      'sample_size': 0,
                      'start_date': 'False',
                      'end_date': 'False',
                      'checking_start_value': 0.0,
                      'savings_start_value': 0.0,
                      'annual_salary': 0.0,
                      'pay_frequency': 'Never',
                      'first_pay_date': 'False',
                      'daily_expense_file': 'False',
                      'total_expense_file': 'False',
                      'planned_expense_file': 'False',
                      'bills_file': 'False',
                      'deductions_file': 'False',
                      'hist_location': 'NA'}

        # - Read input for produce histogram files. If the uer enters
        #   True for Run Histogram, then the code will only exeucte
        #   the histogram building functions and not the Monte Carlo
        #   calculation.
        try:
            input_dict['run_hist'] = self.read_string('Run Histogram:')
        except SystemExit:
            pass
        if input_dict['run_hist'] == 'True':
            input_dict['nbins'] = self.read_integer('Bins:')
            input_dict['hist_start'] = self.read_string('Hist Start Date:')
            input_dict['hist_end'] = self.read_string('Hist End Date:')
            input_dict['daily_expense_file'] = \
                self.read_string('Daily Expense File:')
            input_dict['total_expense_file'] = \
                    self.read_string('Total Expense File:')
            input_dict['hist_location'] = \
                    self.read_string('Histogram Location:')
        # Read input for monte classrlo process
        else:
            input_dict['nbins'] = self.read_integer('Bins:')
            input_dict['hist_start'] = self.read_string('Hist Start Date:')
            input_dict['hist_end'] = self.read_string('Hist End Date:')
            input_dict['daily_expense_file'] = \
                self.read_string('Daily Expense File:')
            input_dict['sample_size'] = self.read_integer('Sample Size:')
            input_dict['start_date'] = self.read_string('Start Date:')
            input_dict['end_date'] = self.read_string('End Date:')
            input_dict['checking_start_value'] = \
                self.read_float('Checking Start Value:')
            input_dict['savings_start_value'] = \
                self.read_float('Savings Start Value:')
            input_dict['annual_salary'] = self.read_float('Annual Salary:')
            input_dict['pay_frequency'] = self.read_string('Pay Frequency:')
            input_dict['first_pay_date'] = self.read_string('First Pay Date:')
            input_dict['total_expense_file'] = \
                self.read_string('Total Expense File:')
            input_dict['planned_expense_file'] = \
                self.read_string('Planned Expense File:')
            input_dict['bills_file'] = self.read_string('Bills File:')
            input_dict['deductions_file'] = \
                self.read_string('Deductions File:')

            # Check values
            self._validate_frequency(input_dict['pay_frequency'])
            self._validate_first_pay_date(input_dict['first_pay_date'], 
                                         input_dict['pay_frequency'])
            input_dict['hist_location'] = \
            self.read_string('Histogram Location:')
        return input_dict
# ================================================================================

    def _validate_frequency(self, freq: str) -> None:
        """

        :param freq: The pay frequency
        :return None:

        This function validates the user pay_frequency input
        """
        accepted = ['WEEKLY', 'MONTHLY', 'BI-WEEKLY']
        msg = "FATAL ERROR: Pay Frequency must be one of the following "
        message = '{}{}'.format(msg, accepted)
        if freq.upper() not in accepted:
            sys.exit(message)
# --------------------------------------------------------------------------------

    def _validate_first_pay_date(self, first_pay_date: str,
                                 pay_freq: str) -> None:
        """

        :param first_pay_date: The user entered first pay date 
        :param pay_freq: The user entered pay frequency
        :return None:

        This function validates the user first_pay_date entry and
        ensures that it matches the pay allocation dates.
        """
        year = int(first_pay_date[0:4])
        month = int(first_pay_date[5:7])
        dates = monthrange(year, month)
        acceptable_dates = [15, dates[1]]
        if pay_freq.upper() == 'MONTHLY' or pay_freq.upper() == 'BI-MONTHLY':
            if first_pay_date not in acceptable_dates:
                msg = 'FATAL ERROR: First Pay Date must be the 15th or the '
                msg += 'last day of the month if the Pay Frequency is '
                msg += 'Bi-monthly or monthly'
                sys.exit(msg)
# ================================================================================
# ================================================================================


class ReadCSVFile:
    """

    This class contains functions that read csv files as relevant to
    the PyFinances software suite.
    """
    @classmethod
    def read_csv_columns_by_headers(cls, file_name: str, headers: List[str],
                                    data_type: List[type],
                                    skip: int = 0) -> pd.DataFrame:
        """

        :param file_name: The file name to include path-link
        :param headers: A list of the names of the headers that contain
                        columns which will be read
        :param data_type: A list containing the data type of each column.  Data
                          types are limited to ``numpy.int64``, ``numpy.float64``,
                          and ``str``
        :param skip: The number of lines to be skipped before reading data
        :return df: A pandas dataframe containing all relevant information

        This function assumes the file has a comma (i.e. ,) delimiter, if
        it does not, then it is not a true .csv file and should be transformed
        to a text function and read by the xx function.  Assume we have a .csv
        file titled ``test.csv`` with the following format.

        .. list-table:: test.csv
          :widths: 6 10 6 6
          :header-rows: 1

          * - ID,
            - Inventory,
            - Weight_per,
            - Number
          * - 1,
            - Shoes,
            - 1.5,
            - 5
          * - 2,
            - t-shirt,
            - 1.8,
            - 3,
          * - 3,
            - coffee,
            - 2.1,
            - 15
          * - 4,
            - books,
            - 3.2,
            - 48

        This file can be read via the following command

        .. code-block:: python

           > file_name = 'test.csv'
           > headers = ['ID', 'Inventory', 'Weight_per', 'Number']
           > dat = [int, str, float, int]
           > obj = ReadCSVFile()
           > df = obj.read_csv_columns_by_headers(file_name, headers, dat)
           > print(df)
               ID Inventory Weight_per Number
            0  1  shoes     1.5        5
            1  2  t-shirt   1.8        3
            2  3  coffee    2.1        15
            3  4  books     3.2        40

        This function can also use the `skip` attributed read data when the
        headers are not on the first line.  For instance, assume the following csv file;

        .. list-table:: test1.csv
          :widths: 16 8 5 5
          :header-rows: 0

          * - This line is used to provide metadata for the csv file
            -
            -
            -
          * - This line is as well
            -
            -
            -
          * - ID,
            - Inventory,
            - Weight_per,
            - Number
          * - 1,
            - Shoes,
            - 1.5,
            - 5
          * - 2,
            - t-shirt,
            - 1.8,
            - 3,
          * - 3,
            - coffee,
            - 2.1,
            - 15
          * - 4,
            - books,
            - 3.2,
            - 48

        This file can be read via the following command

        .. code-block:: python

           > file_name = 'test1.csv'
           > headers = ['ID', 'Inventory', 'Weight_per', 'Number']
           > dat = [int, str, float, int]
           > obj = ReadCSVFile()
           > df = obj.read_csv_columns_by_headers(file_name, headers, dat, skip=2)
           > print(df)
               ID Inventory Weight_per Number
            0  1  shoes     1.5        5
            1  2  t-shirt   1.8        3
            2  3  coffee    2.1        15
            3  4  books     3.2        40
        """
        if not os.path.isfile(file_name):
            sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
        dat = dict(zip(headers, data_type))
        df = pd.read_csv(file_name, usecols=headers, dtype=dat, skiprows=skip)
        return df 
# ================================================================================
# ================================================================================
# eof
