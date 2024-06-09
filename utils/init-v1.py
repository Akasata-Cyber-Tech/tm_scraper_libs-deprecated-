import sys
from modules.custom_modules_import import *
from modules.requirements_modulees import *
from icecream import ic
import_base_modules()
import_custom_modules()
def run_firefox():
    
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    options.add_argument('-allow-host')
    
    # options.binary_location = ''
    # options.binary_location = '/bin/firefox'
    options.accept_insecure_certs = True
    options.set_preference('geo.prompt.testing', True)
    options.set_preference('geo.prompt.testing.allow', False)
    options.set_preference('javascript.enabled', True)


    # print(options)
    # sys.exit()

    # noinspection PyBroadException
    try:
        driver = webdriver.Firefox(options=options)
        ic(driver)
    except Exception as err:
        # ic(driver)
        sys.exit(f'[!] Failed to run firefox {err}')

    return driver

def run_chromium():
    
    options = webdriver.ChromeOptions
    options.binary_location = ''
    # options.capabilities["chromium"]

    # options.set_preference('geo.prompt.testing', True)
    # options.set_preference('geo.prompt.testing.allow', False)
    chromedriver_path = '/path/to/chromedriver'

    

    try:
        driver = webdriver.Chrome(options=options)
    except Exception as err:
        ic(driver)
        sys.exit(f'[!] Failed to run chrome {err}')

    return driver
      
def get_token():
    # url = 'https://portal.sg.xdr.trendmicro.com/#/app/search'
    url = 'https://portal.sg.xdr.trendmicro.com/ui/uic/v3/session'

    with open(COOKIE_PATH, 'rb') as fp:
        cookies = pickle.load(fp)

    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    response = session.get(url)

    # print(response.json())
    # print(response.headers)
    # sys.exit()
    # token = response.headers.get('uic-token')
    # print('token', token)
    # if token:
    #     return token
    return response.headers.get('uic-token')

def check_cookie_24():
    try:
        # Mendapatkan waktu terakhir modifikasi file
        waktu_modifikasi = os.path.getmtime(COOKIE_PATH)

        # Mendapatkan waktu saat ini
        waktu_sekarang = time.time()

        # Menghitung selisih waktu antara waktu modifikasi dan waktu saat ini
        selisih_waktu = waktu_sekarang - waktu_modifikasi

        # Jika selisih waktu lebih dari 24 jam (86400 detik), hapus file
        if selisih_waktu > 1800:
            os.remove(COOKIE_PATH)
            print(f"File {COOKIE_PATH} dihapus karena lebih dari 30 menit.")
        else:
            print(f"File {COOKIE_PATH} tidak dihapus karena belum lebih dari 30 menit.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
    try:
        # Mendapatkan waktu terakhir modifikasi file
        waktu_modifikasi = os.path.getmtime(COOKIE2_PATH)

        # Mendapatkan waktu saat ini
        waktu_sekarang = time.time()

        # Menghitung selisih waktu antara waktu modifikasi dan waktu saat ini
        selisih_waktu = waktu_sekarang - waktu_modifikasi

        # Jika selisih waktu lebih dari 24 jam (86400 detik), hapus file
        if selisih_waktu > 1800:
            os.remove(COOKIE2_PATH)
            print(f"File {COOKIE2_PATH} dihapus karena lebih dari 30 menit.")
        else:
            print(f"File {COOKIE2_PATH} tidak dihapus karena belum lebih dari 30 menit.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
