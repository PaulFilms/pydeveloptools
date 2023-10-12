'''
Functions for using databases in SQL language, dataframes with pandas, and some converters

ATTENTION:
    - SQL_INSERT is not available because the string needs to be adapted to the DB format (ACCESS, SQLITE, ...)
'''
__update__ = '2023.10.12'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import os
from datetime import datetime
from enum import Enum
from dataclasses import dataclass
import pandas as pd
# import numpy as np
from numpy import nan

''' CUSTOM MAIN LIBRARIES '''


''' SQL
------------------------------------------ '''

class OPERATORS(Enum):
    EQUAL = "="
    LESS = "<"
    LESS_EQUAL = "<="
    GREATER = ">"
    GREATER_EQUAL = ">="
    LIKE = "LIKE"
    IS_NULL = "IS NULL"

@dataclass
class FILTER:
    '''
    `VARIABLES`
    - field (str)
    - value (bool, str, int, float)
    - field_type (type): bool, str, int, float
    - operator (str): "=", "<", "<=", ">", ">=", "LIKE"

    `FUNCTIONS`
    - get_str: Get WHERE SQL string from selected FILTERS
    '''
    field: str
    value: str | float | int | bool
    field_type: type = str
    operator: OPERATORS = OPERATORS.EQUAL

    @classmethod
    def get_str(cls, FILTERS: str | list, WHERE_STR: bool = False) -> str:
        # STR
        if type(FILTER) == str:
            filter_str = FILTERS
            if WHERE_STR: filter_str = f"WHERE {filter_str}"
            return filter_str
        # LIST
        filter_str = []
        for filter in FILTERS:
            filter: cls
            FIELD = filter.field
            VALUE = filter.value
            TYPE = filter.field_type
            OPERATOR = filter.operator

            # BOOL
            if TYPE == bool: 
                if VALUE == True or VALUE == "TRUE" or VALUE == 1:
                    VALUE = "TRUE"
                else:
                    VALUE = "FALSE"
            
            # OPERATOR
            if OPERATOR == OPERATORS.IS_NULL:
                fieldFilter = f"{FIELD} {OPERATORS.IS_NULL.value}"
                filter_str.append(fieldFilter)
            elif OPERATOR == OPERATORS.LIKE:
                fieldFilter = f"{FIELD} {chr(39)}%{VALUE}%{chr(39)}"
                filter_str.append(fieldFilter)
            else:
                if TYPE == str:
                    VALUE = f"{chr(39)}{VALUE}{chr(39)}"
                fieldFilter = f"{FIELD} = {VALUE}"
                filter_str.append(fieldFilter)
            # 

        if len(filter_str) > 0:
            filter_str = " AND ".join(filter_str)
            if WHERE_STR: filter_str = f"WHERE {filter_str}"
        else:
            filter_str = ""
        return filter_str

def SQL_SELECT(SELECT: list, FROM: str, WHERE: list = [], ORDER: str = []) -> str:
    '''
    Return simple SELECT SQL String
    - SELECT (str, list)
    - FROM (str) **INCOMPLETE
    - WHERE (str, list): list (sql_filter(s) list) 
    - ORDER (str, list) **INCOMPLETE
    
    INCOMPLETE / DEBUG:
    - Con FROM hay que añadir la posiblidad de hacer JOIN
    '''

    ''' SELECT '''
    if type(SELECT) == str:
        if SELECT == "":
            print("SQL SELECT ERROR / SELECT STRING EMPTY")
            return None
        else:
            SELECT_STR = SELECT
    elif type(SELECT) == list:
        if len(SELECT) == 0:
            print("SQL SELECT ERROR / SELECT LIST EMPTY")
            return None
        else:
            SELECT_STR = []
            for field in SELECT: SELECT_STR.append(str(field))
            SELECT_STR = ", ".join(SELECT_STR)
    else: 
        print("SQL SELECT ERROR / SELECT TYPE DATA WRONG")
        return None
    
    ''' FROM '''
    FROM_STR = ""
    if type(FROM) == str:
        if SELECT == "":
            print("SQL SELECT ERROR / FROM STRING EMPTY")
            return "ERROR"
        else: FROM_STR = FROM
    else: 
        print("SQL SELECT ERROR / FROM TYPE DATA WRONG")
        return None
        
    ''' WHERE '''
    if type(WHERE) == str or type(WHERE) == list:
        WHERE_STR = FILTER.get_str(WHERE, WHERE_STR=True)
    else:
        print("SQL SELECT ERROR / WHERE TYPE DATA WRONG")
        return None

    ''' ORDER '''
    ORDER_STR = ""
    TYPE = type(ORDER)
    if TYPE == str:
        if ORDER == "": ORDER_STR = ""
        else: ORDER_STR = ORDER
    elif TYPE == list:
        if len(ORDER) == 0: ORDER_STR = ""
        else:
            ORDER_STR = []
            for field in ORDER: ORDER_STR.append(str(field))
            ORDER_STR = ", ".join(ORDER_STR)
    else: 
        print("SQL SELECT ERROR / ORDER TYPE DATA WRONG")
        return None
    if ORDER_STR != "": ORDER_STR = " ORDER BY " + ORDER_STR

    ''' SQL STRING '''
    SQL = f"SELECT {SELECT_STR} FROM {FROM_STR} {WHERE_STR} {ORDER_STR};"
    return SQL

def SQL_DELETE(TABLE: str, WHERE: list = []) -> str:
    '''
    Return simple DELETE SQL String
    - TABLE (str)
    - WHERE (str, list): list (sql_filter(s) list) 
    '''
    if type(WHERE) == str or type(WHERE) == list:
        WHERE_STR = FILTER.get_str(WHERE, WHERE_STR=True)
    else:
        print("SQL DELETE ERROR / WHERE TYPE DATA WRONG")
        return None
    # 
    SQL = f"DELETE FROM {TABLE} {WHERE_STR};"
    return SQL

def SQL_UPDATE(TABLE: str, SET: dict, WHERE: list = []) -> str:
    '''
    Return simple UPDATE SQL String
    - TABLE (str)
    - WHERE (str, list): list (sql_filter(s) list)

    INCOMPETE
    '''
    SET_STR = ""
    WHERE_STR = ""
    FIRM = f"{os.getlogin()} [{datetime.now().strftime('%Y-%m-%d / %H:%M')}]"
    SQL = f"UPDATE {TABLE} SET {SET_STR}, FIRM='{FIRM}' WHERE {WHERE_STR};"
    return SQL



''' PANDAS
------------------------------------------ '''

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



''' CONVERTERS
------------------------------------------ '''

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
