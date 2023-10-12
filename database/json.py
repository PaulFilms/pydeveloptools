r'''
Functions for using collections in json format

DEBUG:
    - Son funciones muy sencillas hay que intentar usar las funciones nativas
'''
__update__ = '2023.10.11'
__author__ = 'PABLO GONZALEZ PILA <pablopila.spain@gmail.com>'


''' SYSTEM LIBRARIES '''
import json

''' CUSTOM LIBRARIES '''


''' MAIN
------------------------------------------ '''

def json_load(filePath: str) -> dict:
    '''
    '''
    file = f"{filePath}.json"
    dictionary = {}
    with open(file, "r") as read_file:
        dictionary = json.load(read_file)
    return dictionary

def json_save(dictionary: dict, filePath: str) -> None:
    '''
    '''
    file = f"{filePath}.json"
    with open(file, 'w') as f:
        json.dump(dictionary, f)

def dict_to_json(dictionary=dict):
    '''
    La función "loads" decodifica una información JSON a Diccionario de Python
    '''
    if type(dictionary) != dict:
        print("CLASS TYPE ERROR / dict_to_json")
        return {}
    d = json.dumps(dictionary)
    # d = json.loads(d)
    return d

def json_to_dict(JSON):
    '''
    INCOMPLETE:
        No funciona
    '''
    DICT = {}
    DICT = json.load(JSON)
    return DICT

def json_to_datframe():
    '''
    INCOMPLETE
    Sin hacer
    '''
    print('json_to_datframe')