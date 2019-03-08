print("Running python script")

import sys
import numpy as np
import pandas as pd
import time

import sys
import os

import util
from geom import Circle


radA = sys.argv[1]
radB = sys.argv[2]
path = sys.argv[3]

print("About to pass the parameters")
time.sleep(5)
print("param passed:", radA)
print("param passed:", radB)
print("param passed:", path)

time.sleep(5)
print("Loading the dataset from the parameter path and running them now!")
#Loading the dataset
df = pd.read_csv(path)
print(df.columns)
time.sleep(5)
print("Dataframe shape:", df.shape)


#Then let's run the NaN_Counter fuction from our util file
util.NaN_counter(df)

#It works! But we cannot visualize the plot in the terminal!
print ("It works! But we cannot visualize the plot in the terminal!")

time.sleep(3)

print("Ok! Time to import the class!")

print ("Running Main")
time.sleep(2)
#To create a class object assign it to a variable! Do not forget its arguments!!! (name and radius in this case)
A = Circle("Cool_Circle", 3)
B = Circle("Big Circle", 100)
#If you run the object you'll see its memory location
A
B
print("Objects Created...")
time.sleep(2)
#Object name.attribute will print that specific object attribute (works both for class attributes and method attributes)
#Let's use the object methods that we defined! (of course on the objects themselves)
print("This is the Circumference of circle A:", A.Circumference())
print("This is the Area of circle A:", A.Area())

print("This is the Circumference of circle B:", B.Circumference())
print("This is the Area of circle B:", B.Area())

#Let's use the object methods that we defined! (of course on the objects themselves)
A.Circumference()
A.Area()

B.Circumference()
B.Area()

#Classes are extremely useful to quickly apply functions to similar data structures!

print ("Ending main")
