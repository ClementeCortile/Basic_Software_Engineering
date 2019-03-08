
#Example of pandas subclassing
import pandas as pd

class Cleaner(pd.DataFrame):

        #Class Object Attributes
        #Class Attributes - instanciated for all class objects
        #WARNING NONE

        #Class instantiation method
        #Instance Attributes - different for each object
        #WARNING Class instanciated via self constructor
        @property
        def _constructor(self):
            #Must be initialized as a constructor, all methods are automatically created
            #if __init__ is used the object will exceed the maximum recursion depth
            #self.df = df -> self == df
            return Cleaner

        #Class Methods
        def NaN_counter (self):
            """
            DataFrame parser for NaN:
            input: df = dataframe
            prints the number of NaN by columns
            output: returns the same df with the number of NaNs per column
            """
            print ("Running NaN Counter from the util.py module!!!!")

            col = self.columns
            cont = []
            print("NaN Counter by columns")
            for i in col:
                n = len(self[(self[i].isnull() == True)])
                cont.append(n)
                if ( n != 0):
                    print(i,":",len(self[(self[i].isnull() == True)]))
            df_r = pd.DataFrame([cont], columns=col)

            try:
                col_d = df_r.columns
                sns.barplot(data=df_r)
                plt.xticks(rotation=90)
            except:
                pass
            return df_r

        def TestF (self):
            col = self.columns
            print (col)
            return None
