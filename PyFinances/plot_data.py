# Import necessary packages here
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# ================================================================================
# ================================================================================ 
# Date:    February 6, 2021
# Purpose: This function will plot all of the data created by the PyFinances
#          software suite

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2021, Jon Webb Inc."
__version__ = "0.1.0"
# ================================================================================ 
# ================================================================================ 
# Insert Code here


def plot_func(df: pd.DataFrame, file_name: str):
    # Determine the time scale and choose plotting options
    delta = (df['Date'][max(df.index)] - df['Date'][min(df.index)])
    delta = delta / np.timedelta64(1, 'D')

    fig, td_plot = plt.subplots()
    matplotlib.rc('xtick', labelsize=12)
    matplotlib.rc('ytick', labelsize=12)
    td_plot.set_xlabel('Date', fontsize=14)
    td_plot.set_ylabel('$', fontsize=14)
    
    if delta <= 15:
        myfmt = mdates.DateFormatter('%d')
        td_plot.xaxis.set_major_locator(mdates.DayLocator())
    elif delta <= 90:
        myfmt = mdates.DateFormatter('%b-%y')
        td_plot.xaxis.set_major_locator(mdates.MonthLocator())
    else:
        myfmt = mdates.DateFormatter('%b-%y')
        td_plot.xaxis.set_major_locator(plt.MaxNLocator(4))
    df = df.set_index('Date') 
    td_plot.fill_between(df.index, df['Upper'], df['Lower'],
                         color='red', interpolate=True)
    td_plot.plot(df.index, df['Checking_Mean'], label='Mean', color='black')
    td_plot.xaxis.set_major_formatter(myfmt)
    td_plot.legend()
    plt.savefig(file_name)
    plt.close()
# ================================================================================ 
# ================================================================================ 
# eof
