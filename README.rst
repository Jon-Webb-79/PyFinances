**********
PyFinances
**********

The PyFinances software suite is written to analyze a users historical spending trends
and then to use that information to preduct the date-dependent future value of a 
users checking and savings account.  The software package is predicated on the user
being a salaried employee that has a single checking and savings account. 

Contributing
############
Pull requests are welcome.  For major changes, please open an issue first to discuss
what you would like to change.  Please make sure to include and update tests
as well as relevant doc-string and sphinx updates.

License
#######
The License is included in the **project_name** package

Requirements
############
Python 3.8 or greater
numpy==1.19.5

Installation
############
In order to download this repository from github, follow these instructions

1. Ensure you have .git installed on your computer
2. At your desired location create a directory titled ``project_name``
3. Open a terminal (Bash, zsh, Linux, or DOS) and cd to the ``project_name`` directory and type
   ``close https://github.com/Jon-Webb-79/Project_Name.git project_name``
4. Install with pip3
   ``pip3 install -r requirements``

User Guide
##########
The user will need to maintain a .csv file that tracks their daily spending by
the categories of *Bills*, *Misc*, *Bar*, *Groceries*, *Gas*, *Restaurant* and
*Planned Expense*.  The user may also want to track spending by *Fed Taxes*, 
and *State Taxes*.  In my case I have titled the file `Daily_Expenses.csv`.
An example of a `Daily_Expenses.csv` is profided below.


.. list-table:: Daily_Expenses.csv
   :widths: 10 10 10 10 10 10 10 10
   :header-rows: 1

   * - Date
     - Checking_Debit
     - Checking_Addition
     - Savings_Debit
     - Savings_Addition
     - Expense_Type
     - Vendor
     - Description
   
   * - 01/25/2021
     - 64.90
     - 0.0
     - 0.0
     - 0.0
     - Misc 
     - Target
     - Blankets
   
   * - 01/25/2021
     - 32.18
     - 0.0
     - 0.0
     - 0.0
     - Bills
     - Century Link
     - Internet Bill
   
   * - 01/24/2021
     - 0.0
     - 1000.0
     - 0.0
     - 0.0
     - Paycheck
     - Company
     - None

RunOptions File
===============
The RunOptions file controls the behavior of the entire PyFinances software and is
the users interface to the program.  The RunOptions.txt file must first be configured
by the user to develop the appropriate histogram files, which will be read by
the program later when executed in Monte Carlo mode.  A RunOptions.txt file must
contain a specific key word or phrase followed by the information that the program
will read.  For example, in order to configure the program to develop a set of
histogram files, the RunOptions.txt might look something like the example below.

.. code-block:: text

   Run Histogram: True
   Bins: 60
   Hist Start Date: 03/01/2020
   Hist End Date: 02/28/2021
   Daily Expense File: ../data/Daily_Expense.csv
   Total Expense File: ../data/total_expenses.csv
   Histogram Location: ../data/histograms 

In the example shown above, the term `Run Histogram:` is a key word.  The PyFinances software
will open the `RunOptions.txt` file and look for this keyword.  If it finds the keyword, it
will read the text string immediately to the right, which in this case is `True`.  Since the 
response to the keyword `Run Histogram:` is `True` it means that the code will create 
histogram files, which are necessary for a later execution of the Monte Carlo calculation.  The
keywords in this version of the `RunOptions.txt` file have the following meaning.

- **Run Histogram:** `True` if the code is to develop histograms or `False` if the code will complete a Monte Carlo calculation.
- **Bins:** The number of bins to be used in the probability and cumulative distribution functions that are sampled for the Monte Carlo calculation.
- **Hist Start Date:** The start date for the development of PDFs and CDFs. This date must exist within the `Daily_Expenses.csv` file.
- **Hist End Date:** The end date for the development of PDFs and CDFs.  This date must exist within the `Daily_Expenses.csv` file.
- **Daily Expense File:** The location and name of the daily expense file.  In this example I have named it the `Daily_Expenses.csv` file.
- **Total Expense File:** The name and location of the csv file that will contain the day by day cumulative spending for each category.  This file
 will be created by the program.  In this example I gave the file the name `total_expenses.csv`
- **Histogram Location:** The location where histogram files will be created.  These files contain cumulative distribution data that will be 
used to generate random samples for spending.  In this case, I hae manually created a directory titled 
histograms in the data directory to store the csv files.

  Once you have developed Histogram files, then you must reconfigure the `RunOptions.txt` file to execute the Monte Carlo
  calculations with the histogram files.  In order to do this you can reconfigure the file to look like the example 
  below.

.. code-block:: text

   Sample Size: 1000 
   Start Date: 03/01/2021
   End Date: 02/28/2022
   Checking Start Value: 38000.0
   Savings Start Value: 4500.0
   Annual Salary: 95000.0
   Pay Frequency: bi-weekly
   First Pay Date: 03/05/2021
   Total Expense File: ../data/total_expenses.csv
   Planned Expense File: ../data/planned_expenses.csv
   Bills File: ../data/bills.csv
   Deductions File ../data/deductions.csv
   Run Histogram: False
   Bins: 60
   Hist Start Date: 03/01/2020
   Hist End Date: 02/28/2021
   Daily Expense File: ../data/Daily_Expense.csv
   Histogram Location: ../data/histograms
   Output File: ../data/output

The file above has the same keywords as the first example, with addtion of the following key wordsz

- **Sample Size:** The number of Monte Carlo samples to use in the calculation.  The fidelity increases with sample size.
- **Start Date:** The Start date for the predictions of financial values
- **End Date** The End date for the prediction of financial values
- **Checking Start Value:** The initial value of the checking account on the start date
- **Savings Start Value:** The initial value of the savings account on the start date
- **Annual Salary:** The users annual salary before taxes and deductions
- **Pay Frequency:** The frequency at which the user recievs pay checks.  The input must be weekly, bi-weekly, bi-monthly, or monhly
- **First Pay Date:** The date the first paycheck is recieved.  If Pay Frequency is bi-monthly or monthly, the first pay date must be the 15th of hte last day of the month
- **Total Expense File:** A .csv file that contains the day by day breakdown of spending for all categories.  The user will not create this file, but must
  specify the name and location of this file.
- **Planned Expense File:** A .csv file containing the planned expenses for the calculated time frame that are not covered as random espenses, bills
  or pay deductions.
- **Bills File:** The name and location of the .csv file containing bill information.
- **Deductions File:** The name and location of the .csv file containing paycheck deduction information
- **Run Histogram:** `False` if the user is executing a Monte Carlo calculation, or it can be neglected from the `RunOptions.txt` file as 
  it is defaulted to `False`.  If the files do not exist, the Monte Carlo code will recreate them based on the following inputs.
- **Bins:** The number of bins to be used in the probability and cumulative distribution functions that are sampled for the Monte Carlo calculation.
- **Hist Start Date:** The start date for the development of PDFs and CDFs. This date must exist within the `Daily_Expenses.csv` file.
- **Hist End Date:** THe end date for the development of PDFs and CDFs.  This date must exist within the `Daily_Expenses.csv` file.
- **Daily Expense File:** The location and name of the daily expense file.  In this example I have named it the `Daily_Expenses.csv` file.
- **Histogram Location:** The location where histogram files will be created.  These files contain cumulative distribution data that will be 
 used to generate random samples for spending.  In this case, I hae manually created a directory titled 
 istograms in the data directory to store the csv files.
- **Output File:** This is the location where all output files will be stored.


Planned Expense File
====================
The User must create a planned expense file at the location and name assigned in the `RunOptions.txt` file.  It is best just
to use the name `Planned_Expenses.csv`.  The file should have the following format.

.. list-table:: Planned_Expense.csv
   :widths: 10 15 15 15 15 10
   :header-rows: 1

   * - Date
     - Checking_Debit
     - Checking_Addition
     - Savings_Debit
     - Savings_Addition
     - Description
   
   * - 01/25/2021
     - 640.90
     - 0.0
     - 0.0
     - 0.0
     - Vacation
   
   * - 01/25/2021
     - 250.18
     - 0.0
     - 0.0
     - 0.0
     - New Camera
   
   * - 01/24/2021
     - 0.0
     - 1000.0
     - 0.0
     - 0.0
     - Medical Visit

Bills File
==========
The bills file has a format similar to the Planned Expense File, but assumes that bills re-occur at the same 
time of each month, so the date is replaced with day, and looks similar to the example below.

.. list-table:: Bills.csv
   :widths: 10 15 15 15 15 10
   :header-rows: 1

   * - Day
     - Checking_Debit
     - Checking_Addition
     - Savings_Debit
     - Savings_Addition
     - Description
   
   * - 01
     - 1200.90
     - 0.0
     - 0.0
     - 0.0
     - Rent
   
   * - 22
     - 120.00
     - 0.0
     - 0.0
     - 0.0
     - Phone Bill
   
   * - 28
     - 0.0
     - 420.0
     - 0.0
     - 0.0
     - Car Payment

Deductions File
===============
The deductions file can be named and placed whever the user wants it; however, it is recommended that the 
user of hte software titles the file the `Deductions.csv` file.  The file should have the following 
format.

.. list-table:: Deductions.csv
   :widths: 15 15
   :header-rows: 1

   * - Amount
     - Description
   
   * - 84.50
     - Medical Deductions
   
   * - 150.0
     - 401k
   
   * - 1840.0
     - Federal Income Taxes

Running the Code
================
The PyFinances software can be run py using the following function

.. code-block:: python

   > from PyFinances.pyfinances import pyfinances
   > run_file = 'input_files/RunOptions.txt'
   > pyfinances(run_file)

The software will produce a csv file with a date dependent estimation of the finances 
titled estimates.csv in the location listed in the RunOptions.txt file.  In addition
the software will also produce a plot titled estimates.png in the location listed in
the RunOptions file.

