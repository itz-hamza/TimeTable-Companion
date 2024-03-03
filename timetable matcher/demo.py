import pandas as pd
import numpy as np

excelList = pd.ExcelFile('FAST School of Computing - Spring  2024 TimeTable  V1.2.xlsx')

for sheets in excelList.sheet_names:
    df = excelList.parse(sheets)
    df.to_csv(f'{sheets}.csv',index=False)