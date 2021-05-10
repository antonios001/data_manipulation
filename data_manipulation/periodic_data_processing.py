# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:20:07 2021

@author: dynamit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# This scheduler can be found at https://schedule.readthedocs.io/en/stable/index.html.
# Unfortunately, I have not had the time to test it so if it fails to run, manually run the data_processing.py instead
import schedule
import time

path1='d1.csv'
path2='d2.csv'

def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

def filter_data(data, noname=0, noprice=0, overprice=0):
    if noname == 1:
        data = data.astype({'name':str})
        data = data[data['name']!='nan']
    if noprice == 1:
        data = data[data['price'].apply(lambda x: is_float(x))]
    if overprice == 1:
        data = data.astype({'price':float})
        data['over100'] = np.where(data['price']>100.0, True, False)
    return data

def save_data_file_with_headers(path1,path2):
    
    d1 = pd.read_csv(path1)
    d2 = pd.read_csv(path2)
    dc = pd.concat([d1,d2],axis=0)
    nonamed=1
    nopriced=1
    overpriced=1
    df = filter_data(dc, noname=nonamed, noprice=nopriced, overprice=overpriced)
    dfsplit = df.astype({'name':str})
    firstname = dfsplit['name'].str.split(" ",expand = True)[0].astype(str)
    lastname = dfsplit['name'].str.split(" ",expand = True)[1].astype(str)
    dfsplit.insert(loc=0, column='last', value=lastname)
    dfsplit.insert(loc=0, column='first', value=firstname)
    dfinal = dfsplit.drop(['name'], axis = 1)
    dfinal.to_csv('data_final.csv',index=False)

   
schedule.every().day.at("08:30").do(save_data_file_with_headers,path1=path1,path2=path2)    
while True:
    schedule.run_pending()
    time.sleep(1)