import os 
from dotenv import load_dotenv

# CSV_DATA_PATH = os.getenv("")
# .env
#CSV_DATA_PATH=C:\Users\tegar\Documents\GitHub\ScraperProject\services\storage

load_dotenv()
BASE_PATH = os.getenv("BASE_PATH")
STORAGE_PATH = os.getenv("STORAGE_PATH")

BASE_PATH_DEF = os.path.dirname(os.path.realpath(__file__))
DRIVER_PATH = os.path.join(BASE_PATH, 'storage/drivers')
MODULES_PATH = os.path.join(BASE_PATH, 'storage/modules')
DATA_PATH = os.path.join(BASE_PATH, 'storage/data_path')
PARSED_DATA_PATH = os.path.join(BASE_PATH, 'storage/parsed_data_path')
CSV_DATA_PATH = os.path.join(STORAGE_PATH, 'csv_data_path')
SUPABASE_DATA_PATH = os.path.join(BASE_PATH, 'storage/supabase_data')
MONITORING_DATA_PATH = os.path.join(BASE_PATH, 'storage/monitoring_data')
# GECKO_DRIVER = os.path.join(DRIVER_PATH, 'geckodriver.exe')
GECKO_DRIVER = os.path.join(DRIVER_PATH, 'geckodriver')
CHROME_DRIVER = os.path.join(DRIVER_PATH, 'chromium.exe')
COOKIE_PATH = os.path.join(DRIVER_PATH, 'cookies.pkl')
# DATA_PATH = os.path.join(DRIVER_PATH, 'searchFormat.tm')
COOKIE2_PATH = os.path.join(DRIVER_PATH, 'cookies2.pkl')

# This is path for detailed data
SUS_BEHAVIOR_DATA_PATH = os.path.join(DATA_PATH, 'suspicious_behavior_data.json')
SUS_DNS_RESPONSE_DATA_PATH = os.path.join(DATA_PATH, 'suspicious_dns_response_data.json')
ATTACKS_DATA_PATH = os.path.join(DATA_PATH, 'attacks_data.json')
MALWARE_DATA_PATH = os.path.join(DATA_PATH, 'malware_data.json')
RDP_LOGON_DATA_PATH = os.path.join(DATA_PATH, 'rdp_logon_data.json')
SMB_LOGON_DATA_PATH = os.path.join(DATA_PATH, 'smb_logon_data.json')
SSH_AUTH_DATA_PATH = os.path.join(DATA_PATH, 'ssh_auth_data.json')
CRITICAL_OBSERVED_DATA_PATH = os.path.join(DATA_PATH, 'critical_observed_data.json')
HIGH_OBSERVED_DATA_PATH = os.path.join(DATA_PATH, 'high_observed_data.json')
MEDIUM_OBSERVED_DATA_PATH = os.path.join(DATA_PATH, 'medium_observed_data.json')
LOW_OBSERVED_DATA_PATH = os.path.join(DATA_PATH, 'low_observed_data.json')
INFO_OBSERVED_DATA_PATH = os.path.join(DATA_PATH, 'info_observed_data.json')

# This is path for grouped data

SUS_BEHAVIOR_DATAGROUP_PATH = os.path.join(DATA_PATH, 'suspicious_behavior_datagroup.json')
SUS_DNS_RESPONSE_DATAGROUP_PATH = os.path.join(DATA_PATH, 'suspicious_dns_response_datagroup.json')
ATTACKS_DATAGROUP_PATH = os.path.join(DATA_PATH, 'attacks_datagroup.json')
MALWARE_DATAGROUP_PATH = os.path.join(DATA_PATH, 'malware_datagroup.json')

# This is path for PARSED data

SUS_BEHAVIOR_DATAGROUP_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'suspicious_behavior_datagroup_parsed.json')
SUS_DNS_RESPONSE_DATAGROUP_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'suspicious_dns_response_datagroup_parsed.json')
ATTACKS_DATAGROUP_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'attacks_datagroup_parsed.json')
MALWARE_DATAGROUP_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'malware_datagroup_parsed.json')
CRITICAL_OBSERVED_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'critical_observed_data_parsed.json')
HIGH_OBSERVED_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'high_observed_data_parsed.json')
MEDIUM_OBSERVED_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'medium_observed_data_parsed.json')
LOW_OBSERVED_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'low_observed_data_parsed.json')
INFO_OBSERVED_PARSED_PATH = os.path.join(PARSED_DATA_PATH, 'info_observed_data_parsed.json')



# This is path for ready upload data to databases

SUPABASE_SUS_BEHAVIOR_DATAGROUP_PATH = os.path.join(SUPABASE_DATA_PATH, 'suspicious_behavior_datagroup.json')
SUPABASE_SUS_DNS_RESPONSE_DATAGROUP_PATH = os.path.join(SUPABASE_DATA_PATH, 'suspicious_dns_response_datagroup.json')
SUPABASE_ATTACKS_DATAGROUP_PATH = os.path.join(SUPABASE_DATA_PATH, 'attacks_datagroup.json')
SUPABASE_MALWARE_DATAGROUP_PATH = os.path.join(SUPABASE_DATA_PATH, 'malware_datagroup.json')
SUPABASE_CRITICAL_OBSERVED_DATA_PATH = os.path.join(PARSED_DATA_PATH, 'critical_observed_data.json')
SUPABASE_HIGH_OBSERVED_DATA_PATH = os.path.join(PARSED_DATA_PATH, 'high_observed_data.json')
SUPABASE_MEDIUM_OBSERVED_DATA_PATH = os.path.join(PARSED_DATA_PATH, 'medium_observed_data.json')
SUPABASE_LOW_OBSERVED_DATA_PATH = os.path.join(PARSED_DATA_PATH, 'low_observed_data.json')
SUPABASE_INFO_OBSERVED_DATA_PATH = os.path.join(PARSED_DATA_PATH, 'info_observed_data.json')

# This is path for ready upload data to databases

MONITORING_SUS_BEHAVIOR_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'suspicious_behavior_monitoring.json')
MONITORING_SUS_DNS_RESPONSE_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'suspicious_dns_response_monitoring.json')
MONITORING_ATTACKS_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'attacks_monitoring.json')
MONITORING_MALWARE_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'malware_monitoring.json')
MONITORING_RDP_DDI_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'rdp_ddi_monitoring.json')
MONITORING_RDP_LOGON_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'rdp_logon_monitoring.json')
MONITORING_SMB_LOGON_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'smb_logon_monitoring.json')
MONITORING_AUTH_LOGIN_SSH_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'ssh_auth_login_monitoring.json')
MONITORING_OBSERVED_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'observed_monitoring.json')
CRITICAL_MONITORING_OBSERVED_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'observed_monitoring_critical.json')
HIGH_MONITORING_OBSERVED_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'observed_monitoring_high.json')
MEDIUM_MONITORING_OBSERVED_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'observed_monitoring_medium.json')
LOW_MONITORING_OBSERVED_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'observed_monitoring_low.json')
INFO_MONITORING_OBSERVED_DATA_PATH = os.path.join(MONITORING_DATA_PATH, 'observed_monitoring_info.json')

# This is path for CSV documents

CSV_SUS_BEHAVIOR_DATAGROUP = os.path.join(CSV_DATA_PATH, 'suspicious_behavior_datagroup.csv')
CSV_SUS_DNS_RESPONSE_DATAGROUP = os.path.join(CSV_DATA_PATH, 'suspicious_dns_response_datagroup.csv')
CSV_ATTACKS_DATAGROUP = os.path.join(CSV_DATA_PATH, 'attacks_datagroup.csv')
CSV_MALWARE_DATAGROUP = os.path.join(CSV_DATA_PATH, 'malware_datagroup.csv')

# This is path for Partial CSV documents

CSV_SUS_BEHAVIOR_DATAGROUP_BY_SOURCE = os.path.join(CSV_DATA_PATH, 'suspicious_behavior_datagroup_BY_SOURCE.csv')
CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_SOURCE = os.path.join(CSV_DATA_PATH, 'suspicious_dns_response_datagroup_BY_SOURCE.csv')
CSV_ATTACKS_DATAGROUP_BY_SOURCE = os.path.join(CSV_DATA_PATH, 'attacks_datagroup_BY_SOURCE.csv')
CSV_MALWARE_DATAGROUP_BY_SOURCE = os.path.join(CSV_DATA_PATH, 'malware_datagroup_BY_SOURCE.csv')

# This is path for Partial CSV documents

CSV_SUS_BEHAVIOR_DATAGROUP_BY_RULENAME = os.path.join(CSV_DATA_PATH, 'suspicious_behavior_datagroup_BY_RULENAME.csv')
CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_RULENAME = os.path.join(CSV_DATA_PATH, 'suspicious_dns_response_datagroup_BY_RULENAME.csv')
CSV_ATTACKS_DATAGROUP_BY_RULENAME = os.path.join(CSV_DATA_PATH, 'attacks_datagroup_BY_RULENAME.csv')
CSV_MALWARE_DATAGROUP_BY_RULENAME = os.path.join(CSV_DATA_PATH, 'malware_datagroup_BY_RULENAME.csv')


# This is path for Partial CSV documents

CSV_SUS_BEHAVIOR_DATAGROUP_BY_INDICATOR = os.path.join(CSV_DATA_PATH, 'suspicious_behavior_datagroup_BY_INDICATOR.csv')
CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_INDICATOR = os.path.join(CSV_DATA_PATH, 'suspicious_dns_response_datagroup_BY_INDICATOR.csv')
CSV_ATTACKS_DATAGROUP_BY_INDICATOR = os.path.join(CSV_DATA_PATH, 'attacks_datagroup_BY_INDICATOR.csv')
CSV_MALWARE_DATAGROUP_BY_INDICATOR = os.path.join(CSV_DATA_PATH, 'malware_datagroup_BY_INDICATOR.csv')


# This is path for Partial CSV documents

CSV_SUS_BEHAVIOR_DATAGROUP_BY_DESTINATION = os.path.join(CSV_DATA_PATH, 'suspicious_behavior_datagroup_BY_DESTINATION.csv')
CSV_SUS_DNS_RESPONSE_DATAGROUP_BY_DESTINATION = os.path.join(CSV_DATA_PATH, 'suspicious_dns_response_datagroup_BY_DESTINATION.csv')
CSV_ATTACKS_DATAGROUP_BY_DESTINATION = os.path.join(CSV_DATA_PATH, 'attacks_datagroup_BY_DESTINATION.csv')
CSV_MALWARE_DATAGROUP_BY_DESTINATION = os.path.join(CSV_DATA_PATH, 'malware_datagroup_BY_DESTINATION.csv')

REPORT_LIST_DATA_PATH = os.path.join(PARSED_DATA_PATH, 'report_list_data.txt')