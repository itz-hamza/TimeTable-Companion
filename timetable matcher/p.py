import pandas as pd
import numpy as np

#the excel file has seperate sheets for each day, so extracting sheets of different days in to seperate csv files using this code
#excelList = pd.ExcelFile('FAST School of Computing - Spring  2024 TimeTable  V1.2.xlsx')
#for sheets in excelList.sheet_names:
 #   df = excelList.parse(sheets)
  #  df.to_csv(f'{sheets}.csv',index=False)



# reading all csv files into a list of dataframes
ListOfDF = []
ListOfDF.append( pd.read_csv(r'timetable matcher\MONDAY.csv'))
ListOfDF.append( pd.read_csv(r'timetable matcher/TUESDAY.csv'))
ListOfDF.append( pd.read_csv(r'timetable matcher\WEDNESDAY.csv'))
ListOfDF.append( pd.read_csv(r'timetable matcher\THURSDAY.csv'))
#ListOfDF.append(  pd.read_csv('FRIDAY .csv')) #friday is an exception, so will figure it out later

#fridayDF = pd.read_csv('Friday .csv')

keys = [] # to store time periods of a day
for j in range (1,9):
    keys.append(ListOfDF[0].iloc[1,j]) # making a list which has all the times, like 8-9, 9-10
valuesInitial = [None,None,None,None,None]  #5 values, each for a day in the week. So a key will be time of the day, and it will have 5 values. At 0 index it would tell about monday, at 1st index it would tell about tuesday

#timeTable6F = dict.fromkeys(keys,valuesInitial) #making an empty dictionary with keys only. each key represent a time of the day, like 8-9

#timeTable6A = dict.fromkeys(keys,valuesInitial)

#making a 2d array for timetable of each section. IF there is a class then the value will be one, else it will be zero

TimeTable6F = np.zeros((len(ListOfDF),len(ListOfDF[0].columns)))
#FridayTimeTable6F = np.zeros((len(ListOfDF),len(ListOfDF[4].columns)))
#print(FridayTimeTable6F)
TimeTable6A =  np.zeros((len(ListOfDF),len(ListOfDF[0].columns)))

x = 0

for k in range(len(ListOfDF)):
    for i in range(len(ListOfDF[k])):
        for j in range(len(ListOfDF[k].columns)):
            word = ListOfDF[k].iloc[i,j]
            if 'BCS-6F' in str(word):
            #print(word + str(df.iloc[1,j]))
                TimeTable6F[k,j] = 1
                if 'Lab' in word:
                    TimeTable6F[k+1,j+1]=1
                    TimeTable6F[k+2,j+2]=1
            if 'BCS-6A' in str(word):
                TimeTable6A[k,j] = 1
                if 'Lab' in word:
                    TimeTable6A[k+1,j+1]=1
                    TimeTable6A[k+2,j+2]=1

#FreeTime = []

#for times in timeTable6A.keys():
   # if timeTable6A[times] == None:
  #      if timeTable6F[times] == None:
 #           FreeTime.append(times)

for i in range(len(ListOfDF)):
    for j in range(len(ListOfDF[i].columns)):
        if(TimeTable6A[i][j] == 0 and TimeTable6F[i][j]==0):
            print(f"You both have free time during {ListOfDF[i].iloc[1,j]}")
            

 

 # data is correctly being read. I have two exceptional cases. Labs and electives. I will need to read the data in a notebook and then analyze it to get some insights as to how to make it more efficient to program till then its fine i guess



# have to make a mapping of days and time on a matrix and try to retrieve day and time from that after getting a solution matrix. I need to make a good solution martrix, preferably a map which has mappings on times of the days. All 8 none except fridays which will have 9. maybe friday will have a different map
            
            