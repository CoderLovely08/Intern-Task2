import pandas as pd
import numpy as np
import xlrd as xd

#reading the input excel file
data=pd.read_excel('input_1.xlsx')

#getting the size of sheet rows and columns
rows=int(data.shape[0])
cols=int(data.shape[1])

#to append values for each candidate
name=[]
username=[]
ch_tag=[]   
test_name=[]
answered=[]
correct=[]
score=[]
skipped=[]
time_taken=[]
wrong=[]

for i in range(rows):
    ct=1
    tt=1
    fct=1
    while ct<=5:		
        if data.loc[i,f'Concept Test {ct} - score']!='-':
            name.append(data.loc[i,'Name'])
            username.append(data.loc[i,'id'])
            ch_tag.append(data.loc[i,'Chapter Tag'])
            test_name.append(f'Concept Test {ct}')
            answered.append(data.loc[i,f'Concept Test {ct} - answered'])
            correct.append(data.loc[i,f'Concept Test {ct}- correct'])
            score.append(data.loc[i,f'Concept Test {ct} - score'])
            skipped.append(data.loc[i,f'Concept Test {ct}- skipped'])
            time_taken.append(data.loc[i,f'Concept Test {ct} - time-taken (seconds)'])
            wrong.append(data.loc[i,f'Concept Test {ct}- wrong'])
        ct+=1
    while fct<=2:
        if data.loc[i,f'Full Chapter Test {fct} - score']!='-':
            name.append(data.loc[i,'Name'])
            username.append(data.loc[i,'id'])
            ch_tag.append(data.loc[i,'Chapter Tag'])
            test_name.append(f'Full Chapter Test {fct}')
            answered.append(data.loc[i,f'Full Chapter Test {fct} - answered'])
            correct.append(data.loc[i,f'Full Chapter Test {fct}- correct'])
            score.append(data.loc[i,f'Full Chapter Test {fct} - score'])
            skipped.append(data.loc[i,f'Full Chapter Test {fct}- skipped'])
            time_taken.append(data.loc[i,f'Full Chapter Test {fct} - time-taken (seconds)'])
            wrong.append(data.loc[i,f'Full Chapter Test {fct}- wrong'])
        fct+=1