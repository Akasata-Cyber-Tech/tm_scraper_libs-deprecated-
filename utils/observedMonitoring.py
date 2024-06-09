from modules.pathData import *
import pickle
import json
import requests
# from utils.helper import timestamp
from icecream import ic
from datetime import datetime
from utils.monitors.monitoring_authLogin import export_monitorData


def observedMonitoring(token):
    # https://portal.sg.xdr.trendmicro.com/ui/th/api/v2/detections
#     riskLevels: critical
# riskLevels: high
# riskLevels: medium
# riskLevels: info
# riskLevels: low
# start: 1714348466
# end: 1714352066
# size: 50
# retryCount: 0
    now = datetime.now()
    to_timestamp = int(now.timestamp())
    from_timestamp = int(to_timestamp -(600))
    
    riskLevels = ["critical","high","medium","low","info"]

    # payload = {
    # "riskLevels": "critical",
    # "riskLevels": "high",
    # "riskLevels": "medium",
    # "riskLevels": "low",
    # # "riskLevels": "info",
    # "start": int(from_timestamp),
    # "end": int(to_timestamp),
    # "size": 50,
    # "retryCount": 0
    # }  
    index =0
    while(index < len(riskLevels)):
        payload = {
        "riskLevels": riskLevels[index],
        # "riskLevels": "info",
        "start": int(from_timestamp),
        "end": int(to_timestamp),
        "size": 50,
        "retryCount": 0
        } 


        params = {}

        if index == 0:
            filepath = CRITICAL_MONITORING_OBSERVED_DATA_PATH
            raw_datapath = CRITICAL_OBSERVED_DATA_PATH
        elif index ==1:
            filepath = HIGH_MONITORING_OBSERVED_DATA_PATH
            raw_datapath = HIGH_OBSERVED_DATA_PATH
        elif index ==2:
            filepath = MEDIUM_MONITORING_OBSERVED_DATA_PATH
            raw_datapath = MEDIUM_OBSERVED_DATA_PATH
        elif index ==3:
            filepath = LOW_MONITORING_OBSERVED_DATA_PATH
            raw_datapath = LOW_OBSERVED_DATA_PATH
        elif index ==4:
            filepath = INFO_MONITORING_OBSERVED_DATA_PATH
            raw_datapath = INFO_OBSERVED_DATA_PATH

        # filterNames: -Equated%20Exploit%20Attempt%20SMB%20%28Response%29%20-%20Outbound
        # filterNames: -Suspicious Detection in Private Networks

        uri = 'https://portal.sg.xdr.trendmicro.com/ui/th/api/v2/detections'

        headers = {'Content-type': 'application/json', 'Uic-Token': token}

        with open(COOKIE_PATH, 'rb') as fp:
            cookies = pickle.load(fp)
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'],cookie['value'])
        response = session.post(uri, params=payload,headers=headers)
        # ic(response.json())
        print(f'get {riskLevels[index]} observed data: {response}')
        print(f'from: {payload['start']}')
        print(f'to: {payload['end']}')

        data_json = json.dumps(response.json(), indent=4)
        # write data
        with open(raw_datapath, 'w') as file:
            file.write(data_json)
        # parsing data
        export_monitorData('observed monitoring',raw_datapath, filepath)
        index +=1
    