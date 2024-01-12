r'''
Functions for Using Databases with MS Access
'''
__update__ = '2023.10.11'
__author__ = 'PABLO GONZALEZ PILA <pablopila.spain@gmail.com>'


''' SYSTEM LIBRARIES '''
pass

''' PIP/IMPORTED LIBRARIES '''
import pyodbc

''' CUSTOM LIBRARIES '''
pass


''' MAIN
------------------------------------------ '''

class ACCESS_DB():
    '''
    MS Access Object with some necesary methods to Select and CRUD data base
    '''
    def __init__(self, dbPath: str):
        self.db = dbPath
        self.library = pyodbc
        
    def __CNN_OPEN(self):
        cnn_driver = r"Microsoft Access Driver (*.mdb, *.accdb)"
        cnn_str = f"Driver={cnn_driver};DBQ={self.db}"
        self.CNN = self.library.connect(cnn_str)
        self.CURSOR = self.CNN.cursor()
    
    def __CNN_CLOSE(self):
        self.CURSOR.close()
        self.CNN.close()

    def SQL_EXEC(self, SQL_STR: str, commit: bool = False) -> tuple:
        '''
        Execute a SQL String
        '''
        ## OPEN CONNECTION
        self.__CNN_OPEN()
        ## SQL STRING EXECUTE
        LIST = None
        try:
            self.CURSOR.execute(SQL_STR)
            if commit:
                self.CURSOR.commit()
            else:
                LIST = self.CURSOR.fetchall()
        except:
            print(SQL_STR)
            print("SQL_EXEC ERROR")
        ## CLOSE CONNECTION
        self.__CNN_CLOSE()
        ##
        return LIST
    
    def SQL_TABLES(self) -> list:
        '''
        Get Tables List of selected Acces DB
        '''
        self.__CNN_OPEN()
        LIST: list = []
        for row in self.CURSOR.tables(tableType='TABLE'): # tableType='TABLE' * Para obtener solo las tablas
            LIST.append(row.table_name)
        self.__CNN_CLOSE()
        return LIST