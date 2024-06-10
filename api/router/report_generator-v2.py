from fastapi import FastAPI, Body, status, Response, HTTPException
from fastapi.responses import FileResponse
from fastapi import APIRouter
from pydantic import BaseModel
import json
from fastapi.responses import RedirectResponse
from modules.pathData import CSV_ATTACKS_DATAGROUP_BY_SOURCE, CSV_ATTACKS_DATAGROUP_BY_RULENAME, CSV_ATTACKS_DATAGROUP_BY_INDICATOR
from modules.pathData import CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_SOURCE, CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_DESTINATION,CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_RULENAME, CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_INDICATOR 
from modules.pathData import CSV_MALWARE_DATAGROUP_BY_SOURCE, CSV_MALWARE_DATAGROUP_BY_DESTINATION,CSV_MALWARE_DATAGROUP_BY_RULENAME, CSV_MALWARE_DATAGROUP_BY_INDICATOR 
from modules.logs_scraper import search_data_groups
from modules.logs_scraper import seach_query
from utils.selenium.web_driver import get_token
from utils.generator.generate_csv import generate_csv
from utils.data_parser import json_editor 
from dotenv import load_dotenv
from modules.keywords_data import keywords
# from frontend.CLI.choices import 
import os
import zipfile
load_dotenv()
router = APIRouter()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    

class report_shift1(BaseModel):
    ID: list[int]
    key: list[str]
    count: list[int]

class report_shift2(BaseModel):
    ID: list[int]
    key: list[str] # domain name
    count: list[int] # domain count
    
class report_shift3(BaseModel):
    ID: list[int]
    key: list[str] # domain name
    count: list[int] # domain count 

# Define the paths to the files you want to include in the ZIP archive
file_paths = [
    CSV_ATTACKS_DATAGROUP_BY_SOURCE,
    CSV_ATTACKS_DATAGROUP_BY_RULENAME,
    # CSV_ATTACKS_DATAGROUP_BY_INDICATOR,
    CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_SOURCE,
    # CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_DESTINATION,
    CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_RULENAME,
    CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_INDICATOR,
    CSV_MALWARE_DATAGROUP_BY_SOURCE,
    CSV_MALWARE_DATAGROUP_BY_INDICATOR,
]

@router.get("/generate/report-shift1-batch")
async def generate_report_shift1():
    filepath = file_paths
    loops = 0
    while(loops < 2):
        try:
            if os.path.isfile(filepath[loops]):
                os.remove(filepath[loops])
                print(f"File {filepath[loops]} removed successfully.")
            else:
                print(f"No file found at {filepath[loops]}.")
            loops +=1
        except Exception as e:
            print(f"Error: {e}")
            loops +=1
    token = get_token()
    keyword = [keywords.keywords_suspicious_dns_response,keywords.keywords_suspicious_dns_response,keywords.keyword_malware,keywords.keyword_behavior_violation]
    groups = ["attacks","suspicious_dns","malware","behavior_violation"]
    isPer3H = False
    loops = 0
    while(loops < 3):
        seach_query(token, keyword[loops], groups[loops])
        search_data_groups(token, keyword[loops], groups[loops],isPer3H)
        loops +=1
    json_editor()
    generate_csv()
    zip_filename = os.getenv("ZIPFILE")
    # Check if the files exist
    for file_path in file_paths:
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail=f"File not found: {file_path}")

    # Create a ZIP file
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file_path in file_paths:
            zipf.write(file_path, os.path.basename(file_path))

    # Return the ZIP file as a response
    return FileResponse(
        path=zip_filename,
        filename="reports_data.zip",
        media_type='application/zip'
    )
    
@router.get("/generate/report-shift2", status_code=200)
async def generate_report_shift2():
    with open(os.getenv("ATTACKS_DATAGROUP_PARSED_PATH"), 'r') as data:
        datas = json.load(data)
        return datas@router.get("/generate/report-shift1")
async def generate_report_shift1():
    if os.path.exists(CSV_ATTACKS_DATAGROUP_BY_SOURCE):
        return FileResponse(
            path=CSV_ATTACKS_DATAGROUP_BY_SOURCE,
            filename="downloaded_file.csv",
            media_type='application/csv'
        )
    else:
        raise HTTPException(status_code=404, detail="File not found")
    
@router.get("/generate/report-shift2", status_code=200)
async def generate_report_shift2():
    with open(os.getenv("ATTACKS_DATAGROUP_PARSED_PATH"), 'r') as data:
        datas = json.load(data)
        return datas

@router.get("/generate/report-shift1")
async def generate_report_shift1():
    if os.path.exists(pdf_file_path):
        return FileResponse(
            path=pdf_file_path,
            filename="downloaded_file.pdf",
            media_type='application/pdf'
        )
    else:
        raise HTTPException(status_code=404, detail="File not found")
    
@router.get("/generate/report-shift2", status_code=200)
async def generate_report_shift2():
    with open(os.getenv("ATTACKS_DATAGROUP_PARSED_PATH"), 'r') as data:
        datas = json.load(data)
        return datas
    
@router.get("/generate/report-shift3")
async def generate_report_shift3():
    with open(os.getenv("SUS_BEHAVIOR_DATAGROUP_PARSED_PATH"), 'r') as data:
        datas = json.load(data)
        return datas

@router.get("/generate/report-per2h", include_in_schema=False)
async def generate_report_per2h():
    print("On Development!")

@router.get("/download-pdf")
async def download_pdf():
    if os.path.exists(pdf_file_path):
        return FileResponse(
            path=pdf_file_path,
            filename="downloaded_file.pdf",
            media_type='application/pdf'
        )
    else:
        raise HTTPException(status_code=404, detail="File not found")