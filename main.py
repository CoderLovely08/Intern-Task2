import pandas as pd
import numpy as np
import xlrd as xd

data=pd.read_excel('input_1.xlsx')
rows=int(data.shape[0])
cols=data.shape[1]