'''
¡¡ UNDER TEST!!

Functions for Using Notion API

More info: 
[pypi.org](https://pypi.org/project/notion-client/) / pip install notion-client
[github.com](https://github.com/ramnes/notion-sdk-py)

Get URL Id
[get database URL Id](https://developers.notion.com/docs/working-with-databases) Where can I find my database's ID?
- FORMAT: https://www.notion.so/{workspace_name}/{database_id}?v={view_id}

TASK:
- FILTERS in QUERY

WARNINGS:
- ...

'''

__update__ = '2024.01.12'
__author__ = 'PABLO GONZALEZ PILA <pablopila.spain@gmail.com>'

''' SYSTEM LIBRARIES '''
import os
from dataclasses import dataclass
from enum import Enum
import pandas as pd
from dotenv import load_dotenv
from notion_client import Client


''' MAIN
------------------------------------------ '''

## TOKEN
filePath = "database/notion.env"
load_dotenv(dotenv_path=os.path.join(os.getcwd(), filePath))
notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id: str = os.getenv("DATABASE_ID")

## FUNCTIONS
# v: dict = notion.databases.query(database_id)
# print(v)
# print()

# for key in v.keys():
#     print(key)
#     # print(v[key])
#     print()

# for row in v["results"]:
#     for field in row:
#         print(field)
#     print()

class QUERY_FIELDS(Enum):
    object: str = "object"
    results = "results"
    next_cursor = "next_cursor"
    has_more = "has_more"
    type: str = "type"
    page_or_database: str = "page_or_database"
    request_id: str = "request_id"

class RESULT_FIELDS(Enum):
    '''
    - object
    - id
    - created_time
    - last_edited_time
    - created_by: dict
    - last_edited_by
    - cover
    - icon
    - parent
    - archived
    - properties: dict
    - url
    - public_url
    '''
    object = "object"
    id = "id"
    created_time = "created_time"
    last_edited_time = "last_edited_time"
    created_by = "created_by"
    last_edited_by = "last_edited_by"
    cover = "cover"
    icon = "icon"
    parent = "parent"
    archived = "archived"
    properties = "properties"
    url = "url"
    public_url = "public_url"

class TYPES(Enum):
    '''
    '''
    checkbox = "checkbox"
    date = "date"
    files = "files"
    multi_select = "multi_select" # TAGS / LABELS
    number = 'number'
    rich_text = "rich_text"
    title = "title"
    @classmethod
    def GET_DATA(cls, NOTION_DATA):
        '''
        '''
        match NOTION_DATA["type"]:
            case cls.checkbox.value:
                return bool(NOTION_DATA['checkbox'])
            case cls.number.value:
                return float(NOTION_DATA['number'])
            case cls.rich_text.value | cls.title.value:
                text_data = str()
                for e in NOTION_DATA[NOTION_DATA["type"]]:
                    text_data += e['plain_text']
                return text_data
            case _:
                return None


def DB_QUERY(database_id: str):
    '''
    Get data from Notion DataBase
    '''
    query_dict: dict = notion.databases.query(database_id)

    ## COMPLETE QUERY
    # print(query_dict)
    # print()

    ## RESULTS FIELD QUERY
    # for field in query_dict[QUERY_FIELDS.results.value][0]:
    #     print(field)
    #     print(query_dict[QUERY_FIELDS.results.value][0][field])
    #     print()

    ## QUERY
    # df: pd.DataFrame = pd.DataFrame(query_dict[QUERY_FIELDS.results.value])
    # df.to_csv(os.path.join(r"C:\Users\GONZA_PA\Desktop\TEMP", "ejemplo.csv"), index = False)
    # print(df.columns)
    # print(df)

    data_list: list = list()
    for row in query_dict[QUERY_FIELDS.results.value]:
        row_data: dict = row[RESULT_FIELDS.properties.value]
        fields_dict = dict()
        for field in row_data:
            key: str = field
            data = row_data[field]
            print()
            print(key)
            print(data)
            fields_dict[key] = TYPES.GET_DATA(data)
        data_list.append(fields_dict)
    DF: pd.DataFrame = pd.DataFrame(data_list)
    print()
    print(DF)
    return None

DB_QUERY(database_id)

print()
print("FIN")