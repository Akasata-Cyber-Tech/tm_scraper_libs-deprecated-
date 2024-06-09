from modules.pathData import *
import json
from typing import Literal



class Data:
    
    http_attacks_source = list[str]
    http_attacks_source_count = list[int]
    http_attacks_destination = list[str]
    http_attacks_destination_count = list[int]
    http_attacks_indicators = list[str]
    http_attacks_indicators_count = list[int]
    http_attacks_rulename = list[str]
    http_attacks_rulename_count = list[int]
    
    sus_dns_response_source = list[str]
    sus_dns_response_source_count = list[int]
    sus_dns_response_destination = list[str]
    sus_dns_response_destination_count = list[int]
    sus_dns_response_indicators = list[str]
    sus_dns_response_indicators_count = list[int]
    sus_dns_response_rulename = list[str]
    sus_dns_response_rulename_count = list[int]
    
    malware_detections_by_endpointName = list[str]
    malware_detections_by_endpoint_count = list[str]
    malware_detections_by_filename = list[str]
    malware_detections_by_fiepathName = list[str]
    malware_detections_by_fiepath_count = list[str]
    malware_detections_by_file_count = list[int]
    

def return_arrayData(data_json: dict, group: Literal['attacks', 'malware', 'RDP', 'sus_dns_response', 'ssh_auth_login', 'sus_dns_request', 'threat']):
    # data_json = json.load(path)
    # group attacks via http
    if(group=="attacks"):
        try:
            source = [src['key'] for src in data_json['data']['group'][0]['value']]
            source_count = [src['count'] for src in data_json['data']['group'][0]['value']]
            destination = [dest['key'] for dest in data_json['data']['group'][1]['value']]
            destination_count = [dest['count'] for dest in data_json['data']['group'][1]['value']]
            rulename = [rule['key'] for rule in data_json['data']['group'][2]['value']]
            rulename_count = [rule['count'] for rule in data_json['data']['group'][2]['value']]
            request = [req['key'] for req in data_json['data']['group'][3]['value']]
            request_count = [req['count'] for req in data_json['data']['group'][3]['value']]
            Data.http_attacks_source = source
            Data.http_attacks_source_count = source_count
            Data.http_attacks_destination = destination
            Data.http_attacks_destination_count = destination_count
            Data.http_attacks_indicators = request
            Data.http_attacks_indicators_count = request_count
            Data.http_attacks_rulename = rulename
            Data.http_attacks_rulename_count = rulename_count
        except Exception as err:
            print(f'{err} : No Data Founds!')
        
        # pass
    # group malware deetections
    if(group=="malware"):
        try:
            endpointName = [req['key'] for req in data_json['data']['group'][0]['value']]
            endpoint_count = [req['count'] for req in data_json['data']['group'][0]['value']]
            filename = [req['key'] for req in data_json['data']['group'][2]['value']]
            filename_count = [req['count'] for req in data_json['data']['group'][2]['value']]
            Data.malware_detections_by_endpointName = endpointName
            Data.malware_detections_by_endpoint_count = endpoint_count
            Data.malware_detections_by_filename = filename
            Data.malware_detections_by_file_count = filename_count
        except Exception as err:
            print(f'{err} : No Data Founds!')
    
    if(group=="ssh_auth_login"):
        try:
            index = 0
            
            while(index < len(data_json['data']['logs'])):
                list_remarks = []
                list_shost = []
                list_dhost = []
                remarks = data_json['data']['logs'][index]['remarks']['value']
                # destination = "s"  
                shost = data_json['data']['logs'][index]['shost']
                dhost = data_json['data']['logs'][index]['dhost']
                list_remarks.append(remarks)
                list_dhost.append(dhost)
                list_shost.append(shost)
                auth_data_json = {'shost': list_shost, 'dhost': list_dhost, 'remarks': list_remarks}
                index +=1
        except Exception as err:
            print(f'[ ERROR ] {err}')
    
    # group suspicious dns response connections
    if(group=="sus_dns_response"):
        try:
            source = [req['key'] for req in data_json['data']['group'][0]['value']]
            destination = [req['key'] for req in data_json['data']['group'][1]['value']]
            rulename = [req['key'] for req in data_json['data']['group'][2]['value']]
            hostname = [req['key'] for req in data_json['data']['group'][3]['value']]
            source_count = [req['count'] for req in data_json['data']['group'][0]['value']]
            destination_count = [req['count'] for req in data_json['data']['group'][1]['value']]
            rulename_count = [req['count'] for req in data_json['data']['group'][2]['value']]
            hostname_count = [req['count'] for req in data_json['data']['group'][3]['value']]
            Data.sus_dns_response_source = source
            Data.sus_dns_response_destination = destination
            Data.sus_dns_response_indicators = hostname
            Data.sus_dns_response_indicators_count = hostname_count
            Data.sus_dns_response_rulename = rulename
            Data.sus_dns_response_rulename_count = rulename_count
            Data.sus_dns_response_destination_count = destination_count
            Data.sus_dns_response_source_count = source_count
            
        except Exception as err:
            print(f'[ ERRPR ] {err}')
            
    # group rdp connection via ddi
    if(group=="RDP"):
        try:
            endpointIp= ''
        except Exception as err:
            print(f'{err} : No Data Founds')
    
    # group rdp connection via log
    
    


class parsing:
    def print_waktu(waktu: str,rex:list):
        rex.append({'time':str(waktu)})
        
    def append_datav2(type: str,data1: list[str],data1_count: list[int],data2: list[str],data2_count: list[int], data3: list[str], data3_count: list[int], rex:list):
        loops = 0
        while(loops < len(data1)):
            # rex.append({type:data1[loops],'src_count':data1_count[loops],'rulename':data2[loops],'rulename_cnt':data2_count[loops],'req':data3[loops],'req_cnt':data3_count[loops]})
            
            rex.append({data1[loops]:data1_count[loops],data2[loops]:data2_count[loops],data3[loops]:data3_count[loops]})
            loops +=1
    def append_data(type: str,data: list[str],data_count:list[int], rex:list):
        loops = 0
        while(loops < len(data)):
            rex.append({type:data[loops],'count':data_count[loops]})
            # rex.append({'src':source[loops],'count':source_count[loops]})
            # hsl = rex
            # print(hsl)
            
            loops +=1
    def print_sources(source: list,source_count: list,rex:list):
        loops = 0
        while(loops < len(source)):
            rex.append({'src':source[loops],'count':source_count[loops]})
            # rex.append({'src':source[loops],'count':source_count[loops]})
            # hsl = rex
            # print(hsl)
            
            loops +=1
    def print_rulename(rulename: list,rulename_count: list,rex:list):
        loops = 0
        while(loops < len(rulename)):
            rex.append({rulename[loops]:rulename_count[loops]})
            # rulename[loops]:rulename_count[loops]
            loops +=1
    def print_request(request: list, request_count: list, rex:list):
        loops = 0
        while(loops < len(request)):
            rex.append({request[loops]:request_count[loops]})
            # rulename[loops]:rulename_count[loops]
            loops +=1
    def print_endpointName(endpointName: list,endpoint_count: list, rex:list):
        loops = 0
        while(loops < len(endpointName)):
            rex.append({'endpointName':endpointName[loops],'count':endpoint_count[loops]})
            # rulename[loops]:rulename_count[loops]
            loops +=1
    def print_filename(filename: list, filename_count: list, rex:list):
        loops = 0
        while(loops < len(filename)):
            rex.append({'filename':filename[loops],'count':filename_count[loops]})
            # rulename[loops]:rulename_count[loops]
            loops +=1
            loops +=1
            
    def print_destination(destination: list, destination_count:list, rex:list):
        loops = 0
        while(loops < len(destination)):
            rex.append({destination[loops]:destination_count[loops]})
            # rulename[loops]:rulename_count[loops]
            loops +=1
    def print_remarks(remarks: list, remarks_count:list, rex:list):
        loops = 0
        while(loops < len(remarks)):
            rex.append({remarks[loops]:remarks_count[loops]})
            # rulename[loops]:rulename_count[loops]
            loops +=1