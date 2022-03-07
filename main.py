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

