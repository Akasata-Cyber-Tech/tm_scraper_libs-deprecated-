from modules import dataGroups
from modules.exportData import export_json_monitors
from modules.pathData import COOKIE_PATH,SSH_AUTH_DATA_PATH, MONITORING_AUTH_LOGIN_SSH_DATA_PATH,SMB_LOGON_DATA_PATH,MONITORING_SMB_LOGON_DATA_PATH,RDP_LOGON_DATA_PATH,MONITORING_RDP_LOGON_DATA_PATH
from modules.fieldsData import fieldList 
from utils.monitors.monitoring_authLogin import monitors_authLogin
import pickle
from datetime import datetime
import pytz
import sys
import json
import requests
import time
from icecream import ic

def monitoring(token: str, keyword):
    url = "https://portal.sg.xdr.trendmicro.com/ui/ase/api/search_agg"
    search_uri = "https://portal.sg.xdr.trendmicro.com/ui/ase/api/search"
    
    query = keyword
    headers = {'Content-type': 'application/json', 'Uic-Token': token}
    
    
    with open(COOKIE_PATH, 'rb') as fp:
        cookies = pickle.load(fp)
    logs_loop = 0
    nw = datetime.now()
    
    
    now = datetime.now()
    waktu_realtime = now.timestamp()
    waktu_inisialisasi = now.timestamp()
    waktu_end = waktu_inisialisasi + (1800)
    # generator using loops
    while(waktu_realtime < waktu_end):
        ses = nw.timestamp()
        ep = ses + (1800)
        if(ses == ep):
            sys.exit()
        # now = datetime.now()
        to_timestamp = now.timestamp()
        from_timestamp = to_timestamp - (3600*3)
        # from_timestamp = to_timestamp - (360)
        waktu = datetime.fromtimestamp(from_timestamp)
        list_time = [to_timestamp,from_timestamp]
        # Creating a new timezone
        utc_dt = datetime.now(pytz.utc)
        new_tz = pytz.timezone('Asia/Jakarta')
        waktu_now = utc_dt.astimezone(new_tz)
        qry_loops = 0
        dataSource = 2
        dataType = 2
        agg_fields = [fieldList.attacksFields,fieldList.malwareFields,fieldList.dnsFields]
        
        while(qry_loops <= 2):
            # print(query[qry_loops])
            # sys.exit()
            search = {
                # datasource general=2, datasource network =11 default is 2:2 
            "dataSource": dataSource,
            "dataType": dataType,
            "from": from_timestamp,
            "to": to_timestamp,
            "query": query[qry_loops],
            "searchType": 1,
            "filters": [],
            "aggFields": agg_fields[qry_loops]
        }
            json_data = json.dumps(search)
        
            session = requests.Session()
            for cookie in cookies:
                session.cookies.set(cookie['name'], cookie['value'])
    
            response = session.post(url, data=json_data, headers=headers)
            data_json = response.json()
            
            rex = []
            parsing = dataGroups.parsing
            
            # attacks monitoring generator 1
            if qry_loops == 0 :
                try:
                    # sys.exit(waktu_now)
                    # monitors_authLogin(token, query[0],"Exploit Attempts", ATTACKS_DATA_PATH, MONITORING_ATTACKS_DATA_PATH,"general")  
                    dataSource = 2
                    dataType = 2
                    type = "attacks"
                    dataGroups.return_arrayData(data_json, type)
                    source = dataGroups.Data.http_attacks_source
                    print(dataGroups.Data.http_attacks_source)
                    source_count = dataGroups.Data.http_attacks_source_count
                    rulename = dataGroups.Data.http_attacks_rulename
                    rulename_count = dataGroups.Data.http_attacks_rulename_count
                    request = dataGroups.Data.http_attacks_indicators
                    request_count = dataGroups.Data.http_attacks_indicators_count
                    destination = dataGroups.Data.http_attacks_destination
                    destination_count = dataGroups.Data.http_attacks_destination_count

                    # srcx = [rule['key'] for rule in data_json['data']['group'][2]]
                    parsing.print_waktu(str(waktu_now),rex)
                    # parsing.append_datav2('src',source,source_count,rulename,rulename_count,request,request_count,rex)
                    parsing.append_data('src',source, source_count,rex)
                    parsing.append_data('rulename',rulename, rulename_count,rex)
                    parsing.append_data('requests',request, request_count,rex)

                    data_json = json.dumps(rex, indent=4)
                    # ic(data_json)

                    export_json_monitors(data_json,type) 
                    # rex = []
                except Exception as err:
                    type = "attacks"
                    export_json_monitors("No DATA Founds",type) 
                    print(f'{err} : Tidak Ada Serangan Yang Terdeteksi!')
                       
            # malware monitoring generator 2
            if qry_loops == 1 :
                try:
                    dataSource = 2
                    dataType = 2
                    type = "malware"
                    data = dataGroups.Data
                    dataGroups.return_arrayData(data_json, type)
                    dataGroups.parsing.print_waktu(str(waktu_now),rex)
                    endpointName = data.malware_detections_by_endpointName
                    endpoint_count = data.malware_detections_by_endpoint_count
                    filename = data.malware_detections_by_filename
                    print(data.malware_detections_by_filename)
                    filename_count = data.malware_detections_by_file_count
                    # srcx = [rule['key'] for rule in data_json['data']['group'][2]]
                    # rex = []
                    # parsing.print_endpointName(endpointName,endpoint_count,rex)
                    parsing.append_data('endpointName',endpointName,endpoint_count,rex)
                    parsing.append_data('filename',filename,filename_count,rex)
                    # parsing.print_filename(filename,filename_count,rex)
                    data_json = json.dumps(rex, indent=4)
                    export_json_monitors(data_json,type) 
                    rex = []
                except :
                    print(f': Tidak Ada Malware Terdeteksi!')
                    type = "malware"
                    data_json = response.json()
                    ic(data_json)
                    export_json_monitors("No DATA Founds",type) 

            # suspicious dns response monitoring 3
            if qry_loops == 2 :
                try:
                    dataSource = 2
                    dataType = 2
                    type = "sus_dns_response"
                    type_export = "suspicious_dns"
                    data = dataGroups.Data
                    #Eksekusi data fetching untuk suspicious dns response dari datagroup json
                    dataGroups.return_arrayData(data_json, type)
                    dataGroups.parsing.print_waktu(str(waktu_now), rex)
                    source = data.sus_dns_response_source
                    destination = data.sus_dns_response_destination
                    rulename = data.sus_dns_response_rulename
                    cccaDestination = data.sus_dns_response_indicators
                    source_count = data.sus_dns_response_source_count
                    rulename_count = data.sus_dns_response_rulename_count
                    destination_count = data.sus_dns_response_destination_count
                    cccaDestination_count = data.sus_dns_response_indicators_count
                    
                    # parsing.append_data('src',source, source_count, rex)
                    # parsing.append_data('dst',destination, destination_count, rex)
                    # parsing.append_data('rulename',rulename, rulename_count, rex)
                    parsing.append_data('cccaDestination',cccaDestination, cccaDestination_count, rex)
                    data_json = json.dumps(rex, indent=4)
                    export_json_monitors(data_json, type_export)
                    # print()
                except Exception as err:
                    print(f'[ ERROR ] {err}')
                    type_export = "suspicious_dns"
                    data_json = response.json()
                    ic(data_json)
                    export_json_monitors("No DATA Founds", type_export)



            
            # ssh login auth monitoring 4
            monitors_authLogin(token, query[3],"SSH Authentications", SSH_AUTH_DATA_PATH, MONITORING_AUTH_LOGIN_SSH_DATA_PATH,"general",list_time)  
             
            # rdp login auth 5 
            # ic(query[4])
            monitors_authLogin(token, query[4], "RDP LOGONS", RDP_LOGON_DATA_PATH,MONITORING_RDP_LOGON_DATA_PATH,"general",list_time)  
            monitors_authLogin(token, query[5], "RDP LOGONS", SMB_LOGON_DATA_PATH,MONITORING_SMB_LOGON_DATA_PATH,"general",list_time)      
                
            
            # ic(query[5])
            # rdp login auth 6
            # monitors_authLogin(token, query[5], "RDP LOGONS", RDP_LOGON_DATA_PATH,MONITORING_RDP_LOGON_DATA_PATH,"general")      
            
            # suspicious monitoring generator
            
            # 
            # else:
            #     print('nanti lagi yaa....')
            qry_loops += 1
            print('tunggu 5 detik')
            time.sleep(1)

        # waktu_inisialisasi = waktu_realtime
        