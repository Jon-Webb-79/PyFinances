##############
Pre-Processors
##############

These functions and classes are used to pre-process information prior 
to entering the Monte Carlo calculation to estimate the values of the 
checking and savings accounts.  All of the software described in this 
section is maintained in the `pre_processors.py` file. 

ProcessDailyExpenseFile
=======================
The `ProcessDailyExpenseFile` class is encoded with the functionality that
allows it to open and read the `Daily_Expenses.csv` file.  This class
also has the functionality that allows it to transform the contents of
the `Daily_Expenses.csv` file into a day by day accounting of the cumulative
spending for each category, which is written to the `Total_Expenses.csv` file
and placed at the location of the users choice.

.. autoclass:: pre_processor.ProcessDailyExpenseFile
   :members:

