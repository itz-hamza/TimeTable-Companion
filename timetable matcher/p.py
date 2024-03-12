import pandas as pd
import numpy as np


# FirstSection = input("Enter first section: ")
# SecondSection = input("Enter second section")
FirstSection = "BCS-6F"
SecondSection = "BCS-6A"
# the excel file has seperate sheets for each day, so extracting sheets of different days in to seperate csv files using this code

# reading all csv files into a list of dataframes
ListOfDF = []
ListOfDF.append( pd.read_csv(r'timeTableCsv 0'))
ListOfDF.append( pd.read_csv(r'timeTableCsv 1'))
ListOfDF.append( pd.read_csv(r'timeTableCsv 2'))
ListOfDF.append( pd.read_csv(r'timeTableCsv 3'))
ListOfDF.append( pd.read_csv(r'timeTableCsv 4'))

# removing extra columns from fridays csv 
#ListOfDF[4].drop(ListOfDF[4].columns[[7,11,12,13,14,15]], axis=1, inplace=True) code that shall run only once
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
valuesInitial = [None, None, None, None, None, None, None, None]

# Create a dictionary where each day has a separate list
tt = {day: valuesInitial[:] for day in days}
tt6A = {day: valuesInitial[:] for day in days}
tt['friday'].append(None)
tt6A['friday'].append(None) #friday has 9 blocks

mapDayToIndex = {0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday'}
print(len(ListOfDF[0].columns))
for k in range(len(ListOfDF)):
    for i in range(len(ListOfDF[k])): # all the rows
        for j in range(len(ListOfDF[k].columns)):
            word = ListOfDF[k].iloc[i,j]
            if FirstSection in str(word):
                tt[mapDayToIndex[k]][j-1] = 1
                #print(f"{(ListOfDF[k].columns[0])} at {(ListOfDF[k].iloc[1,j])} {word}")
                if 'Lab' in word:
                    tt[mapDayToIndex[k]][j]=1
                    tt[mapDayToIndex[k]][j+1]=1
            if SecondSection in str(word):
                tt6A[mapDayToIndex[k]][j-1] = 1
                if 'Lab' in word:
                    tt6A[mapDayToIndex[k]][j]=1
                    tt6A[mapDayToIndex[k]][j+1]=1



for i in range(len(ListOfDF)):
    for j in range(len(tt[mapDayToIndex[i]])): 
       if(tt[mapDayToIndex[i]][j] == None and tt6A[mapDayToIndex[i]][j]==None):
           print(f"You both have free time during {j+1} block on {mapDayToIndex[i]} ")
# print(tt6A)
# need to make another tt for another section
 # data is correctly being read. I have two exceptional cases. Labs and electives. I will need to read the data in a notebook and then analyze it to get some insights as to how to make it more efficient to program till then its fine i guess



# have to make a mapping of days and time on a matrix and try to retrieve day and time from that after getting a solution matrix. I need to make a good solution martrix, preferably a map which has mappings on times of the days. All 8 none except fridays which will have 9. maybe friday will have a different map

#bas ab file sahi karni hai friday ki aur labs ko dekhna hai
            