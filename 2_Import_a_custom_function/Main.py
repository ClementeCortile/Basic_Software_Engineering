
#In this directory Utilities.py contains a list of useful functions!

#Let's start by importing our environment libraries
import os
import sys
import numpy as np
import pandas as pd

#We can use os.getcwd to retrieve our local path!
print("my_path_is:", os.getcwd())

#Let's use it to tell python where our custom modules are
path = os.getcwd()
sys.path.insert(0, path )
# then let's import the custom file
import util

#Loading the dataset
df = pd.read_csv("/home/clemente/hub/Datasets/PA_Datasets/pirate_data.csv")

#let's explore the dataset a little
print(df.columns)
print("Dataframe shape:", df.shape)


#Then let's run the NaN_Counter fuction from our util file
util.NaN_counter(df)

#It works! But we cannot visualize the plot in the terminal!
print ("It works! But we cannot visualize the plot in the terminal!")
