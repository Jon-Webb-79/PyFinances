# Import necessary packages here
import numpy as np
from pre_processor import ReadMonteCarloFiles
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


class MonteCarloExec(ReadMonteCarloFiles):
    """

    This class contains functions that are used during the PyFinances
    Monte Carlo iteration process
    """
    def determine_pay_allocation(self, salary: np.float32, pay_frequency: str,
                                 file_name: str):
        """

        :param salary: The annualy salary before any pay deductions
        :param pay_frequency: The frequency of pay allocation, can be WEEKLY, 
                              BI-WEEKLY, or MONTHLY
        :param file_name: THe name and location of the csv file containing the
                          pay deduction information.
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
# Private-Like functions 

    def _determine_alloc(self, salary: np.float32, pay_frequency: str):
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
