import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print("project is based on Shoe Sales")
print("------------------------------------")
df=pd.read_csv('Sales 2021-22.csv')
print("------------------------------------")
print("------------------------------------")
while(True):
    print(" Main Menu")
    print("1. Show all Records")
    print("2. information about the file")
    print("3.Attributes of Shoe Sales DataFrame")
    print("4. Search Records")
    print("5. Add Records")
    print("6.Delete  Records ")
    print("7.Graphical representation")
    print("8.Exit")
    #print("9.")
    x=int(input("Enter your Choice"))
    if x==1:
        print(df)
        break 
    if x==2:
        print("This is a Python program to see and maintain record of sales of shoes")
        break
    elif x==3:#working
        print("------------------------------------")
        #while(True):
    print("A. Display Rows of the Sales")
    print("B. Display columns of the Sales")
    print("C. Display Both Rows and Columns of the Sales")  
    print("D. Display the size of the Sales")
    print("E. Display the shape of the Sales")
    print("F. Display Axes of the Sales")
    print("G. Exit")
    ch=input("Enter Choice")
    if ch=='A':
        print(df.index)
        break
    elif ch=='B':
        print(df.columns)
        break
    elif ch=='F':
        print(df.axes)
        break
    elif ch=='D':
        print(df.size)
        break
    elif ch=='C':
        print("{COLUMNS}:",df.columns,"{AXES}:",df.axes)
        break
    elif ch=='E':
        print(df.shape)
        break
    elif ch=='G':
        print(df.empty)
        break
    if x==4:
        print("------------------------------------")
       # while(True):
    print("Display Records Menu")
    print("1. Top 5 Records")
    print("2. Bottom 5 Records")
    print("3. Specific number of records from the top")
    print("4. Specific number of records from the bottam")
    print("5. Exit")
    ch4=int(input("Enter choice"))
    if ch4==1:
        print(df.head())
        #break
    elif ch4==2:
        print(df.tail())
        #break
    elif ch4==3:
        n=int(input("Enter how many records you want to display from the top"))
        print(df.head(n))
        #break
    elif ch4==4:
        n=int(input("Enter how many records you want to display from the bottom"))
        print(df.tail(n))
        #break
    else:
        print("INVAILD INPUT")
    exit()
    #ch=5 
    if x==5:
        print("------------------------------------")
       # while(True):
        print("1. Add a row")
        print("2. Modify a row")
        print("3. Exit")
    ch5=int(input("Enter Choice"))
    if ch5==1:
        p=input("Input the number of row you wanna add")
        o=int(input("Input the values you wanna give to that row"))
        df.at[p,:]=o
        print(df)
        #break
    elif ch5==2:
        i=int(input("Input the number of a existing row which you wanna modify"))
        j=input("Input the values you wanna change")
    df.loc[i,:]=[j]
    print(df)
    #break
    ##  elif ch5==5:
                #    break
    if x==6:
        g=int(input("Enter the number of row you wanna delete"))
        print(df.drop(g))
        #break
    if x==7:
        print("--------------------------------------")
       # while(True):
        print("1. Line Chart")
        print("2. Bar graph")
        print("3. histogram")
        print("4. Exit")
    ch7=int(input("Enter Choice"))
    if ch7==1:
        df.plot(x ='Name of customers', y='Number of shoes sold')
        plt.show()
        #break
    elif ch7==2:
        df.plot(x ='Name of customers', y='Number of shoes sold',kind='bar')
        plt.show()
        #break
    elif ch7==3:
        df.hist(bins=20)
        plt.show()
        #break
              
    if x==8:
        print("Want to continue?")
        sys.exit()
        
        
        

                    
              
        
        
        
        
    
    
    
    