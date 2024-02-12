'''
Functions for Using Databases with SeaTable DB

More info: 
- https://seatable.io/es/
- https://seatable.github.io/seatable-scripts/python/

TASK:
    - Use dataclass

WARNINGS:
    - ...
'''

__update__ = '2024.02.12'
__author__ = 'PABLO GONZALEZ PILA <pablopila.spain@gmail.com>'


''' SYSTEM LIBRARIES '''
from seatable_api import Base, context
import pandas as pd
from dataclasses import dataclass
import asyncio

''' CUSTOM LIBRARIES '''
from pydeveloptools.func_system import GET_FIRM, DATE_GET_TODAY, INTERNET_CONNECTION_CHECK


''' MAIN
------------------------------------------ '''

class SEATABLE_DB():
    def __init__(self, token: str) -> None:
        server_url = context.server_url or 'https://cloud.seatable.io'
        api_token = context.api_token or token
        self.base = Base(api_token, server_url)
        self.base.auth()
    
    def SQL_DF(self, SQL_STR: str) -> pd.DataFrame:
        '''
        return a pandas DataFrame of a SQL string
        '''
        SQL = self.base.query(SQL_STR)
        df = pd.DataFrame(SQL)
        return df
    
    def SQL_UPDATE(self, TABLE: str, DATA: dict, WHERE: list) -> None:
        '''
        VALUES (dict) = {"Field1": Value1, "Field2 ...} \n
        WHERE (list) = List of <class '.sql_filter'> objects \n
        Info: SeaTable only allows the use of update_row in conjunction with its internal _id \n
        Attention: If filters are not specified correctly you can change the data for multiple records
        '''
        TBL_INFO = self.TABLE_INFO(TABLE)
        ## WHERE
        WHERE_LST = []
        for filter in WHERE:
            if filter.value != None:
                #
                tbl_typ = TBL_INFO[filter.field]['type']
                type_datas = {'text':str, 'long-text':str, 'date':str, 'checkbox':bool, 'number':float, 'auto-number':str}
                # 
                typ = type_datas.get(tbl_typ, int)
                if typ == str:
                    where_str = str(filter.field) + filter.operator + chr(39) + str(filter.value) + chr(39)
                elif typ == int or typ == float: 
                    where_str = str(filter.field) + filter.operator + str(filter.value)
                elif typ == bool: 
                    if filter.value == True: 
                        where_str = str(filter.field) + filter.operator + "TRUE"
                    else: 
                        where_str = str(filter.field) + filter.operator + "FALSE"
                WHERE_LST.append(where_str)
        WHERE_STR = " AND ".join(WHERE_LST)
        ## _ID
        sql = self.base.query("SELECT _id FROM {} WHERE {};".format(TABLE, WHERE_STR))
        IDs = []
        for row in sql:
            id = row.get("_id")
            if id != None: IDs.append(id)
        ## UPDATE
        DATA_LST = []
        for id in IDs:
            id_dic = {"row_id": id, "row": DATA}
            id_dic['row']['FIRM'] = GET_FIRM()
            DATA_LST.append(id_dic)
        self.base.batch_update_rows(TABLE, rows_data=DATA_LST)

    def TABLE_INFO(self, TABLE: str) -> dict:
        '''
        Get a dictionary with all info about table columns
        dict = {field: 'type', 'editable', 'description'}
        '''
        SQL = self.base.list_columns(TABLE)
        fields = dict()
        for row in SQL:
            field = row['name']
            fields[field] = {}
            fields[field]['type'] = row['type']
            fields[field]['editable'] = row['editable']
            fields[field]['description'] = row['description']
        return fields

    def TABLE_HEADERS(self, TABLE: str) -> list:
        '''
        Get a list with all fields
        '''
        SQL = self.base.list_columns(TABLE)
        headers = list()
        for row in SQL:
            field = row['name']
            headers.append(field)
        return headers

class LICENSE():
    def __init__(self, APPLICATION, LOGIN) -> None:
        self.APPLICATION = APPLICATION
        self.LOGIN = LOGIN
        # 
        self.license_opens = 0
        self.license_date = DATE_GET_TODAY()
        self.license_connection = INTERNET_CONNECTION_CHECK()
        # 
        if self.license_connection == True:
            DB_NET = SEATABLE_DB()
            df = DB_NET.SQL_DF("SELECT * FROM LICENSES WHERE USER='{}' AND APPLICATION='{}'".format(self.LOGIN, self.APPLICATION))
            if len(df) == 1:
                self.license_opens = df.loc[0]['OPENS']
                self.license_date = df.loc[0]['DATE_LIMIT']

''' TEST
------------------------------------------ '''

