from modules.custom_modules_import import *
from modules.requirements_modulees import *
import_base_modules()
import_custom_modules() 

    
def post_sus_object_tm(token: str):
    url = "https://portal.sg.xdr.trendmicro.com/ui/atl/api/v2/ctd/udso"
    with open('blocklist.txt', 'r') as blocklist:
        list = blocklist.read()
        ip_blocklist = list.split('\n')
    # Expire For 30 Days
    # print(token)
    # sys.exit()
    headers = {'Content-type': 'application/json', 'Uic-Token': token, 'Referer': 'https://portal.sg.xdr.trendmicro.com/ui/atl/ctd/list/'}

    now = datetime.now()
    expire_time = now.timestamp() + (18144000*3)
    ip = 0
    while(ip < len(ip_blocklist)):
        ip_list = ip_blocklist[ip - 1]
        desc =  f'{ip_list} indicated as botnet from https://feodotracker.abuse.ch/downloads/ipblocklist.txt Last updated: 2024-03-06 16:34:45 UTC'
        data = {
        "action": "add",
        "updated_by": "Soc User 2",
        "so_list": [
            {
                "source": {
                    "type": "manual"
                },
                "description": desc,
                "expired_time": expire_time,
                "scan_action": "block",
                "risk_level": "high",
                "type": "ip",
                "value": ip_list
            }
        ]
    }
        # print(post_data)
        time.sleep(2.5)
        print('cotto matte....')
        # sys.exit()
        with open(COOKIE_PATH, 'rb') as fp:
            cookies = pickle.load(fp)
            
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
            
        post_data = json.dumps(data)
        response = session.post(url, data=post_data, headers=headers)
        # print('tunggu bentarr....')
        # time.sleep(1)
        print(response.text)
        print(response)
        response
        # return(response)
        ip += 1
  