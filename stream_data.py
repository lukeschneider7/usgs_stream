import numpy as np
import pandas as pd
import os
from tkinter import simpledialog
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
os.getcwd()
os.chdir("/Users/luke/Documents/projects")


# Ask user for input
user_inp = input("Enter letter for stream you want to analyze: \n A) Difficult Run \n " 
                                              "B) James River \n C) Smith Creek \n D) Snakeden Branch \n E) the_glade")

# Name filepath based on user input
filepath = '' 
if user_inp == "A":
    filepath = 'difficult_run.csv'
    rows_to_skip = 55
elif user_inp == "B":
    filepath = 'james_river.csv'
    rows_to_skip = 55
elif user_inp == "C":
    filepath = 'smith_creek.csv'
    rows_to_skip = 47
elif user_inp == "D":
    filepath = 'snakeden_branch.csv'
    rows_to_skip = 47
elif user_inp == "E":
    filepath = 'the_glade.csv'
    rows_to_skip = 47

# Read in and print first five rows of water data
df = pd.read_csv(filepath, skiprows=rows_to_skip, sep="\t")
data = df.iloc[1:] # Revmove 5s, 15s, 20d row of nonsense below header
data.head()

# # Show Column names
# pd.set_option('display.max_seq_items', None) # No limit on items in list
# print(data.columns[0:10]) # show just columns 
# data.info(verbose=True) # show columns with data types

# # pd.set_option to limit output and show datatypes
# pd.set_option('display.max_columns', 41) #display a maximumn of 10 columns
# pd.set_option('display.max_rows', 8) #display a maximumn of 10 rows
# data[0:5]

# pd.set_option('display.max_rows', 6) # Can also be 'None' for second arg
# data.dtypes # Show data types

# Descripitive statistics for specific column
# Convert even-indexed columns to integers
for column in data.columns[1::2]:  # Select columns at even indices
    data[column] = pd.to_numeric(data[column], errors='coerce')
data.dtypes

# access median stats basic on column name e
total_nitrogen_median = data.loc[:, data.columns.str.endswith('99133_00008')]
discharge_mean = data.loc[:, data.columns.str.endswith('00060_00003')]
dissolved_oxygen_median = data.loc[:, data.columns.str.endswith('00300_00008')]
ph_median = data.loc[:, data.columns.str.endswith('00400_00008')]
temperature_median = data.loc[:, data.columns.str.endswith('00010_00008')]
specific_conductance_median = data.loc[:, data.columns.str.endswith('00095_00008')]
turbidity_median = data.loc[:, data.columns.str.endswith('63680_00008')]

# Strip Dates from data frame and plots stats over time 
dates = [datetime.strptime(x, '%Y-%m-%d') for x in data['datetime']]
plt.subplot(2, 2, 1)
plt.plot(dates, ph_median)
plt.subplot(2, 2, 2)
plt.plot(dates, discharge_mean)
plt.subplot(2, 2, 3)
plt.plot(dates, dissolved_oxygen_median)
plt.subplot(2, 2, 4)
plt.plot(dates, total_nitrogen_median)
plt.xticks(rotation=45)