import pandas as pd
df = pd.read_excel('FAST School of Computing - Spring  2024 TimeTable  V1.2.xlsx')
keys = []
for j in range (1,9):
    keys.append(df.iloc[1,j]) # making a list which has all the times, like 8-9, 9-10

timeTable6F = dict.fromkeys(keys,None) #making an empty dictionary with keys only. each key represent a time of the day, like 8-9

timeTable6A = dict.fromkeys(keys,None)

for i in range(len(df)):
    for j in range(len(df.columns)):
        word = df.iloc[i,j]
        if 'BCS-6F' in str(word):
            #print(word + str(df.iloc[1,j]))
            timeTable6F[str(df.iloc[1,j])] = word
        if 'BCS-6A' in str(word):
            timeTable6A[str(df.iloc[1,j])] = word

FreeTime = []

for times in timeTable6A.keys():
    if timeTable6A[times] == None:
        if timeTable6F[times] == None:
            FreeTime.append(times)


print(FreeTime)
