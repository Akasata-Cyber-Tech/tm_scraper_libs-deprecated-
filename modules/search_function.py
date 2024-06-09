from .fieldsData import fieldList
from datetime import datetime
import json



def search_data_groups(token: str, keyword: str,type: str,isPer3H: bool):
    # with open(COOKIE_PATH, 'rb') as fields:
        
    url = "https://portal.sg.xdr.trendmicro.com/ui/ase/api/search_agg"
    
    now = datetime.now()
    to_timestamp = now.timestamp()
    from_timestamp = to_timestamp - (3600*8)
    if isPer3H:
        to_timestamp = now.timestamp()
        from_timestamp = to_timestamp - (3600*3)
        

    headers = {'Content-type': 'application/json', 'Uic-Token': token}
    
    search_type = type
    
    malware_data_groups = {
        "dataSource": 2,
        "dataType": 2,
        "from": from_timestamp,
        "to": to_timestamp,
        "query": keyword,
        "searchType": 1,
        "filters": [],
        "aggFields": fieldList.malwareFields
    }
    activity_data_groups = {
        "dataSource": 10,
        "dataType": 1,
        "from": from_timestamp,
        "to": to_timestamp,
        "query": keyword,
        "searchType": 1,
        "filters": [],
        "aggFields": fieldList.activityFields
    }
        
    attacks_data_groups = {
        "dataSource": 2,
        "dataType": 2,
        "from": from_timestamp,
        "to": to_timestamp,
        "query": keyword,
        "searchType": 1,
        "filters": [],
        "aggFields": fieldList.attacksFields
    }
    dns_data_groups = {
        "dataSource": 2,
        "dataType": 2,
        "from": from_timestamp,
        "to": to_timestamp,
        "query": keyword,
        "searchType": 1,
        "filters": [],
        "aggFields": fieldList.dnsFields
    }
    
    search_malware = malware_data_groups
    search_attacks = attacks_data_groups
    search_dns = dns_data_groups
    search_activity = activity_data_groups
    
    if search_type == "malware":
        json_data = json.dumps(search_malware)
        type = "malware"
    elif search_type == "attacks":
        json_data = json.dumps(search_attacks)
        type = "attacks"
    elif search_type == "suspicious_dns":
        json_data = json.dumps(search_dns)
        type = "suspicious_dns"
    elif search_type == "behavior_violation":
        json_data = json.dumps(search_activity)
        type = "behavior_violation"
    else:
        print('terdapat kesalahan pada tipe pencarian')
        
    with open(COOKIE_PATH, 'rb') as fp:
        cookies = pickle.load(fp)

    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    response = session.post(url, data=json_data, headers=headers)
    data_json = json.dumps(response.json())
    # print(response.json())
        
    export_json_data_groups(data_json, type)
    return data_json

def seach_query(token: str, keyword: str, type:str):
    # url = 'https://portal.sg.xdr.trendmicro.com/#/app/search'
    url = 'https://portal.sg.xdr.trendmicro.com/ui/ase/api/search'

    now = datetime.now()
    to_timestamp = now.timestamp()
    from_timestamp = to_timestamp - (3600*8)

    headers = {'Content-type': 'application/json', 'Uic-Token': token}

    search = {
        'dataSource': 0,
        'dataType': 0,
        'filters': [],
        'from': from_timestamp,
        'to': to_timestamp,
        'searchType': 0,
        'query': keyword
    }
    json_data = json.dumps(search)

    with open(COOKIE_PATH, 'rb') as fp:
        cookies = pickle.load(fp)

    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    response = session.post(url, data=json_data, headers=headers)
    data_json = json.dumps(response.json())
    # print(response.json())

    export_json_search(data_json,type)
    return data_json
