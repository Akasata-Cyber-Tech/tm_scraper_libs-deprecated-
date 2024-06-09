from fastapi import FastAPI, Body, status, Response
from pydantic import BaseModel
import requests
import json
import sys
import uvicorn
from fastapi.responses import RedirectResponse
# from modules.pathData import *
import api.router.reportAPI as reportAPI
import api.router.postReportData as postResport
router = FastAPI()

app = FastAPI()

app.include_router(reportAPI.router,tags=["getData"])
app.include_router(postResport.router,tags=["postData"])

@app.get("/")
def read_root():
    return {"message": "Welcome to my modular FastAPI application"}

if __name__ == '__main__':
    try:
        host = "127.0.0.1"
        port = 8959
        # workers_num = 4  # Number of worker processes
        # log_config = "log/config.yaml"  #
        uvicorn.run("main:app", host=host, port=port, reload=True)    
    except KeyboardInterrupt:
        # print(f'{err} : error')
        sys.exit("error")