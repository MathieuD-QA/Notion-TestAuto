import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR /".env")

class Notion:
    def __init__(self):
        self.hed = {'Authorization': f'Bearer {os.getenv("NOTION_API_KEY")}',
               'Notion-version': '2022-02-22'}

    def search(self,data = None):
        r = requests.post('https://api.notion.com/v1/search', json=data,headers=self.hed)
        print(r.status_code)
        print(r.json())

    def get_page_id(self):
        r = requests.get('https://api.notion.com/v1/pages/575a4f383f034971b39f75e12b445a77', headers=self.hed)
        print(r.status_code)
        print(r.json())

    def delete_page_id(self):
        r = requests.delete('https://api.notion.com/v1/blocks/be4f2161f49647f59eaf1420f3a88568', headers=self.hed)
        print(r.status_code)
        print(r.json())


    def get_bot(self):
        r = requests.get('https://api.notion.com/v1/users/me', headers=self.hed)
        print(r.status_code)
        print(r.json())

    def get_all_user(self):
        r = requests.get('https://api.notion.com/v1/users?page_size=100', headers=self.hed)
        print(r.status_code)
        print(r.json())

    def get_block_id(self):
        r = requests.get('https://api.notion.com/v1/blocks/575a4f383f034971b39f75e12b445a77', headers=self.hed)
        print(r.status_code)
        print(r.json())


    def get_db_id(self):
        r = requests.get('https://api.notion.com/v1/databases/c9d39095c55444fdb055a30ef835214f', headers=self.hed)
        print(r.status_code)
        print(r.json())


    def createPage(self):
        with open("/Users/mathieu/Desktop/notion_testcafe/createPage.json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
        r = requests.post('https://api.notion.com/v1/pages', json=jsonObject,headers=self.hed)
        print(r.status_code)
        print(r.json())



    def createDB(self):
        with open("/createDB.json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
        r = requests.post('https://api.notion.com/v1/databases', json=jsonObject,headers=self.hed)
        print(r.status_code)
        print(r.json())

testcafe = Notion()
testcafe.createPage()