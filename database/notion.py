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
# import pandas as pd
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
    date = ...
    files = ...
    multi_select = ...
    rich_text = ...
    title = ...

def DB_QUERY(database_id: str):
    '''
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

    for row in query_dict[QUERY_FIELDS.results.value]:
        row_data: dict = row[RESULT_FIELDS.properties.value]
        for field in row_data:
            key: str = field
            data = row_data[field]
            print(key)
            print(data)
            # match data["type"]:
            #     case "title":
            #         value = data["type"][""]
            #         print(data["type"][])
        print()

    return None

DB_QUERY(database_id)

print()
print("FIN")