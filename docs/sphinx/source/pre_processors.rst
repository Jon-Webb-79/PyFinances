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

MakeDistribution
================

The `MakeDistribution` class acceps a data stream at instantiation.  The class
member functions can transform the data stream into a discrete or cumulative
probability density function and cumulative distribution function.  In each
case the calculated distributions can be normalized.

.. autoclass:: pre_processor.MakeDistribution
   :members:

CreateCDF
=========
The `CreateCDF` class inherits the `MakeDistribution` class to execute its
functionality.  This class specifically reads in column data from the 
`Total_Expenses.csv` file, that is transformed into a cdf and then
written to a file.

.. autoclass:: pre_processor.CreateCDF
   :members:
