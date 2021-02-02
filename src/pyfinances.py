# Import necessary packages here
import sys 
import os
sys.path.insert(0, os.path.abspath('../src'))
from read_files import ReadRunOptionsFile
from pre_processor import hist_pre_processor, verify_hist_files
from pre_processor import ReadMonteCarloFiles, make_dates, make_pay_dates
# ================================================================================
# ================================================================================ 
# Date:    January 27, 2021
# Purpose: This file integrates all functions and classes necessary to run the 
#          PyFinances software package.

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2021, Jon Webb Inc."
__version__ = "1.0"
# ================================================================================ 
# ================================================================================ 
# Insert Code here


def pyfinances(runoptionsfile: str) -> None:
    # Read the RunOptions file
    inp = ReadRunOptionsFile(runoptionsfile)
    input_dict = inp.read_file()
    hist_location = '../data/hist/'

    # if run_hist is True then only create cdf files 
    if input_dict['run_hist'] == 'True':
        hist_pre_processor(input_dict['hist_start'], input_dict['hist_end'], 
                           input_dict['nbins'], 
                           input_dict['daily_expense_file'], 
                           input_dict['total_expense_file'], 
                           hist_location)
        return

    # verify that cdf files exist.  If not, then create them
    file_exist = verify_hist_files(hist_location)
    if not file_exist:
        hist_pre_processor(input_dict['hist_start'], input_dict['hist_end'], 
                           input_dict['nbins'], 
                           input_dict['daily_expense_file'], 
                           input_dict['total_expense_file'], 
                           hist_location)

    # read cdf files
    read = ReadMonteCarloFiles()
    barcdf = read.read_cdf_file(hist_location + 'barcdf.csv')
    gascdf = read.read_cdf_file(hist_location + 'gascdf.csv')
    groccdf = read.read_cdf_file(hist_location + 'groccdf.csv')
    misccdf = read.read_cdf_file(hist_location + 'misccdf.csv')
    restcdf = read.read_cdf_file(hist_location + 'restcdf.csv')

    # Read Planned Expenses

    # Read Bills

    # Determine Pay Allocation

    # Determine iteration Dates 
    dates = make_dates(input_dict['start_date'], input_dict['end_date'])

    # Determine pay dates
    pay_dates = make_pay_dates(input_dict['first_pay_date'], 
                               input_dict['pay_frequency'], 
                               input_dict['end_date'])
    print(pay_dates)
    # Monte Carlo pre-processor goes here

    # Monte Carlo engine goes here
# ================================================================================
# ================================================================================


if __name__ == "__main__":
    # file = '../data/input/RunOptions.txt'
    file = '../data/input/RunOptionsOne.txt'
    pyfinances(file)
# eof
