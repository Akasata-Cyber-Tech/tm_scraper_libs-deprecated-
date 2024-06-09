import requests
from modules.pathData import *
import pickle
import json
import modules.dataGroups as dataGroups
from datetime import datetime
from icecream import ic
import os
import sys
from hashlib import sha256

def hash(object: str):
    buffer = object.encode('utf-8')
    return sha256(buffer).hexdigest()
    # print(hash_data)
    # return hashed_str

exampleMonitoringData ={
        "endpointHostName": "svrlporadb52.sub11240637381.proddb01.oraclevcn.com",
        "shost": "svrlporadb52",
        "dhost": "",
        "remarks": "(to root) root on none",
        "eventDataIpAddress": "",
        "endpointIP": [
            "10.122.1.88"
        ]
    }


def get_req(uri: str,payload, token: str, filepath,label:str):
        url = uri
        headers = {'Content-type': 'application/json', 'Uic-Token': token}
        
        
        with open(COOKIE_PATH, 'rb') as fp:
            cookies = pickle.load(fp)
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
        response = session.post(url, data=json.dumps(payload), headers=headers)
        print(f'{label}:{response}')
        data_json = json.dumps(response.json(), indent=4)
        with open(filepath, 'w') as file:
            file.write(str(data_json))
            

def export_monitorData(label: str,dataPath, monitorDataPath,):
        with open(dataPath, 'rb') as file:
            files_data = json.load(file)
            index = 0
            list_result = []
            temp_data = []
            def hash_isAdded(hash: str):
                return hash in [data['dataHash'] for data in temp_data]
                    # return isAdded
            
            def data_loops(index: int, isTemp:True):
                while(index < len(files_data['data']['logs'])):
                        try:
                            data = files_data['data']['logs'][index]['remarks']['value']
                        except:
                            data= ""

                        try:
                            shost = files_data['data']['logs'][index]['shost']['value']
                        except:
                            shost= ""

                        try:
                            dhost = files_data['data']['logs'][index]['dhost']['value']
                        except:
                            dhost = ""

                        try:
                            rawDataStr = files_data['data']['logs'][index]['rawDataStr']['value']
                        except:
                            rawDataStr =""

                        try:
                            endpointIp = files_data['data']['logs'][index]['endpointIp']['value']
                        except:
                            endpointIp = ""

                        try:
                            eventDataIpAddress = files_data['data']['logs'][index]['eventDataIpAddress']['value']
                        except:
                            eventDataIpAddress = ""

                        try:
                            endpointHostName = files_data['data']['logs'][index]['endpointHostName']['value']
                        except:
                            endpointHostName = ""

                        data_hash = {'endpointHostName':endpointHostName,'shost': shost,'dhost': dhost,'remarks':data,'eventDataIpAddress':eventDataIpAddress,'endpointIP':endpointIp, "dataHash": ""}
                        uniqueID = hash_and_grouping(data_hash)
                        result = {'endpointHostName':endpointHostName,'shost': shost,'dhost': dhost,'remarks':data,'eventDataIpAddress':eventDataIpAddress,'endpointIP':endpointIp, "dataHash": uniqueID}
                        if isTemp:
                            temp_data.append(result)
                        else:
                            isAdded = hash_isAdded(uniqueID)
                            try:
                                if not isAdded:
                                    # print(isAdded)
                                    # sys.exit()
                                    # isAdded = True
                                    result = {'endpointHostName':endpointHostName,'shost': shost,'dhost': dhost,'remarks':data,'eventDataIpAddress':eventDataIpAddress,'endpointIP':endpointIp, "dataHash": uniqueID}
                                    list_result.append(result)
                                    print(f'{result['dataHash']} is sucessfully added')
                            except Exception as e:
                                sys.exit(e)
                                
                        
                        index +=1
                        
                        # temp_data.append(data_hash)
                       
                        
            try: 
                data_loops(index =0,isTemp=True)
                print("add temporary")
            except Exception as err:
                 print(f'[ ERROR ] {err}')
                 
            try:
                data_loops(index =0,isTemp=False)
                print("add data")
                
                
            except Exception as err:
                 print(f'[ ERROR ] {err}')
            
            
            content = json.dumps(list_result, indent=4)
            with open(monitorDataPath, 'w') as file:
                file.write(content)
            # sys.exit()

            # with open(monitorDataPath, 'rb') as writedContent:
            #     data = json.load(writedContent)
            #     IDs = 1
            #     for dt in data:
            #         print(f'{IDs} -> {hash_and_grouping(dt)}')
            #         dataHash = (f'{IDs} -> {hash_and_grouping(dt)}')
            #         IDs += 1
            #     def databaseUpdate():
            #         exData = {
            #             "endpointHostName": "svrlporadb52.sub11240637381.proddb01.oraclevcn.com",
            #             "shost": "svrlporadb52",
            #             "dhost": "",
            #             "remarks": "(to root) root on none",
            #             "eventDataIpAddress": "",
            #             "endpointIP": [
            #                 "10.122.1.88"
            #             ],
            #             "dataHash": ""
            #         }
            #         if dataHash != exData['dataHash']:
            #             print("")



def hash_and_grouping(data):
    # print(sha256(b'10.10.10.10').hexdigest())
    dt = data
    data_to_hash = [dt['shost'],dt['dhost'],dt['endpointIP'],dt['remarks']]
    # hash("10.10.10.10")
    hash_data = hash(str(data_to_hash))
    # IDs = 1
    return hash_data
    

def monitors_authLogin(token: str, qry: str, label,dataPath, monitorDataPath, searchType):
    query = qry
    url = "https://portal.sg.xdr.trendmicro.com/ui/ase/api/search"
    now = datetime.now()
    to_timestamp = now.timestamp()
    from_timestamp = to_timestamp - (3600*3)
    dataSource= 0
    dataType= 0
    if searchType == "general":
        dataSource= 0
        dataType= 0
        srchType= 0
    if searchType == "detections":
        dataSource= 2
        srchType= 1
        dataType= 2
    search = {
            # datasource general=2, datasource network =11default is 2:2
        
        "dataSource": dataSource,
        "dataType": dataType,
        "filters": [],
        "from": int(from_timestamp),
        "query": query,
        "searchType": srchType,
        "to": int(to_timestamp)
        }
    post_data = json.dumps(search)
    # dataPath = SSH_AUTH_DATA_PATH
    # monitorDataPath = MONITORING_AUTH_LOGIN_SSH_DATA_PATH
    
    get_req(url,search,token, dataPath,label=label)
    export_monitorData(label ,dataPath, monitorDataPath)
    
    
            
def monitors_rdpLogin(token: str, qry):
    query = qry
    url = "https://portal.sg.xdr.trendmicro.com/ui/ase/api/search"
    now = datetime.now()
    to_timestamp = now.timestamp()
    from_timestamp = to_timestamp - (3600*12)
    search = {
            # datasource general=2, datasource network =11default is 2:2 
        "dataSource": 0,
        "dataType": 0,
        "from": from_timestamp,
        "to": to_timestamp,
        "query": query,
        "searchType": 1,
        "filters": [],}
    post_data = json.dumps(search)
    filepath = SSH_AUTH_DATA_PATH
    
    get_req(url,post_data,token, filepath)
    
    