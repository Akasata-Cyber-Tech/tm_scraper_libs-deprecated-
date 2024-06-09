from fastapi import FastAPI, Body, status, Response
from fastapi import APIRouter
from pydantic import BaseModel
import json
from fastapi.responses import RedirectResponse
# from modules.pathData import *
from dotenv import load_dotenv
import os
load_dotenv()
router = APIRouter()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    

class data_malware(BaseModel):
    ID: list[int]
    key: list[str]
    count: list[int]

class suspicious_dns_response_data(BaseModel):
    ID: list[int]
    key: list[str] # domain name
    count: list[int] # domain count
    
class suspicious_dns_request_data(BaseModel):
    ID: list[int]
    key: list[str] # domain name
    count: list[int] # domain count 

@router.get("/get_data/malware")
async def get_malware():
    with open(os.getenv("MALWARE_DATAGROUP_PARSED_PATH"), 'r') as data:
        datas = json.load(data)
        return datas
    
@router.get("/get_data/http_attacks", status_code=200)
async def get_attacks_via_http():
    with open(os.getenv("ATTACKS_DATAGROUP_PARSED_PATH"), 'r') as data:
        datas = json.load(data)
        return datas
    
@router.get("/get_data/suspicious_dns_reponse")
async def get_suspicious_dns_response():
    with open(os.getenv("SUS_BEHAVIOR_DATAGROUP_PARSED_PATH"), 'r') as data:
        datas = json.load(data)
        return datas

@router.get("/get_data/suspicious_dns_request", include_in_schema=False)
async def get_suspicious_dns_request():
    print("On Development!")