'''
Toolkit with simplified functions and methods for development with Python
- Operating System functions
- Internet Connection
- Datetime formats and converters


TASK:
    mypyc --ignore-missing-imports func_system.py
    ...

    
WARNINGS:
    - The License functions have many errors to compile using mypyc
    - The <pyperclip.copy> function is very simple, it is better to remove it from this module, or add --ignore-missing-imports option with mypyc compyle

________________________________________________________________________________________________ '''

__version__ = '2024.01.13' # + '_Compiled'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

''' SYSTEM LIBRARIES '''
import os
import platform, time, locale
from datetime import datetime
# import hashlib
# import urllib.request # INTERNET CONNECTION
from socket import gethostbyname # INTERNET CONNECTION
# from dataclasses import dataclass, fields, MISSING
from glob import glob
import enum
from enum import Enum, auto
from typing import List
# from importlib import import_module

''' PIP/IMPORTED LIBRARIES '''
# import pyperclip # type: ignore[import-untyped]


''' FUNCTIONS
________________________________________________________________________________________________ '''

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

def PATH_VALIDATE(path: str) -> str:
    '''
    Check and remove invalid characters
    '''
    ## ASCII
    invalids_int: List[int] = [10, 32, 34, 39, 42, 47, 58, 59, 60, 62, 63, 92, 94, 96, 124]
    invalids: List[str] = [chr(c) for c in invalids_int]
    # 
    valid_path: str = path
    for c in invalids:
        if c in valid_path:
            valid_path = valid_path.replace(c, str())
    return valid_path

class PATH_BASENAME(Enum):
    '''
    '''
    PATH = auto()
    BASENAME = auto()
    EXTENSION = auto()
    EXTENSION_ONLY = auto()
    @classmethod
    def GET(cls, path: str, option: enum):
        '''
        '''
        BASENAME: str = os.path.basename(path)
        SPLIT: List[str] = BASENAME.split(".")
        if option == cls.PATH:
            return path.replace(BASENAME, '')
        if option == cls.BASENAME:
            return BASENAME
        if option == cls.EXTENSION:
            if len(SPLIT) == 2:
                return SPLIT[1]
            else:
                return None

def PATH_FIND(path: str) -> List[str]:
    '''
    Get a list of files with especified name

    - path: str = "<your_path>/*.exe"
    '''
    return glob(path)

## DATE FUNCTIONS

class DATE_STR_FORMATS(Enum):
    YYYY_MM_DD = r'%Y-%m-%d'
    ISO_8601 = r'%Y-%m-%d'
    DATE_NOW = r"%Y-%m-%d / %H:%M"
    NOW = r"%H:%M"

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

BOOLEANS: tuple = ("TRUE", True, 1, "1", "On", "ON")

# def INT_TWODIGITS(INT: int) -> str:
#     '''
#     Convert Integer to two digit string
#     1 --> 01
#     '''
#     ORDR = f'{INT:02d}'
#     return ORDR


''' TEST
________________________________________________________________________________________________ '''

# def COPY2CLIPBOARD(TEXT: str) -> None:
#     '''
#     Add selected data to clipboard
#     '''
#     pyperclip.copy(TEXT)


# from inspect import getmembers, isfunction, isclass # OBJECTS CHECK

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