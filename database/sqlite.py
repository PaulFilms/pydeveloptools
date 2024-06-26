'''
Functions for Using Databases with SQLite Format

`TASK:`
    - Implementar fetchone() para las consultas de un solo dato

`WARNINGS:`
    - ...
________________________________________________________________________________________________ '''

__update__ = '2024.03.30'
__author__ = 'PABLO GONZALEZ PILA <pablopila.spain@gmail.com>'


''' SYSTEM LIBRARIES '''
import sqlite3
import json
from typing import List

''' CUSTOM LIBRARIES '''
from pydeveloptools.func_database import SQL_SELECT, FILTER, OPERATORS


''' MAIN
________________________________________________________________________________________________ '''

class SQLITE_DB():
    '''
    SQLite DB
    '''
    def __init__(self, dbPath: str) -> None:
        self.dbPath = dbPath
        self.library = sqlite3
    
    def SQL_EXEC(self, SQL_STR: str, commit: bool = False) -> tuple:
        '''
        Execute a SQL String
        - `SQL_STR:` (str)
        - `commit:` (bool)
        '''
        ## OPEN CONNECTION
        self.CNN = self.library.connect(self.dbPath)
        self.CURSOR = self.CNN.cursor()
        
        ## SQL STRING EXECUTE
        LIST = None
        try:
            # print(SQL_STR)
            self.CURSOR.execute(SQL_STR)
            if commit:
                self.CNN.commit()
            else:
                LIST = self.CURSOR.fetchall()
        except:
            print(SQL_STR)
            print("SQL_EXEC ERROR")
        
        ## CLOSE CONNECTION
        self.CURSOR.close()
        self.CNN.close()
        ##
        return LIST

    def SQL_TABLES(self) -> list:
        '''
        An list with all tables in the DB 
        '''
        DATA = self.SQL_EXEC("SELECT name FROM sqlite_master WHERE type='table';")
        LIST: list = []
        for row in DATA:
            LIST.append(row[0])
        LIST.remove('sqlite_sequence')
        return LIST

    def SQL_TABLE_INFO(self, TABLE: str) -> dict:
        '''
        List with info data about selected Table

        BUG:
            Hay que crear una lista con elementos de python:
            FIELD_ID, TYPE
        '''
        SQL = f"PRAGMA table_info({TABLE});"
        LIST = self.SQL_EXEC(SQL, commit=False)
        DICT: dict = {}
        for row in LIST:
            ORDER = row[0]
            DICT[row[1]] = {
                "ORDER": ORDER,
                }
        return LIST

    def SQL_TABLE_HEADERS(self, TABLE: str) -> List[str]:
        '''
        List of headers
        '''
        SQL = f"PRAGMA table_info({TABLE});"
        SQL_LIST = self.SQL_EXEC(SQL, commit=False)
        LIST: list = []
        for row in SQL_LIST:
            LIST.append(row[1])
        return LIST

    def SQL_SELECT_JSON(self, TABLE: str, FIELD: str, ID: str | int) -> dict:
        '''
        Get a Dictionary Type of an JSON BLOB Field
        '''
        VALUE: dict = None
        TYPE_ID = type(ID)

        ## CHECK TABLE
        SQL: str = f"SELECT COUNT (*) FROM sqlite_master WHERE type='table' AND name='{TABLE}';"
        CHECK: int = self.SQL_EXEC(SQL)[0][0]
        if CHECK != 1:
            return VALUE
        
        ## CHECK ID
        if TYPE_ID == str:
            SQL: str = f"SELECT COUNT (*) FROM {TABLE} WHERE Id='{ID}'"
        elif TYPE_ID == int or TYPE_ID == float:
            SQL: str = f"SELECT COUNT (*) FROM {TABLE} WHERE Id={ID}"
        CHECK: int = self.SQL_EXEC(SQL)[0][0]
        if CHECK != 1:
            return VALUE
        
        ## QUERY JSON
        if TYPE_ID == str:
            SQL = f"SELECT {TABLE}.{FIELD} FROM {TABLE} WHERE {TABLE}.Id={chr(39)}{ID}{chr(39)};"
        elif TYPE_ID == int or TYPE_ID == float:
            SQL = f"SELECT {TABLE}.{FIELD} FROM {TABLE} WHERE {TABLE}.Id={ID};"
        VALUE = self.SQL_EXEC(SQL)[0][0]
        
        if VALUE != None and VALUE != "":
            VALUE = json.loads(VALUE)
        
        ## RETURN
        return VALUE

    def SQL_FIELD_LIST(self, TABLE=str, FIELD=str, ORDER="ASC") -> list:
        '''
        Get a list of all data in a selected FIELD
        ORDER can use ASC / DESC
        '''
        SQL = SQL_SELECT(SELECT=FIELD, FROM=TABLE, ORDER=FIELD + " " + ORDER)
        SQL_LIST = self.SQL_EXEC(SQL)
        LIST: list = []
        if len(SQL_LIST) > 0:
            for row in SQL_LIST: LIST.append(row[0])
        return LIST

    def SQL_INSERT(self, TABLE=str, VALUES={}):
        '''
        - TABLE (str) ** Table Name
        - VALUES (dict) ** dict {"field1": value1, "field2 ...}

        ATTENTION:
        - The BLOB type Data, is reserved in this function for JSON data
        
        INCOMPLETE / DEBUG: 
        - Revisar el caso en el que no hay valores que añadir
        - Para los separadores de comas hay que utilizar join para reducir codigo
        '''
        COLUMNS_STR = ""
        VALUES_STR = ""
        ## TABLE INFO
        TABLE_INFO = self.SQL_TABLE_INFO(TABLE)
        TABLE_DICT = {}
        for row in TABLE_INFO: TABLE_DICT[row[1]] = row[2]
        ## VALUES
        COLUMNS_LST = []
        VALUES_LST = []
        if len(VALUES) > 0:
            for field in VALUES.keys():
                ## COLUMNS
                COLUMNS_LST.append(field)
                ## VALUES TYPE
                if type(VALUES[field]) == dict: TYPE = VALUES[field].get('TYPE')
                else:
                    TYPE = TABLE_DICT[field]
                    if TYPE == 'INTEGER' or TYPE == 'REAL' or TYPE == 'NUMERIC': TYPE = int
                    elif TYPE == 'TEXT': TYPE = str
                    elif TYPE == 'BLOB': TYPE = dict
                    elif TYPE == None: pass
                ## VALUES DATA
                if type(VALUES[field]) == dict: VALUE = VALUES[field].get('VALUE')
                else: VALUE = VALUES[field]
                ## 
                if VALUE == None:
                    # VALUES_STR += "NULL"
                    VALUE_STR = "NULL"
                elif TYPE == bool: 
                    if VALUE == True: 
                        # VALUES_STR += "TRUE"
                        VALUE_STR = "TRUE"
                    else: 
                        # VALUES_STR += "FALSE"
                        VALUE_STR = "FALSE"
                elif TYPE == int or TYPE == float:
                    # VALUES_STR += str(VALUE)
                    VALUE_STR = str(VALUE)
                elif TYPE == str: 
                    # VALUES_STR += chr(39) + str(VALUE) + chr(39)
                    VALUE_STR = chr(39) + str(VALUE) + chr(39)
                elif TYPE == dict:
                    # VALUE = dict_to_json(VALUE)
                    # VALUES_STR += chr(39) + VALUE + chr(39)
                    # VALUES_STR += f"'{VALUE}'" # '{DICT}'
                    VALUE_STR = chr(39) + str(VALUE) + chr(39) # '{DICT}'
                elif TYPE == None:
                    # VALUES_STR += "NULL"
                    VALUE_STR = "NULL"
                # 
                VALUES_LST.append(VALUE_STR)
                # 
        COLUMNS_STR = ", ".join(COLUMNS_LST)
        VALUES_STR = ", ".join(VALUES_LST)
        SQL = f"INSERT INTO {TABLE} ({COLUMNS_STR}) VALUES ({VALUES_STR});"
        try:
            self.SQL_EXEC(SQL, commit=True)
        except:
            print("SQL INSERT ERROR / SQL_INSERT")
            print(SQL)

    def SQL_UPDATE(self, TABLE: str, VALUES: dict, WHERE_STR: str):
        '''
        - TABLE (str) ** Table Name
        - VALUES (dict) ** dict {"field1": value1, "field2 ...}
        - WHERE_STR (str) ** str "Id=23 AND field1='value'"
        
        ATTENTION: 
        - The BLOB type Data, is reserved in this function for JSON data
        - When VALUES dict are empty the UPDATE write NULL value
        '''
        ## TABLE INFO
        TABLE_INFO = self.SQL_TABLE_INFO(TABLE)
        TABLE_DICT = {}
        for row in TABLE_INFO: 
            TABLE_DICT[row[1]] = row[2]
        ## SET VALUES
        SET_STR = ""
        SET_LST = []
        for field in VALUES.keys():
            value = VALUES[field]
            ## VALUE NULL
            if value == "" or value == None:
                set_str = "{}=NULL".format(field)
            ## VALUES STR
            else:
                ## VALUES TYPE
                TYPE = TABLE_DICT.get(field)
                if TYPE == 'INTEGER' and type(value) == bool: TYPE = bool
                elif TYPE == 'INTEGER' and type(value) == int: TYPE = int
                elif TYPE == 'REAL' or TYPE == 'NUMERIC': TYPE = int
                elif TYPE == 'TEXT': TYPE = str
                elif TYPE == 'BLOB': TYPE = dict
                else: TYPE = None
                # 
                if TYPE == bool: 
                    if value == True: set_str = "{}=TRUE".format(field)
                    else: set_str = "{}=FALSE".format(field)
                elif TYPE == int or TYPE == float:
                    set_str = "{}={}".format(field, value)
                elif TYPE == str: 
                    set_str = "{}='{}'".format(field, value)
                elif TYPE == dict:
                    # VALUE = dict_to_json(VALUE)
                    set_str = "{}='{}'".format(field, value) # '{DICT}'
                    ## TypeError: can only concatenate str (not "dict") to str
                elif TYPE == None:
                    set_str = "{}=NULL".format(field)
            SET_LST.append(set_str)
        ## COMAS
        SET_STR = ", ".join(SET_LST)
        ## SQL STRING
        SQL = "UPDATE {} SET {} WHERE {};".format(TABLE, SET_STR, WHERE_STR)
        # print(SQL)
        try:
            if len(VALUES) > 0: self.SQL_EXEC(SQL, commit=True)
            else: print("VALUES (dict) ERROR / SQL_UPDATE")
        except:
            print("SQL UPDATE ERROR / SQL_UPDATE")
            print(SQL)

    def BLOB(self, TABLE: str, Id: str):
        '''
        Get BLOB data
        BUG INCOMPLETE
        '''

''' JSON FUNCTIONS
________________________________________________________________________________________________ '''

def JSON_UPDATE(TABLE: str, DB_FIELD: str, JSON_FIELD: str, WHERE: list, VALUE) -> str:
    '''
    UPDATE THE VALUE OF SPECIFIC FIELD.
    **IF THE FIELD IS NULL, AN EMPTY JSON IS ADDED**
    
    - `TABLE:` (str) NAME OF TABLE
    - `DB_FIELD:` (str) NAME OF FIELD IN DB TABLE
    - `JSON_FIELD:` (str) NAME OF FIELD IN JSON
    - `WHERE:` (str | list) LIST OF FILTERS
    - `VALUE:` VALUE TO BE UPDATE
    
    `EXAMPLE:`
    ###### UPDATE <`TABLE`>
    ###### SET
    ###### <`DB_FIELD`> = JSON_SET(IIF(<`DB_FIELD`> IS NULL, '{}', <`DB_FIELD`>), '$.<`JSON_FIELD`>', <`VALUE`>)
    ###### WHERE <`WHERE`>;
    '''
    ## VARIANT
    VARIANT = "NULL"
    if type(VALUE) == None:
        VARIANT = "NULL"
    elif type(VALUE) == str:
        VARIANT = f"'{VALUE}'"
    elif type(VALUE) == bool:
        if VALUE == True or VALUE == "TRUE" or VALUE == "true" or VALUE == 1 or VALUE == "1":
            VARIANT = "TRUE"
        else:
            VARIANT = "FALSE"
    elif type(VALUE) == int or type(VALUE) == float:
        VARIANT = VALUE
    ## WHERE STR
    WHERE_STR = FILTER.get_str(WHERE)
    ## SQL STR
    sql = f"UPDATE {TABLE} SET {DB_FIELD} = JSON_SET(IIF({DB_FIELD} IS NULL, '{chr(123)}{chr(125)}', {DB_FIELD}), '$.{JSON_FIELD}', {VARIANT})"
    if len(WHERE_STR) > 0:
        sql += f" WHERE {WHERE_STR}"
    sql += ";"
    return sql

def JSON_SELECT(TABLE: str, DB_FIELD: str, JSON_FIELD: str, WHERE: list) -> str:
    '''
    INCOMPLETE
    
    `EXAMPLE:`
    ###### SELECT json_extract(<`DB_FIELD`>, '$.<`JSON_FIELD`>') AS <`JSON_FIELD`>)
    ###### FROM <`TABLE`>
    ###### WHERE <`WHERE`>;
    '''
    pass

def JSON_WHERE(TABLE: str, DB_FIELD: str, ID, JSON_FIELD: str, VALUE: bool | str | int | float) -> None:
    '''
    INCOMPLETE
    
    `EXAMPLE:`
    ###### SELECT * FROM <`TABLE`>
    ###### WHERE JSON_EXTRACT(<`DB_FIELD`>, '$.`<JSON_FIELD>`') LIKE <'%2023-10%'>;
    '''
    pass


''' TEST
________________________________________________________________________________________________ '''

# sql = JSON_SELECT("CALIBRATIONS", "DB", "TECHNICIAN", [FILTER("Id", "1111")])
# print(sql)

# sql = JSON_UPDATE("CALIBRATIONS", "DB", "FINALIZED", [FILTER("Id", "1111")], True)
# print(sql)