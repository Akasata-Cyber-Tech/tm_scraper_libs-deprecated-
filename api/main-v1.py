from fastapi import FastAPI, Body, status, Response
from pydantic import BaseModel
import requests
import json
import sys
import uvicorn
from fastapi.responses import RedirectResponse
from modules.pathData import *
app = FastAPI()

responses={
    200: {"description": "Everything worked as expected"},
    400: {"description": "Bad Request", "content": {"application/json": {"example": {"error": "Missing parameter"}}}},
    401: {"description": "Unauthorized", "content": {"application/json": {"example": {"error": "No valid API key provided"}}}},
    # Add more custom responses as needed
    
}

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    

class data_malware(BaseModel):
    ID: list[int]
    key: list[str]
    count: list[int]
# app.get/post("/path", response_model, status_code)
#  async def fungsi(param1=parameter_url: tipe data, param2=request_body: Model = examples)
    # return= kembalikan nilai

class suspicious_dns_response_data(BaseModel):
    ID: list[int]
    key: list[str] # domain name
    count: list[int] # domain count
    
class suspicious_dns_request_data(BaseModel):
    ID: list[int]
    key: list[str] # domain name
    count: list[int] # domain count 

# FastAPI Guide

# app.get/post("/path", response_model, status_code)
#  async def fungsi(param1=parameter_url, param2=request_body)
    # return= kembalikan nilai

class Get():
    def malware_data():
        @app.get("/get_data/malware")
        async def get_malware():
            with open(MALWARE_DATAGROUP_PARSED_PATH, 'r') as data:
                datas = json.load(data)
                # response.status_code = status.HTTP_201_CREATED
                # print(datas)
                return datas
    def get_http_attack_data():    
    @app.get("/get_data/http_attacks", status_code=200)
    async def get_attacks_via_http():
        with open(ATTACKS_DATAGROUP_PARSED_PATH, 'r') as data:
            datas = json.load(data)
            # response.status_code = status.HTTP_201_CREATED
            
            # response.status_code = status.HTTP_201_CREATED
            # print(datas)
            return datas
        
class Login(BaseModel):
    username: str
    password: str

@app.post("/items/")
async def create_item(login: Login):
    return {"username": login.username, "password": login.password}

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

def note():
    @app.get("/note", include_in_schema=False)
    async def root():
        return RedirectResponse(url="/docs")\
    
@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        examples={
            "Normal": {"value": {"name": "Foo", "price": 35.4}},
            "Converted": {"value": {"name": "Bar", "price": 42.0}},
        }
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
# url = "https://mocki.io/v1/2cc61cdd-33f9-4173-a46b-03659adbee07"
# response = requests.get(url)
# datas = response.json()




    
def get_
@app.get("/get_data/suspicious_dns_reponse")
async def get_suspicious_dns_response():
    with open(SUS_BEHAVIOR_DATAGROUP_PARSED_PATH, 'r') as data:
        datas = json.load(data)

@app.get("/get_data/suspicious_dns_request", include_in_schema=False)
async def get_suspicious_dns_request():
    print("On Development!")
    
@app.get("/whois/{ip}", include_in_schema=False)
async def whois_ip():
    print("On Development")
    
@app.get("/abuse_data/{ip}", include_in_schema=False)
async def get_abuse_ipdb():
    print("On Development!")
    



# @app.get("/get_data/{type}", status_code=200)
# async def get_data(type: str):
#     if type == "malware":
        
#         with open(MALWARE_DATAGROUP_PARSED_PATH, 'r') as data:
#             datas = json.load(data)

#             return datas
#     elif type == "attacks":

#         with open(ATTACKS_DATAGROUP_PARSED_PATH, 'r') as data:
#             datas = json.load(data)
#             return datas
#     else:
#         return {'message': 'tolong masukan request yang benar'}
    
# @app.get("/get_data/attacks")
# async def get_attacks():
#     url = "https://mocki.io/v1/5859d617-a291-447f-91c8-0e514b4bc87a"
#     response = requests.get(url)
#     datas = response.json()
#     return datas

# def run():
if __name__ == '__main__':
    try:
        host = "127.0.0.1"
        port = 8859
        # workers_num = 4  # Number of worker processes
        # log_config = "log/config.yaml"  #

        uvicorn.run("main:app", host=host, port=port, reload=True)    
    except KeyboardInterrupt:
        # print(f'{err} : error')
        sys.exit("error")
    