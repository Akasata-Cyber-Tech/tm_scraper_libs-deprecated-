from fastapi import FastAPI, Body, status, Response, HTTPException
from fastapi import APIRouter
from pydantic import BaseModel
import json
from fastapi.responses import RedirectResponse
# from fastapi_session import FastAPISession, SessionData
# from modules.pathData import *
from dotenv import load_dotenv
from database.crud.reports.insert_report_data import insert_attack_data
import os
import utils.selenium.get_session as get_session
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

class Login(BaseModel):
    username: str
    password: str



@router.post("/login/")
async def authLogin(login: Login):
    return {"username": login.username, "password": login.password, "token":get_session.login(username=login.username,password=login.password)}
