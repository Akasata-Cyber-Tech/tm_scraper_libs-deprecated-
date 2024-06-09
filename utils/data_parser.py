from modules.requirements_modulees import *
from modules.custom_modules_import import *
import_base_modules()
import_custom_modules()
def json_editor():
    def group_parser(fileName, rawfileName,group,supabase_filename):
        # rawfileName adalah datagroup raw yang belum di parsing
        # ambil count/summary dari looping rawFilename 
        def get_id_and_totalLogs(rawfileName):
            with open(rawfileName, 'r') as rawfile:
                        data = json.load(rawfile)
                        totalLogs = [count['count'] for count in data['data']['group'][0]['value']]
                        element_rawfile = len(totalLogs)
                        count_start_from = 1
                        print(' total source IP :',element_rawfile)
                        print('total Logs :',sum(totalLogs))
                        id =[]
                        while(count_start_from < element_rawfile +1):
                            id.append(count_start_from)
                            # print('ID :',element_rawfile -1,'total Logs :',logs)
                            count_start_from += 1
                            # return logs
                        print(id)
                        return id
        try:
            with open(rawfileName, 'r') as file:
                data = json.load(file)
                totalLogs = [count['key'] for count in data['data']['group'][0]['value']]
                count_start_from = 1
                id =[]
                while(count_start_from < len(totalLogs) +1):
                    id.append(count_start_from)
                    count_start_from += 1
                
                if group == 'attacks' or 'dns':
                    dest = [item['key'] for item in data['data']['group'][1]['value']]
                    dest_count = [item['count'] for item in data['data']['group'][1]['value']]
                    rulename= [item['key'] for item in data['data']['group'][2]['value']]
                    rulename_count= [item['count'] for item in data['data']['group'][2]['value']]
                    req = [item['key'] for item in data['data']['group'][3]['value']]
                    source = [item['key'] for item in data['data']['group'][0]['value']]
                    source_count = [item['count'] for item in data['data']['group'][0]['value']]
                    sourceIP = source
                    destinationIP = dest
                    ruleName = rulename
                    result = {'ID': id,'src': sourceIP,'dst': destinationIP,'ruleName': ruleName,'requests': req}
                    supabase_result = {'ID': id,'key': sourceIP,'count':source_count}
                if group == 'malware':
                    files = [item['key'] for item in data['data']['group'][2]['value']]
                    hostname = [item['key'] for item in data['data']['group'][0]['value']]
                    count_endpoint = [item['count'] for item in data['data']['group'][0]['value']]
                    endpoint = hostname
                    file = files
                    result = {'endpointHostName': endpoint,'fileName':file}
                    supabase_result = {'ID': id,'key': endpoint,'count':count_endpoint}


                # print(result)
            file_path = fileName
            file_content = json.dumps(result, indent=4)
            supabase_content = json.dumps(supabase_result, indent=4)
            def create_and_fill_file(file_path, content):
                try:
                    with open(file_path, 'w') as file:
                        file.write(content)
                    print(f"\n [ SUCESS ] File '{file_path}' created successfully.")
                except Exception as e:
                    print(f"Error creating the file: {e}")
            def create_database_file(supabase_filename, content):
                try:
                    with open(supabase_filename, 'w') as file:
                        file.write(content)
                        print(f"\n [ SUCESS ] File '{supabase_filename}' created successfully.")
                        
                except Exception as err:
                    print(err)
            create_and_fill_file(file_path, file_content)
            create_database_file(supabase_filename, supabase_content)
        except Exception as error:
            print('\n','[ ERROR ]',rawfileName,' For Group ',group,' Cannot Parsed Because ',error,' [ A.K.A ] Data Not Found','\n')
            with open(fileName , 'w') as nowrite:
                nowrite.write('{"data": "No Data"}')

    def attacks_datagroup_parser():
        supabase_filename = SUPABASE_ATTACKS_DATAGROUP_PATH
        fileName = ATTACKS_DATAGROUP_PARSED_PATH
        rawfileName = ATTACKS_DATAGROUP_PATH
        group = "attacks"
        group_parser(fileName, rawfileName, group, supabase_filename)
    def suspicious_dns_datagroup_parser():
        supabase_filename = SUPABASE_SUS_DNS_RESPONSE_DATAGROUP_PATH
        fileName = SUS_DNS_RESPONSE_DATAGROUP_PARSED_PATH
        rawfileName = SUS_DNS_RESPONSE_DATAGROUP_PATH
        group = "dns"
        group_parser(fileName, rawfileName, group, supabase_filename)
    def malware_datagroup_parser():
        supabase_filename = SUPABASE_MALWARE_DATAGROUP_PATH
        fileName = MALWARE_DATAGROUP_PARSED_PATH
        rawfileName = MALWARE_DATAGROUP_PATH
        group = "malware"
        group_parser(fileName, rawfileName, group, supabase_filename)
    def behavior_datagroup_parser():
        supabase_filename = SUPABASE_SUS_BEHAVIOR_DATAGROUP_PATH
        fileName = SUS_BEHAVIOR_DATAGROUP_PARSED_PATH
        rawfileName = SUS_BEHAVIOR_DATAGROUP_PATH
        group = "behavior"
        group_parser(fileName, rawfileName, group, supabase_filename)
        
    def custom_csv_parser():
        csv_data = str
        return csv_data

    attacks_datagroup_parser()
    suspicious_dns_datagroup_parser()
    malware_datagroup_parser()
    behavior_datagroup_parser()
