days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
valuesInitial = [None, None, None, None, None, None, None, None]

# Create a dictionary where each day has a separate list
tt = {day: valuesInitial[:] for day in days}

tt['friday'].append(None)

mapDayToIndex = {0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday'}
#print(mapDayToIndex)

#tt[mapDayToIndex[0],1]
#print(tt[mapDayToIndex[0],1])

#print(tt['monday'])
# generated a code which can work as a nice data structure for holding the timetable values

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

print(type(ListOfDF[0].columns[0])) #day

print(ListOfDF[0].iloc[5,1]) #time

for i in range(1,len(ListOfDF[0].columns)):
    print(ListOfDF[0].iloc[1,i])