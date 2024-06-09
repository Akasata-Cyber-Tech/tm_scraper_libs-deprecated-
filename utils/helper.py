import pickle
import os
from datetime import datetime

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DRIVER_PATH = os.path.join(BASE_PATH, '../drivers')
MODULES_PATH = os.path.join(BASE_PATH, '../modules')
DATA_PATH = os.path.join(BASE_PATH, '../data_path')
PARSED_DATA_PATH = os.path.join(BASE_PATH, '../parsed_data_path')
GECKO_DRIVER = os.path.join(DRIVER_PATH, 'geckodriver.exe')
CHROME_DRIVER = os.path.join(DRIVER_PATH, 'chromium.exe')
COOKIE_PATH = os.path.join(DRIVER_PATH, 'cookies.pkl')
# DATA_PATH = os.path.join(DRIVER_PATH, 'searchFormat.tm')
COOKIE2_PATH = os.path.join(DRIVER_PATH, 'cookies2.pkl')


def import_cookies():
    with open(COOKIE_PATH, 'rb') as fp:
        cookies = pickle.load(fp)
        return cookies
    
class timestamp:
    now = datetime.now()
    to_timestamp = now.timestamp()
    from_timestamp = to_timestamp -(3600*1)