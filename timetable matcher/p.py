import pandas as pd

# reading all csv files into a list of csv files
ListOfDF = []
ListOfDF.append( pd.read_excel('FAST School of Computing - Spring  2024 TimeTable  V1.2.xlsx'))
ListOfDF.append( pd.read_excel('Tuesday.xlsx'))
ListOfDF.append( pd.read_excel('Wednesday.xlsx'))
ListOfDF.append( pd.read_excel('Thursday.xlsx'))
ListOfDF.append(  pd.read_excel('Friday.xlsx'))


keys = []
for j in range (1,9):
    keys.append(ListOfDF[0].iloc[1,j]) # making a list which has all the times, like 8-9, 9-10

timeTable6F = dict.fromkeys(keys,None) #making an empty dictionary with keys only. each key represent a time of the day, like 8-9

timeTable6A = dict.fromkeys(keys,None)

for i in range(len(ListOfDF[0])):
    for j in range(len(ListOfDF[0].columns)):
        word = ListOfDF[0].iloc[i,j]
        if 'BCS-6F' in str(word):
            #print(word + str(df.iloc[1,j]))
            timeTable6F[str(ListOfDF[0].iloc[1,j])] = word
        if 'BCS-6A' in str(word):
            timeTable6A[str(ListOfDF[0].iloc[1,j])] = word

FreeTime = []

for times in timeTable6A.keys():
    if timeTable6A[times] == None:
        if timeTable6F[times] == None:
            FreeTime.append(times)


print(FreeTime)
