import utils.helper as helper
import requests
import json
import sys

def suspicious_object_collector(token):
    pageNumber = 0

    
    headers = {'Content-type': 'application/json', 'Uic-Token': token}
    
    cookies = helper.import_cookies()
    
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    suspiciousObjectList = []

    try: 
        dataEnum = 0
        try:
            counter_url = f'https://portal.sg.xdr.trendmicro.com/ui/atl/api/v2/ctd/udsocount?currentPage=1&pageSize=200&sortKey=updated_time&reverse=true'
            startUrl = f'https://portal.sg.xdr.trendmicro.com/ui/atl/api/v2/ctd/udso?currentPage=1&pageSize=200&sortKey=updated_time&reverse=true'
            
            counter_response = session.get(counter_url, headers=headers)
            counter_data = counter_response.json()
            total_data = counter_data['data']['count']
            response = session.get(startUrl, headers=headers)
            data = response.json()
            for i in data['data']['items']:
                    suspiciousObjectList.append(i)
            nextToken = data['data']['nextToken']
            print(startUrl)
            dataEnum += 200
        except:
            sys.exit('something wrong hapened!')

        pageEnum = 2
        while dataEnum < total_data:
            nextUrl = f'https://portal.sg.xdr.trendmicro.com/ui/atl/api/v2/ctd/udso?currentPage={pageEnum}&pageSize=200&sortKey=updated_time&reverse=true&nextToken={nextToken}'
            response = session.get(nextUrl, headers=headers)
            data = response.json()
            nextToken = data['data']['nextToken']
            for i in data['data']['items']:
                suspiciousObjectList.append(i)
            data_json = json.dumps(data, indent=4)
            with open('suspiciousObject.json', 'w') as exect:
                exect.write(data_json)
            print(nextUrl)
            dataEnum += 200
            pageEnum += 1
        
        print(data_json)
        # print(f'Page Enumeration Finished {err}')
        items = json.dumps(suspiciousObjectList, indent=4)
        with open('test_sus_object_parser.json', 'w') as file:
            file.write(data_json)

    except Exception as err:
        print(f'Page Enumeration Finished {err}')
        items = json.dumps(suspiciousObjectList, indent=4)
        with open('test_sus_object_parser.json', 'w') as file:
            file.write(items)
    sys.exit()

    
    
    # susObjects = [sus['value'] for sus in data['data']['items']]
    # desc = [desc['description'] for desc in data['data']['items']]
    # objList = {'objects':susObjects[loops],'desc':desc[loops]}
    
    suspiciousObject = data['data']['items'][loops]['value']
    content = json.dumps(response.json(), indent=4)
    try:
        susObjectData = []
        for objects in data['data']['items']:
            objList = {'objects':objects['value'],'desc':objects['description']}
            susObjectData.append(objList)
        with open('suspiciousObject.json', 'w') as exect:
            exect.write(susObjectData)
        print(f"File '{'suspiciousObject.json'}' created successfully.")
    except Exception as err:
        print(err)
    # json_data = json.dumps(response)
    
    # response = session.post(url, data=json_data, headers=headers


    # def suspicious_object_filter():
        # uri_counter = https://portal.sg.xdr.trendmicro.com/ui/atl/api/v2/ctd/udsocount?filter=counterboring.sbs&currentPage=1&pageSize=200&sortKey=updated_time&reverse=true

        
        # uri_detials = # https://portal.sg.xdr.trendmicro.com/ui/atl/api/v2/ctd/udso?filter=counterboring.sbs&currentPage=1&pageSize=200&sortKey=updated_time&reverse=true

        # method = GET 

#         response :
        #         {
        #     "data": {
        #         "items": [
        #             {
        #                 "updated_time": 1712922945,
        #                 "customer_id": "3323542f-00d6-4701-86b3-6be30a0d1863",
        #                 "source": {
        #                     "type": "import",
        #                     "file_sha256": "4a8a88da5f1747e1d096d77de16395567a47bd1ad13b191c6e4c422775bdbc71",
        #                     "file_type": "csv",
        #                     "file_name": "Raspberry Robin Malware  IoC - 1.csv"
        #                 },
        #                 "sync_status": "success",
        #                 "risk_level_number": 3,
        #                 "scan_action": "log",
        #                 "updated_by": "SOC MXDR",
        #                 "search_key": "counterboring.sbs\nraspberry robin malware  ioc - 1.csv",
        #                 "expired_time": -1,
        #                 "valid": true,
        #                 "source_details": "Raspberry Robin Malware  IoC - 1.csv",
        #                 "id": "1f171a4a1cf6549fbe6e5a00b7d360b7b78c504cde41d75465bd56625ee54e8c",
        #                 "risk_level": "high",
        #                 "type": "domain",
        #                 "value": "counterboring.sbs",
        #                 "so_source": "udso"
        #             }
        #         ],
        #         "size": 1,
        #         "lastSync": 1713025005
        #     }
        # }

