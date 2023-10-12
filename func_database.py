''' 
NOTES:
TASK:
WARNINGS:
'''
__update__ = '2023.10.12'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import os, json
from datetime import datetime
from dataclasses import dataclass
import pandas as pd
# import numpy as np
from numpy import nan

''' CUSTOM MAIN LIBRARIES '''


'''
PANDAS
------
'''

def pandas_df_save(dataFrame: pd.core.frame.DataFrame, file_name: str):
    '''
    Save Pandas DataFrame to .pkl file
    '''
    file_str = file_name + ".pkl"
    dataFrame.to_pickle(file_str)

def pandas_df_load(file_name=str):
    '''
    Load Pandas DataFrame from .pkl file
    '''
    file_str = file_name+".pkl"
    dataFrame = pd.read_pickle(file_str)
    return dataFrame

def pandas_reindex(dataFrame=pd.core.frame.DataFrame, row_index=int, order="up" or "down"):
    lst = []
    for row in range(len(dataFrame)):
        if order == "up":
            if row == row_index-1: lst.append(row_index)
            if row != row_index or row == 0: lst.append(row)
        if order == "down":
            if row == row_index and row != len(dataFrame)-1: lst.append(row_index+1)
            elif row == row_index+1: lst.append(row_index)
            else: lst.append(row)

    DATAFRAME = dataFrame.reindex(lst)
    return DATAFRAME


'''
CONVERTERS
----------
'''

def sql_to_dataframe(headers: list, sql_list):
    dictionary = {}
    for field in headers:
        dictionary[field] = []
    if sql_list != None:
        for row in sql_list:
            for field in headers:
                indx = headers.index(field)
                value = row[indx]
                dictionary[field].append(value)
    dataframe = pd.DataFrame(dictionary)
    return dataframe

def dataframe_to_dict(dataframe=pd.core.frame.DataFrame):
    dictionary = dataframe.to_dict()
    return dictionary

def dataframe_to_txt(DATAFRAME=pd.DataFrame) -> str:
    '''
    '''
    columns = {}
    for col in DATAFRAME.columns:
        columns[col] = 0
        for row in DATAFRAME.index:
            value = len(str(DATAFRAME.loc[row][col]))
            if columns[col] < value: columns[col] = value
    ## Texto
    tx = ""
    for row in DATAFRAME.index:
        lst = []
        for col in DATAFRAME.columns:
            value = DATAFRAME.loc[row][col]
            largo = columns[col]+1
            texto = f'{value: <{largo}}'
            texto = str(value)
            lst.append(texto)
        tx += ", ".join(lst) # chr(9) + "| "
        tx += chr(10) # "\n"
    return tx



def dataframe_getcell(dataframe=pd.core.frame.DataFrame, FIELD=str, ROW=int, type=float):
    '''
    Get cell from data_frame
    '''
    value = dataframe[FIELD].iloc[ROW]
    if type == float:
        if value == "" or value == nan:
            value = 0
        value = float(value)
    return value

