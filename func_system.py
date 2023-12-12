'''
Toolkit with simplified functions and methods for development with Python
- Operating System
- Internet
- Datetime

\n
`TASK:`
    mypyc --ignore-missing-imports func_system.py

\n
WARNINGS:
    - The License functions have many errors to compile using mypyc
    - The <pyperclip.copy> function is very simple, it is better to remove it from this module, or add --ignore-missing-imports option with mypyc compyle
'''
__version__ = '2023.12.12' # + '_Compiled'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import os
import platform, time, locale
from datetime import datetime
# import hashlib
# import urllib.request # INTERNET CONNECTION
from socket import gethostbyname # INTERNET CONNECTION
from inspect import getmembers, isfunction, isclass # OBJECTS CHECK
from dataclasses import dataclass, fields, MISSING
from enum import Enum
# from importlib import import_module

''' PIP/IMPORTED LIBRARIES '''
import pyperclip # type: ignore[import-untyped]


''' FUNCTIONS
--------------------------------------------------------
'''

## OPERATING SYSTEM

def OS_GET_SYSTEM() -> str:
    '''
    Returns the system OS name 
    '''
    return platform.system()

def OS_GET_MACHINE() -> str:
    '''
    Returns the system Device name
    '''
    return platform.node()

def OS_GET_LOGIN() -> str:
    '''
    Get User SO Log-In Id in str format
    '''
    return os.getlogin()

def OS_GET_DECIMAL() -> str:
    '''
    Get the decimal separator used by the system
    '''
    return str(locale.localeconv()['decimal_point'])

def COPY2CLIPBOARD(TEXT: str) -> None:
    '''
    Add selected data to clipboard
    '''
    pyperclip.copy(TEXT)

def INTERNET_CONNECTION_CHECK(URL: str = r'www.seatable.io') -> bool:
    '''
    Check if the selected URL connection is available.

    Args:
        URL (str): The URL to check for connectivity.

    Returns:
        bool: True if connection is available, False if connection is not available.

    Info:
        Some generic URLs may not work as expected.

        Tested URLs:
            - www.google.com
            - www.rohde-schwarz.com
            - www.seatable.io
    
    Previously used: \n
    
    ```python
    try:
        urllib.request.urlopen(URL, timeout=5) # import urllib.request
        return True
    except:
        return False
    # Tested URLs: https://www.google.com | https://cloud.seatable.cn/ | https://www.rohde-schwarz.com/
    ```
    Both methods are valid and can be used to check for internet connectivity:
    - The socket method is a bit faster and simpler, as it only tries to resolve a DNS address. 
    - The urllib method is more comprehensive, as it tries to establish a connection to a URL and can handle more complex scenarios, but it may be slower due to the additional overhead.
    '''
    try:
        gethostbyname(URL)
        return True
    except:
        return False


## PATH FUNCTIONS

def PATH_OPEN(path: str = os.getcwd()) -> None:
    ''' 
    Open the selected path
    '''
    os.startfile(path)

def PATH_OPEN_TERMINAL(path: str = os.getcwd()) -> None:
    '''
    Open the selected path using the terminal
    '''
    realpath = os.path.realpath(path)
    os.system(f'start {realpath}')

def PATH_FOLDER_NEW(path: str, folder_name: str) -> None:
    '''
    Create a new folder in selected path
    '''
    NEW_FOLDER = os.path.join(path, folder_name)
    os.mkdir(NEW_FOLDER)

def PATH_GET_DESKTOP() -> str:
    '''
    Returns Desktop Path in str format
    '''
    return os.path.join(os.path.expanduser('~'), 'Desktop')

def PATH_EXIST_CHECK(path: str) -> bool:
    '''
    Check if selected path or file exist 
    '''
    return os.path.exists(path)


## DATE FUNCTIONS

class DATE_STR_FORMATS(Enum):
    YYYY_MM_DD = r'%Y-%m-%d'
    ISO_8601 = r'%Y-%m-%d'
    DATE_NOW = r"%Y-%m-%d / %H:%M"

def DATE_GET_TODAY() -> str:
    '''
    Returns Date in str format like ' yyyy-mm-dd '
    '''
    return datetime.now().strftime(DATE_STR_FORMATS.YYYY_MM_DD.value)

def DATE_GET_NOW(format: str = DATE_STR_FORMATS.DATE_NOW.value) -> str:
    '''
    Returns Date Time in str (default) format like 'yyyy-mm-dd / hh:mm'
    '''
    return str(datetime.now().strftime(format))

def DATE_ISO(DATE: datetime) -> str:
    '''
    Convert date to ISO Format 'yyyy-mm-dd'
    '''
    return f"{DATE.year}-{DATE.month}-{DATE.day:02d}"

def GET_FIRM() -> str:
    '''
    Returns string with OS Login Id and Date in format ' yyyy-mm-dd / hh:mm '
    '''
    return f"{os.getlogin()} [{DATE_GET_NOW()}]"


## IMAGES FUNCTIONS

def IMG_PIXEL2CM(PIXELS: float) -> float:
    '''
    Convert from pixels value to centimeters value
    '''
    return PIXELS * 0.0264583333

def IMG_CM2PIXEL(CM: float) -> float:
    '''
    Convert from centimeters value to pixels value 
    '''
    return CM * 37.795275591


## MISCELLANEOUS FUNCTIONS

def INT_TWODIGITS(INT: int) -> str:
    '''
    Convert Integer to two digit string
    1 --> 01
    '''
    ORDR = f'{INT:02d}'
    return ORDR

# def ENCODE_STR(STR: str) -> str:
#     '''
#     Encode selected STR
#     '''
#     return hashlib.sha256(str(STR).encode('utf-8')).hexdigest()


''' TEST
--------------------------------------------------------
'''

# def OBJECT_CHECK(OBJECT, objectType: str = 'function', onlyNames: bool = False) -> list:
#     '''
#     - OBJECT: Library from importlib
#     - objectType: 'function' (for function objects) / 'class' (for class objects)
#     - onlyNames:
#         - True (Return a List with al the selected objects in the library)
#         - False (Return a List with a tuple with object name and the object)
    
#     INCOMPLETE:
#     - Cuando el objeto es creado desde importlib no se pasa path
#     - No he comprobado si puedes pasar un path, directamente un import, etc.
#     '''
#     if objectType != 'function' and objectType != 'class':
#         print("OBJECT_CHECK ERROR / objectType not supported")
#         return []
#     if objectType == 'function':
#         LIST = getmembers(OBJECT, isfunction)
#     if objectType == 'class':
#         LIST = getmembers(OBJECT, isclass)
#     if onlyNames:
#         LIST = [func[0] for func in LIST]
#     return LIST

# ## LICENSE FUNCTIONS

# def LICENSE_TXT(file, appName: str, loginId: str, limitOpens: int, limitDate: int) -> None:
#     '''
#     Make a LICENSE FILE with the next atributes:
#     - file (str) / Address and name of the file
#     - appName (str) / Name of the Application
#     - loginId (str) / Id of the OS User
#     - limitOpens (int) / Maximun Opens
#     - limitDate (int) / Maximun Date example: 20230601
    
#     INCOMPLETE:
#         - Hay que añadir la fecha de creación
#     '''
#     ## INIT FILE
#     with open(file, 'w') as f:
#         f.write('')
#     ## ENCODE
#     app = f"@{appName}"
#     app = hashlib.sha256(app.encode('utf-8')).hexdigest()
#     login = f"@{loginId}"
#     login = hashlib.sha256(login.encode('utf-8')).hexdigest()
#     opens = f"@{limitOpens}"
#     opens = hashlib.sha256(opens.encode('utf-8')).hexdigest()
#     date = f"@{limitDate}"
#     date = hashlib.sha256(date.encode('utf-8')).hexdigest()
#     ## CREATION TIME FILE
#     createTime = os.path.getctime(file)
#     createTime = time.ctime(createTime)
#     createTime = f"@{createTime}"
#     createTime = hashlib.sha256(createTime.encode('utf-8')).hexdigest()
#     ## MODIFICATION TIME FILE
#     modTime = os.path.getmtime(file)
#     modTime = time.ctime(modTime)
#     modTime = f"@{modTime}"
#     modTime = hashlib.sha256(modTime.encode('utf-8')).hexdigest()
#     ## EDIT FILE
#     txtList = [app, login, opens, date, createTime, modTime]
#     with open(file, 'w') as f:
#         f.write('\n'.join(txtList))

# def LICENSE_TXT_DATA(file) -> dict:
#     '''
#     Get data in the file

#     INCOMPLETE:
#     - Esta funcion se usa una vez dentro de la APP poder obtener los valores de la licencia
#     - Hay que integrar esta funcion dentro de LICENSE_TXT_CHECK
#     '''
#     data = {
#         'login': "FAIL",
#         'opens': 0,
#         'date': 0,
#         }
    
#     ## OPEN FILE
#     if os.path.exists(file):
#         with open(file, 'r') as f:
#             txt = f.readlines()
#     else:
#         return data
#     ## LOGIN
#     login = f"@{OS_GET_LOGIN()}"
#     login = hashlib.sha256(login.encode('utf-8')).hexdigest()
#     if login == txt[1].replace(chr(10), ""): 
#         data['login'] = "PASS"
#     ## OPENS
#     opens = 0
#     for i in range(0, 2000):
#         hash = f"@{i}"
#         hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
#         if hash == txt[2].replace(chr(10), ""):
#             opens = i
#             # print("limitOpens: PASS", opens)
#             data['opens'] = opens
#             break
#         if i == 1999:
#             # print("ERROR / limitOpens")
#             data['opens'] = 0
#             # return False
#     ## DATE
#     date = 0
#     for i in range(20230101, 20250101):
#         hash = f"@{i}"
#         hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
#         if hash == txt[3].replace(chr(10), ""):
#             date = i
#             # print("limitDate: PASS", date)
#             data['date'] = date
#             break
#     return data

# def LICENSE_TXT_CHECK(file, appName: str, debug: bool = False) -> bool:
#     '''
#     appName, loginId, limitOpens, limitDate, modTime

#     INCOMPLETE:
#         - Si no encuentra el fichero devuelve False
#     '''

#     ## OPEN FILE
#     if os.path.exists(file) == False:
#         return False
    
#     with open(file, 'r') as f:
#         txt = f.readlines()

#     ## CHECK
#     if len(txt) == 6:
#         # 
#         app = f"@{appName}"
#         app = hashlib.sha256(app.encode('utf-8')).hexdigest()
#         if app == txt[0].replace(chr(10), ""):
#             if debug: print("appName: PASS")
#             pass
#         else:
#             if debug: print("ERROR / appName")
#             return False
#         # 
#         login = f"@{os.getlogin()}"
#         login = hashlib.sha256(login.encode('utf-8')).hexdigest()
#         if login == txt[1].replace(chr(10), ""): 
#             if debug: print("loginId: PASS")
#             pass
#         else:
#             if debug: print("ERROR / loginId")
#             return False
#         # 
#         opens = None
#         for i in range(0, 2000):
#             hash = f"@{i}"
#             hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
#             if hash == txt[2].replace(chr(10), ""):
#                 opens = i
#                 if debug: print("limitOpens: PASS", opens)
#                 break
#             if i == 1999:
#                 if debug: print("ERROR / limitOpens")
#                 return False
#         # 
#         for i in range(20230101, 20250101):
#             hash = f"@{i}"
#             hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()
#             if hash == txt[3].replace(chr(10), ""):
#                 date = i
#                 if debug: print("limitDate: PASS", date)
#                 break
#             if i == 20250100:
#                 if debug: print("ERROR / limitDate")
#                 return False
#         # 
#         createTime = os.path.getctime(file)
#         createTime = time.ctime(createTime)
#         createTime = f"@{createTime}"
#         createTime = hashlib.sha256(createTime.encode('utf-8')).hexdigest()
#         if createTime == txt[4].replace(chr(10), ""): 
#             if debug: print("createTime: PASS")
#             pass
#         else:
#             if debug: print("ERROR / createTime")
#             return False
#         # 
#         modTime = os.path.getmtime(file)
#         modTime = time.ctime(modTime)
#         modTime = f"@{modTime}"
#         modTime = hashlib.sha256(modTime.encode('utf-8')).hexdigest()
#         if modTime == txt[5].replace(chr(10), ""): 
#             if debug: print("modTime: PASS")
#             pass
#         else:
#             if debug: print("ERROR / modTime")
#             return False
        
#         ## EDIT FILE
#         opens -= 1
#         opens = f"@{opens}"
#         opens = hashlib.sha256(opens.encode('utf-8')).hexdigest()
#         # 
#         with open(file, 'w') as f:
#             f.write('')
#         now = os.path.getmtime(file)
#         now = time.ctime(now)
#         now = f"@{now}"
#         now = hashlib.sha256(now.encode('utf-8')).hexdigest()
#         with open(file, 'w') as f:
#             f.write('\n'.join(
#                 [txt[0].replace(chr(10), ""), 
#                 txt[1].replace(chr(10), ""), 
#                 opens, 
#                 txt[3].replace(chr(10), ""), 
#                 createTime, 
#                 now
#                 ]))
#         # 
#         return True
#     # 
#     else: 
#         return False



# def dataClass_to_dict(DATACLASS: dataclass) -> dict:
#     '''
#     Get a dictionary from a dataclass

#     DEBUG:
#         Creo que es mejor usar un pydantic si la finalidad es obtener un dict
#     '''
#     DICT = dict()
#     for field in fields(DATACLASS):
#         FIELD = field.name
#         VALUE = field.value
#         TYPE = field.type
#         DEFAULT = field.default
#         if DEFAULT == MISSING:
#             DICT[FIELD] = TYPE
#         else:
#             DICT[FIELD] = DEFAULT
#     return DICT