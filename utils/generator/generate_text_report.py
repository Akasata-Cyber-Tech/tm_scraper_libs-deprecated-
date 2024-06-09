import os
import json
from modules.pathData import *

def generate_list_report(filepath):
    content = []
    index = 0
    while (index  != len(filepath) ):
        with open(filepath[index], 'r') as file:
            data = json.load(file)
            with open(REPORT_LIST_DATA_PATH, 'w') as file_result:
                def srcList():
                    try:
                        source = data['src']    
                        for sourceIP in source:
                            content.append(sourceIP)
                    except:
                        # source = ""
                        print('source not found')
                def endpointHostNameList():
                    try:
                        endpointHostName = data['endpointHostName']    
                        for endpointName in endpointHostName:
                            content.append(endpointName)
                    except:
                        # source = ""
                        print('endpointName not found')
                def fileNameList():
                    try:
                        fileName = data['fileName']    
                        for files in fileName:
                            content.append(files)
                    except:
                        # source = ""
                        print('fileName not found')
                def dstList():
                    try:
                        destination = data['dst']
                        for dstIP in destination:
                            content.append(dstIP)
                    except:
                        # destination = ""
                        print('destination not found')
                def rulenameList():
                    try:
                        rulename = data['ruleName']
                        for rules in rulename:
                            content.append(rules)
                    except:
                        # rulename = ""
                        print('rulename not found')
                def reqList():
                    try:
                        requests = data['requests']
                        for req in requests:
                            content.append(req)
                    except:
                        # requests = ""
                        print('requests not found')
                        
                        
                # class observedDaata:
                #     def src():
                #         print
                if filepath[index] == ATTACKS_DATAGROUP_PARSED_PATH:
                    content.append(f'ATTACKS DATA/Exploit Attemops')
                    
                    content.append(f'\n')
                    content.append(f'SourceIP Attacks\n')
                    srcList()
                    content.append(f'\n')
                    content.append(f'Destination IP\n')
                    dstList()
                    content.append(f'\n')
                    content.append(f'ruleNames\n')
                    rulenameList()
                    content.append(f'\n')
                    content.append(f'requests\n')
                    reqList()
                if filepath[index] == SUS_DNS_RESPONSE_DATAGROUP_PARSED_PATH:
                    content.append(f'Suspicious DNS Response')
                    content.append(f'\n')
                    content.append(f'SourceIP Attacks\n')
                    srcList()
                    content.append(f'\n')
                    content.append(f'Destination IP\n')
                    dstList()
                    content.append(f'\n')
                    content.append(f'ruleNames\n')
                    rulenameList()
                    content.append(f'\n')
                    content.append(f'requests\n')
                    reqList()

                if filepath[index] == MALWARE_DATAGROUP_PARSED_PATH:
                    content.append(f'Malware Reports')
                    content.append(f'\n')
                    content.append(f'endpointName')
                    content.append(f'\n')
                    endpointHostNameList()

                    content.append(f'\n')
                    content.append(f'fileNames')
                    content.append(f'\n')
                    fileNameList()
                for result in content:
                    file_result.write(f'{result}\n')
                    
            index += 1
            print(index)
            print(len(filepath))
    