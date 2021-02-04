 # Import necessary packages here
import sys 
import os
sys.path.insert(0, os.path.abspath('../src'))
from read_files import ReadRunOptionsFile
from pre_processor import hist_pre_processor, MCPreProcessor
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
# --------------------------------------------------------------------------------
# Execute the histogram pre-processor

    # if run_hist is True then only create cdf files 
    if input_dict['run_hist'] == 'True':

        hist_pre_processor(input_dict['hist_start'], input_dict['hist_end'], 
                           input_dict['nbins'], 
                           input_dict['daily_expense_file'], 
                           input_dict['total_expense_file'], 
                           hist_location)
        return
# --------------------------------------------------------------------------------
# Execute the Monte Carlo Pre-processor

    # verify that cdf files exist.  If not, then create them
    files = ['groccdf.csv', 'misccdf.csv', 'gascdf.csv', 
             'barcdf.csv', 'restcdf.csv']
    files = [hist_location + i for i in files]
    mc_pre = MCPreProcessor()
    mc_pre.validate_hist_files(files, hist_pre_processor, 
                               input_dict, hist_location)
    
    # read files 
    bills_df = mc_pre.read_bills(input_dict['bills_file'])
    expenses_df = mc_pre.read_expenses(input_dict['planned_expense_file'])
    cdf_list = mc_pre.read_cdf(files)

    # Determine Pay Allocation
    pay_aloc = mc_pre.pay_allocation(input_dict['deductions_file'], 
                                    input_dict['annual_salary'], 
                                    input_dict['pay_frequency'])

    # Determine iteration Dates 
    iter_dates, pay_dates = mc_pre.create_dates(input_dict['start_date'], 
                                                input_dict['end_date'], 
                                                input_dict['first_pay_date'], 
                                                input_dict['pay_frequency'])
    # Monte Carlo pre-processor goes here

    # Monte Carlo engine goes here
# ================================================================================
# ================================================================================


if __name__ == "__main__":
    # file = '../data/input/RunOptions.txt'
    file = '../data/input/RunOptionsOne.txt'
    pyfinances(file)
# eof
