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
import api.router.report_generator as generateResport
import api.router.auth as auth
# router = FastAPI()

app = FastAPI()

app.include_router(auth.router,tags=["Auth"])
app.include_router(reportAPI.router,tags=["getData"])
# app.include_router(postResport.router,tags=["postData"])
app.include_router(generateResport.router,tags=["generateReport"])

@app.get("/")
def read_root():
    return {"message": "Welcome to my modular FastAPI application"}

if __name__ == '__main__':
    try:
        host = "0.0.0.0"
        port = 8959
        # workers_num = 4  # Number of worker processes
        # log_config = "log/config.yaml"  #
        uvicorn.run("main:app", host=host, port=port, reload=True)    
        # serve(app, host='0.0.0.0', port=8959,url_scheme='https', threads=4, channel_timeout=120, cleanup_interval=30)

    except KeyboardInterrupt:
        # print(f'{err} : error')
        sys.exit("error")