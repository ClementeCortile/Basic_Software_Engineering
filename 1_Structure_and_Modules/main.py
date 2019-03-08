
#The program will run from this main file ( C style!)
#Read every comment from top to bottom
#Try running the file from the terminal with | python3 main.py | command

#Python modules are imported from
import sys
#print(sys.path)

#Importing modules
import os
import numpy as np

os.getcwd()

#...but we can import our own custom modules that are stored in the same directory/folder
# The comment below is a copy of the code contained in test.py and test_2
# test.py has two functions:
####################################
"""
#test.py

def hello_world():
    print("Hello World")
    print("Module_Executed")

def hi_world():
    print("Hi World")
    print("Module_Executed")

##################################
"""
# test_2.py has just one function:
"""
#test_2
#Relative import

def hello_world_2():
    print("I am hello world 2!")
"""

import test
# is an absolute custom import

import test_2
#BEWARE: eager execution (i#is a relative import !!!!!!!!!
#in-line execution) will not work with relative imports

#Testing if the main is executing
print("executing main - all imports are correct")

test.hello_world() #absolute import's functions need to be called as methods on the name of the module

test.hi_world()

test_2.hello_world_2() #relative imports's functions can just be executed!
