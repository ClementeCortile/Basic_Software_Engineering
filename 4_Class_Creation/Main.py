
import sys
import os
path = os.getcwd()
sys.path.insert(0, path+'Software_Engineering_Basic/4_Create_and_import_a_class' )

from geom import Circle

#Testing the class below!! Very Bad Practice! This should be done in the main file!

print ("Running Main")

#To create a class object assign it to a variable! Do not forget its arguments!!! (name and radius in this case)
A = Circle("Cool_Circle", 3)
B = Circle("Big Circle", 100)
#If you run the object you'll see its memory location
A
B
#Object name.attribute will print that specific object attribute (works both for class attributes and method attributes)
A.name
A.pi
A.rad

B.name
B.pi
B.rad

#Let's use the object methods that we defined! (of course on the objects themselves)
A.Circumference()
A.Area()

B.Circumference()
B.Area()

#Classes are extremely useful to quickly apply functions to similar data structures!

print ("Ending main")
