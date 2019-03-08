#Utilities.py
#This file contains a custom function that will be imported in the main file


def NaN_counter (df):
    """
    DataFrame parser for NaN:
    input: df = dataframe
    prints the number of NaN by columns
    output: returns the same df with the number of NaNs per column
    """
    print ("Running NaN Counter from the util.py module!!!!")
    import pandas as pd

    col = df.columns
    cont = []
    print("NaN Counter by columns")
    for i in col:
        n = len(df[(df[i].isnull() == True)])
        cont.append(n)
        if ( n != 0):
            print(i,":",len(df[(df[i].isnull() == True)]))
    df_r = pd.DataFrame([cont], columns=col)

    #try:
    #    col_d = df_r.columns
    #    sns.barplot(data=df_r)
    #    plt.xticks(rotation=90)
    #except:
    #    pass
    return df_r


#if __name__ == '__main__':
#    NaN_counter(df)
