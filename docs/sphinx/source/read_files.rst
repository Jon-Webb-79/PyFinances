##########
read_files
##########
The functions and classes described in this section are used to read
ASCII based text files, to include `.txt` files and `.csv` files.  All of
the code described in this section is maintained in the `read_files.py` file.

ReadTextFileKeywords
====================
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

ReadCSVFile
===========
This class is used to read csv files as relevant to the PyFinances software suite.

.. autoclass:: read_files.ReadCSVFile
   :members:
