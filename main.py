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

#to iterate over each candidate data
for i in range(rows):
    ct=1
    tt=1
    fct=1
    
    #to iterate over each concept test of each data and append the corresponding info
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
    
    #to iterate over each full chapter test data of each candidate
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
        
        #to iterate over each topic test data of each candidate
        while tt<=2:
            if data.loc[i,f'Topic Test {tt} - score']!='-':
                name.append(data.loc[i,'Name'])
                username.append(data.loc[i,'id'])
                ch_tag.append(data.loc[i,'Chapter Tag'])
                test_name.append(f'Topic Test {tt}')
                answered.append(data.loc[i,f'Topic Test {tt} - answered'])
                correct.append(data.loc[i,f'Topic Test {tt}- correct'])
                score.append(data.loc[i,f'Topic Test {tt} - score'])
                skipped.append(data.loc[i,f'Topic Test {tt}- skipped'])
                time_taken.append(data.loc[i,f'Topic Test {tt} - time-taken (seconds)'])
                wrong.append(data.loc[i,f'Topic Test {tt}- wrong'])
            tt+=1

#empty dictionary for create dataframe at later stage
df={}
df['Name']=name
df['Username']=username
df['Chapter Tag']=ch_tag
df['Test_Name']=test_name
df['answered']=answered
df['correct']=correct
df['score']=score
df['skipped']=skipped
df['time-taken (seconds)']=time_taken
df['wrong']=wrong

#creates a data frame out of the given dictionary
newdf=pd.DataFrame(df)

#to create an excel file out of the data frame
newdf.to_excel('Output_1.xlsx')



##notes 
#the program is capable of handling edge cases like if a student dosen't appear for a particular test
#in order to use the program the the input format is given along with the main.py file
#just change the name of the file in 6th line of program and change the name output file name for the same at line no. 92
