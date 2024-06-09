from modules.pathData import *
import json

def generate_csv():
    # Malware CSV export
    with open(MALWARE_DATAGROUP_PATH, 'rb') as file:
        data = json.load(file)
        # file.read(f'{malware_csv_content}\n')
        endpointName = [req['key'] for req in data['data']['group'][0]['value']]
        endpoint_count = [req['count'] for req in data['data']['group'][0]['value']]
        filename = [req['key'] for req in data['data']['group'][2]['value']]
        filename_count = [req['count'] for req in data['data']['group'][2]['value']]
        
        
        loops_start = 0

        with open(CSV_MALWARE_DATAGROUP_BY_SOURCE, 'w') as file:
            file.write('endpointName,totalLogs\n')
            while(loops_start < len(endpointName)):
                file.write(f'{endpointName[loops_start]},{endpoint_count[loops_start]}\n')    
                loops_start += 1
        loops_start = 0
        with open(CSV_MALWARE_DATAGROUP_BY_INDICATOR, 'w') as file:
            file.write('filename,totalLogs\n')
            while(loops_start < len(filename)):
                file.write(f'{filename[loops_start]},{filename_count[loops_start]}\n')
                loops_start += 1
    
    # Suspicious DNS Respoonse By Indicator CSV
    
    with open(SUS_DNS_RESPONSE_DATAGROUP_PATH, 'rb') as file:
        data = json.load(file)
        cccaDestination = [req['key'] for req in data['data']['group'][3]['value']]
        cccaDestination_count = [req['count'] for req in data['data']['group'][3]['value']]
        
        loops = 0
        with open(CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_INDICATOR, 'w') as file_data:
            file_data.write('cccaDestination,totalLogs\n')
            while(loops < len(cccaDestination)):
                file_data.write(f'{cccaDestination[loops]},{cccaDestination_count[loops]}\n')
                loops +=1
    
    # attacks_filepath = ATTACKS_DATAGROUP_PATH
    file_to_convert = [ATTACKS_DATAGROUP_PATH,SUS_DNS_RESPONSE_DATAGROUP_PATH]
    csv_filepath_by_source = [CSV_ATTACKS_DATAGROUP_BY_SOURCE,CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_SOURCE]
    csv_filepath_by_rulename = [CSV_ATTACKS_DATAGROUP_BY_RULENAME,CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_RULENAME]        
    csv_content = []
    # append csv content
    loop_start = 0
    while(loop_start < len(file_to_convert)):
        with open(file_to_convert[loop_start], 'rb') as file_data:
            data = json.load(file_data)
            
            sourceIP = [source['key'] for source in data['data']['group'][0]['value']]
            count_sourceIP = [count_source['count'] for count_source in data['data']['group'][0]['value']]
            
            ruleName = [rulename['key'] for rulename in data['data']['group'][2]['value']]
            count_ruleName = [count_rulename['count'] for count_rulename in data['data']['group'][2]['value']]
            
            
            append_loop_start = 0
            csv_content.append('IP,totalLogs')    
            while(append_loop_start < len(sourceIP)):
                csv_content.append(f"{sourceIP[append_loop_start]},{count_sourceIP[append_loop_start]}")
                append_loop_start += 1
            try:
                with open(csv_filepath_by_source[loop_start], 'w') as file:
                    for content in csv_content:
                        file.write(f"{content}\n")
                    print(f"File '{csv_filepath_by_source[loop_start]}' created successfully.")
            except Exception as error:
                print(error)     
            csv_content = []
            csv_content.append('ruleName,totalLogs')    
            append_loop_start = 0
            while(append_loop_start < len(ruleName)):
                csv_content.append(f"{ruleName[append_loop_start]},{count_ruleName[append_loop_start]}")
                append_loop_start += 1
            try:
                with open(csv_filepath_by_rulename[loop_start], 'w') as file:
                    for content in csv_content:
                        file.write(f"{content}\n")
                    print(f"File '{csv_filepath_by_rulename[loop_start]}' created successfully.")
            except Exception as error:
                print(error)     
            csv_content = []
            loop_start += 1