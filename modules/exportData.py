
from modules.pathData import *

def create_and_fill_file(file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{file_path}' created successfully.")
        except Exception as e:
            print(f"Error creating the file: {e}")
    # create_and_fill_file(file_path, file_content)
    
def export_json_monitors(data, type:str):
    # Example usage:
    if type == "malware":
        file_path = MONITORING_MALWARE_DATA_PATH
    if type == "attacks":
        file_path = MONITORING_ATTACKS_DATA_PATH
    if type == "suspicious_dns":
        file_path = MONITORING_SUS_DNS_RESPONSE_DATA_PATH
    if type == "behavior_violation":
        file_path = MONITORING_SUS_BEHAVIOR_DATA_PATH
    if type == "rdp_ddi_login":
        file_path = MONITORING_RDP_DDI_DATA_PATH
    if type == "rdp_login":
        file_path = MONITORING_RDP_LOGON_DATA_PATH
    file_content = data
    print('exporting...')
    create_and_fill_file(file_path, file_content)
    
def export_json_search(data, type:str):
	# Example usage:
    if type == "malware":
        file_paths = MALWARE_DATA_PATH
        print(f'{file_paths}')
    if type == "attacks":
        file_paths = ATTACKS_DATA_PATH
        print(f'{file_paths}')

    if type == "suspicious_dns":
        file_paths = SUS_DNS_RESPONSE_DATA_PATH
        print(f'{file_paths}')

    if type == "behavior_violation":
        file_paths = SUS_BEHAVIOR_DATA_PATH
        print(f'{file_paths}')

    file_content = data
    def create_and_fill_file(file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{file_path}' created successfully.")
        except Exception as e:
            print(f"Error creating the file: {e}")
    create_and_fill_file(file_path=file_paths, content=file_content)

def export_json_data_groups(data, type:str):
   def create_file(file_path):
       file_content = data
       def create_and_fill_file(file_path, content):
           try:
               with open(file_path, 'w') as file:
                   file.write(content)
               print(f"File '{file_path}' created successfully.")
           except Exception as e:
               print(f"Error creating the file: {e}")
       create_and_fill_file(file_path, file_content)
# Example usage:
   if type == "malware":
       file_path = MALWARE_DATAGROUP_PATH
       create_file(file_path)
   if type == "attacks":
       file_path = ATTACKS_DATAGROUP_PATH
       create_file(file_path)
   if type == "suspicious_dns":
       file_path = SUS_DNS_RESPONSE_DATAGROUP_PATH
       create_file(file_path)
   if type == "behavior_violation":
       file_path = SUS_BEHAVIOR_DATAGROUP_PATH
       create_file(file_path)
   # else:
   #     print("kesalahan")

