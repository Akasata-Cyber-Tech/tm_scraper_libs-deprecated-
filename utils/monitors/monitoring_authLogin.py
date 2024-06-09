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
                
            def data_loops(index, isTemp:True):
                try:
                    lpd_data = len(files_data['data']['logs'])
                    observedData = False
                except:
                    lpd_data = len(files_data['data']['detections'])
                    observedData = True
                while(index < lpd_data):
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
                            dhost = None

                        try:
                            rawDataStr = files_data['data']['logs'][index]['rawDataStr']['value']
                        except:
                            rawDataStr = None

                        try:
                            endpointIp = files_data['data']['logs'][index]['endpointIp']['value']
                        except:
                            endpointIp = None

                        try:
                            eventDataIpAddress = files_data['data']['logs'][index]['eventDataIpAddress']['value']
                        except:
                            eventDataIpAddress = None

                        try:
                            endpointHostName = files_data['data']['logs'][index]['endpointHostName']['value']
                        except:
                            endpointHostName = None
                            
                        # Check If Its come from observed monitoring data
                        try:
                            detection_name = files_data['data']['detections'][index]['name']
                        except:
                            detection_name = None
                        try:
                            shost = files_data['data']['detections'][index]['raw_log']['shost']                        
                        except:
                            shost = None
                        try:
                            dst_attack = files_data['data']['detections'][index]['raw_log']['dst']
                        except:
                            dst_attack = None
                        try:
                            dhost = files_data['data']['detections'][index]['raw_log']['dhost']
                        except:
                            dhost = None
                        try:
                            request = files_data['data']['detections'][index]['raw_log']['request']
                        except: 
                            request = None
                        try:
                            src_attack = files_data['data']['detections'][index]['raw_log']['src']                            
                        except:
                            src_attack = None
                        try:
                            endpoint = files_data['data']['detections'][index]['endpoint']['name']                            
                        except:
                            endpoint = None
                        try:
                            description = files_data['data']['detections'][index]['description']                            
                        except:
                            description = None
                        try:
                            severity_level = files_data['data']['detections'][index]['level']                            
                        except:    
                            severity_level = None
                        try:
                            rulename = files_data['data']['detections'][index]['raw_log']['rulename']
                        except:
                            rulename = None
                        try:
                            app = files_data['data']['detections'][index]['raw_log']['app']
                        except:
                            app = None
                        try:
                            botUrl = files_data['data']['detections'][index]['raw_log']['botUrl']
                        except:
                            botUrl = None
                        try:
                            userAgent = files_data['data']['detections'][index]['raw_log']['requestClientApplication']
                        except:
                            userAgent = None
                        try:
                            pAttackPhase = files_data['data']['detections'][index]['raw_log']['pAttackPhase']
                        except:
                            pAttackPhase = None
                        try:
                            remarks = files_data['data']['detections'][index]['raw_log']['remarks']
                        except: 
                            remarks = None
                        try:
                            uuid = files_data['data']['detections'][index]['raw_log']['uuid']
                        except:
                            uuid = None
                        try:
                            detected_by = files_data['data']['detections'][index]['raw_log']['pname']
                        except:
                            detected_by = None
                            
                        try:
                            objectCmd = files_data['data']['detections'][index]['raw_log']['objectCmd']
                        except:
                            objectCmd = None
                        try:
                            data_hash = {'endpointHostName':endpointHostName,'shost': shost,'dhost': dhost,'remarks':data,'eventDataIpAddress':eventDataIpAddress,'endpointIP':endpointIp, "dataHash": ""}
                            uniqueID = hash_and_grouping(data_hash)
                        except:
                            data_hash = {'detection_name':detection_name,'severity_level': severity_level,'description': description,'endpoint':endpoint,'src_attack':src_attack,
                                              'shost':shost,
                                              'dst_attack':dst_attack ,
                                              'dhost':dhost ,
                                              'request': request,
                                              'rulename': rulename,
                                              'app':app ,
                                              'botUrl':botUrl ,
                                              'userAgent':userAgent ,
                                              'pAttackPhase':pAttackPhase ,
                                              'remarks':remarks ,
                                              'objectCmd': objectCmd,
                                              'detected_by': detected_by,
                                              'uuid':uuid,
                                              "dataHash": ""}
                            uniqueID = hash_and_grouping(data_hash)
                            
                        # result = {'endpointHostName':endpointHostName,'shost': shost,'dhost': dhost,'remarks':data,'eventDataIpAddress':eventDataIpAddress,'endpointIP':endpointIp, "dataHash": uniqueID}
                        if isTemp:
                            temp_data.append(data_hash)
                            
                        else:
                            isAdded = hash_isAdded(uniqueID)
                            # print(str(isAdded))
                            if not isAdded:
                                # print(isAdded)
                                # sys.exit()
                                # isAdded = True
                                if not observedData:
                                    result = {'endpointHostName':endpointHostName,'shost': shost,'dhost': dhost,'remarks':data,'eventDataIpAddress':eventDataIpAddress,'endpointIP':endpointIp, "dataHash": uniqueID}
                                    temp_data.append(result)
                                    list_result.append(result)
                                else:
                                    result = {'detection_name':detection_name,'severity_level': severity_level,'description': description,'endpoint':endpoint,'src_attack':src_attack,
                                              'shost':shost,
                                              'dst_attack':dst_attack ,
                                              'dhost':dhost ,
                                              'request': request,
                                              'rulename': rulename,
                                              'app':app ,
                                              'botUrl':botUrl ,
                                              'userAgent':userAgent ,
                                              'pAttackPhase':pAttackPhase ,
                                              'remarks':remarks ,
                                              'objectCmd': objectCmd,
                                              'detected_by': detected_by,
                                              'uuid':uuid ,
                                              "dataHash": uniqueID}
                                    temp_data.append(result)
                                    list_result.append(result)
                                    
                                # isAdded = hash_isAdded(uniqueID)
                                
                                # if not isAdded:
                                #     sys.exit("duplicated")
                                # print(f'{result['dataHash']} is sucessfully added')
                                
                        index +=1
                        
                        # temp_data.append(data_hash)
                       
            
                        
            try: 
                print("add temporary")
                data_loops(index=index,isTemp=True)
                tmp = json.dumps(temp_data, indent=4)
                # ic(tmp)
                # print(str(temp_data))
                print(f'raw data count {len(files_data['data']['logs'])}')
                print(f'temp data count {len(tmp)}')
            except Exception as err:
                 print(f'[ ERROR ] {err}')
                 
            try:
                # try:
                #     isAdded = hash_isAdded(uniqueID)
                #     print(str(isAdded))
                #     # if not isAdded:
                #     #     # print(isAdded)
                #     #     # sys.exit()
                #     #     # isAdded = True
                #     #     result = {'endpointHostName':endpointHostName,'shost': shost,'dhost': dhost,'remarks':data,'eventDataIpAddress':eventDataIpAddress,'endpointIP':endpointIp, "dataHash": uniqueID}
                #     #     list_result.append(result)
                #     #     print(f'{result['dataHash']} is sucessfully added')
                # except Exception as e:
                #     sys.exit(e)
                print("add data")
                # list_result.append(data_loops(index=index,isTemp=False))
                data_loops(index=index,isTemp=False)
                res = json.dumps(list_result, indent=4)
                print(f'result data count {len(list_result)}')
                # print(f'result data count {str(list_result)}')
                # ic(list_result)
                with open(monitorDataPath, 'w') as file:
                    file.write(res)

                
                
            except Exception as err:
                 print(f'[ ERROR ] {err}')
            
            
            # content = json.dumps(list_result, indent=4)
            # with open(monitorDataPath, 'w') as file:
            #     file.write(content)
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
    

def monitors_authLogin(token: str, qry: str, label,dataPath, monitorDataPath, searchType,list_time:list):
    query = qry
    url = "https://portal.sg.xdr.trendmicro.com/ui/ase/api/search"
    now = datetime.now()
    # to_timestamp = now.timestamp()
    to_timestamp = list_time[0]
    # from_timestamp = to_timestamp - (3600*48)
    from_timestamp = list_time[1]
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
    
    