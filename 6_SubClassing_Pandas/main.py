import pandas as pd
import mypanda as mypd


df1 = pd.read_csv("/home/clemente/hub/Datasets/Datasets/crypto-markets.csv")
df2 = pd.read_csv("/home/clemente/hub/Datasets/PA_Datasets/pirate_data.csv")

#Create my subclassed pandas dataframe
New_df = mypd.Cleaner(df1)

#All of the usual pandas methods do work on it
New_df.describe()

#Plus you can add your own custom methods using the pandas functionality
New_df.TestF()

#You can create a NaN counter
New_df.NaN_counter()

New_df2 = mypd.Cleaner(df2)

New_df2.NaN_counter()
