##########
read_files
##########
This section describes the functions and classes in the `read_files.py` file.

ReadTextFileKeywords
=====================
This class is used to read a text file by its keywords.  The member functions will
open a file and search it for a user defined keyword.  if the keyword is found, 
the function will read the text string to the right of the keyword into 
memory.  The various functions will control the data type of the keyword.

.. autoclass:: read_files.ReadTextFileKeywords
   :members:

ReadRunOptionsFile
==================
This class is used to read the `RunOptions.txt` file, which controls the 
behavior of the PyFinances computer program.  The `ReadRunOptionsFile class`
inherits the `ReadTextFiles` class in order to execute its functionality.  
This class is pre-programmed to look for the keywords which are expected
in the `RunOptions.txt` file.

.. autoclass:: read_files.ReadRunOptionsFile
   :members:

read_csv_columns_by_headers
===========================
This function is used to read csv files, which have structured and defined
headers.  The data is read into a numpy dataframe, in order to make it easier
and faster for a user to access the data read from the csv file.

.. autofunction:: read_files.read_csv_columns_by_headers

read_daily_expenses_csv
=======================
This function is used to read the `Daily_Expenses.csv` file, which is necessary
for the creation of the `Total_Expenses.csv` file.  The user only has to pass
the name and location of the file, the function is pre-programmed to 
understand the structure of the document.


.. autofunction:: read_files.read_daily_expenses_csv

