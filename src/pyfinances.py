# Import necessary packages here
import sys 
import os
sys.path.insert(0, os.path.abspath('../src'))
from read_files import ReadRunOptionsFile
from pre_processor import hist_pre_processor
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


def pyfinances(runoptionsfile: str):
    # Read the RunOptions file
    inp = ReadRunOptionsFile(runoptionsfile)
    input_dict = inp.read_file()

    if input_dict['run_hist'] == 'True':
        hist_pre_processor(input_dict['hist_start'], input_dict['hist_end'], 
                           input_dict['nbins'], 
                           input_dict['daily_expense_file'], 
                           input_dict['total_expense_file'], 
                           '../data/hist/')
    else:
        # Monte Carlo pre-processor goes here

        # Monte Carlo engine goes here
        pass
# ================================================================================
# ================================================================================


if __name__ == "__main__":
    file = '../data/input/RunOptions.txt'
    pyfinances(file)
# eof
