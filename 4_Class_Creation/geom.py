#Training code for creating a Class!


#Let's create a Circle Class Object!!!

class Circle (object):

        #Class Object Attributes
        #Class Attributes - instanciated for all class objects
        pi = 3.14

        #Class instantiation method
        #Instance Attributes - different for each object
        def __init__(self, name: str, rad: int): # Creates a circle object when called (also specifing the tyoe)
            self.name = name
            self.rad = rad
        #Remember the "self" specification when creating variables inside a class instantiation
        #ALSO: mimic the assignment self.name_of_the_variable = variable

        #Class Methods
        def Circumference (self):
            """
            Computes the Circumference of a circle object
            and returns it
            """
            return 2*(self.pi)*(self.rad)
            #use the "self" assignment in the Class Methods as well!!!
            # you can omit the "self" with CLASS Attributes (which scope spans the whole class) but it's better to specify it!
            # but DO NOT OMIT the "self" when calling Instance Attributes (ex: pi VS rad)

        def Area (self):
            """
            Computes the Area of a circle object
            and returns it
            """
            return (self.pi)*((self.rad)**2)


#Testing the class below!! Very Bad Practice! This should be done in the main file!
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
