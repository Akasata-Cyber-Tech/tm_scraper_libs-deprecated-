from fastapi import FastAPI, Body, status, Response, HTTPException
from fastapi import APIRouter
from pydantic import BaseModel
import json
from fastapi.responses import RedirectResponse
# from modules.pathData import *
from dotenv import load_dotenv
from database.crud.reports.insert_report_data import insert_attack_data
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

class http_attack_data(BaseModel):
    ID: list[int]
    key: list[str] # domain name
    count: list[int] # domain count 

@router.post("/post_data/malware")
async def post_malware(data: data_malware):
    try:
        print("post database Logic Here!")
    except:
        print("Exception For Error Here1")

    # Simulate a check if the user already exists
    if data.username == "existing_user":
        raise HTTPException(status_code=400, detail="Username already taken")
    
    # Here you would typically save the user to the database
    # For this example, we're just returning the user data
    return data

    
@router.post("/post_data/http_attacks")
async def post_attack_data_via_http(data: http_attack_data):
    try:
        print("post database Logic Here!")
    except:
        print("Exception For Error Here1")

    # Here you would typically save the user to the database
    # For this example, we're just returning the user data
    return data

    
@router.post("/post_data/suspicious_dns_request")
async def post_attack_data_via_http(data: suspicious_dns_request_data):
    try:
        print("post database Logic Here!")
    except:
        print("Exception For Error Here1")
        
    # Here you would typically save the user to the database
    # For this example, we're just returning the user data
    return data

@router.post("/post_data/suspicious_dns_response")
async def post_attack_data_via_http(data: suspicious_dns_response_data):
    try:
        print("post database Logic Here!")
    except:
        print("Exception For Error Here1")
        
    # Here you would typically save the user to the database
    # For this example, we're just returning the user data
    return data
# @router.get("/post_data/suspicious_dns_request", include_in_schema=False)
# async def get_suspicious_dns_request():
#     print("On Development!")