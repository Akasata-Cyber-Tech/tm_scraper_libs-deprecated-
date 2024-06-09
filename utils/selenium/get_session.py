import time
import random
from modules.custom_modules_import import *
from utils.selenium.web_driver import check_cookie_24
from utils.selenium.web_driver import run_firefox
from utils.selenium.web_driver import get_token
from modules.requirements_modulees import *
# from modules.custom_modules_import import *
# from modules.requirements_modulees import *
from icecream import ic
import_base_modules()
import_custom_modules()    
def login_tm(driver: webdriver, username: str, password: str):
    url = 'https://portal.sg.xdr.trendmicro.com/'
    # url = 'https://signin.v1.trendmicro.com/'

    # print(username)
    # print(password)
    # driver.quit()
    # sys.exit()

    driver.get(url)
    
    print("[*] find username input")
    i = 0
    while i < 10:
        try:
            input_user = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@id="username"]'))
            )
            # print(input_user)
            if input_user:
                print("[+] found username input")
            else:
                print('uname not found')

            # print("[+] found username input")
            input_user.send_keys(username)
            time.sleep(random.choice(range(3,6)))
            time.sleep(5)
            ic(input_user.send_keys(Keys.ENTER))
            input_user2 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@id="username"]'))
            )
            ic(input_user2)

            if not input_user2:
                time.sleep(2)
                print("retrying...")
            else:
                with open('debug_data-dev-v1.html','w') as html:
                    html.write(driver.page_source)
                break
        except Exception as err:
            print(err)
            print("retrying...")
            with open('debug_data-dev-v1.html','w') as html:
                html.write(driver.page_source)
            ic(err)
            time.sleep(1)
            # driver.quit()
            i +=1
            # sys.exit('[!] Failed get element input username')
    # print("[*] find btn_sign_in")
    # try:
    #     btn_sign_in = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//button[@data-test="_IAM_SIGN_IN_BTN_"]'))
    #     )
    #     # print(input_user)
    #     print("[+] found btn sign in")
    #     btn_sign_in.click()
    # except Exception as err:
    #     print(err)
    #     driver.quit()
    #     sys.exit('[!] Failed click btn sign in')

    # print("[*] find password input")

    i = 0
    while i <= 10:
        try:
            input_password = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))
            )
            print("[+] found input password")

            input_password.send_keys(password)
            input_password.send_keys(Keys.ENTER)
            break
        except Exception as err:
            print(err)
            print(driver.page_source)
            i += 1
            driver.quit()
            sys.exit('[!] Failed get element input password')


    try:
        user_img = WebDriverWait(driver, 70).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.uic_avatar'))
        )
        print('user_img', user_img)
    except Exception as err:
        print(err)
        driver.quit()
        sys.exit('[!] Login failed')

    # seach_query(driver, 'test')

    cookie = driver.get_cookies()
    with open(COOKIE_PATH, 'wb') as fp:
        pickle.dump(cookie, fp)

    driver.quit()

    # return driver.get_cookies()


def login(username: str,password: str):
    # GECKO_DRIVER = os.getenv("GECKO_DRIVER")
    # DRIVER_PATH = os.getenv("DRIVER_PATH")
    # COOKIE_PATH = os.getenv("COOKIE_PATH")
    # username = 'soc.user2@pelindo.co.id'
    # password = 'P#lindo@2023'

    if not os.path.isdir(DRIVER_PATH):
        os.makedirs(DRIVER_PATH, 0o755)
    if not os.path.isfile(GECKO_DRIVER):
        print(os.getenv("BASE_PATH"))
        print(os.getenv("DRIVER_PATH"))
        print(os.getenv("GECKO_DRIVER"))
        print(os.path.isfile(GECKO_DRIVER))
        sys.exit('[!] Please download geckodriver.exe')
        # print(os.path.isfile(GECKO_DRIVER))

    check_cookie_24()

    if not os.path.isfile(COOKIE_PATH):
        driver = run_firefox()
        # driver = run_chromium()
        login_tm(driver, username, password)

    # if not os.path.isfile(COOKIE2_PATH):
    #     driver = run_firefox()
    #     get_exploit_db(driver)
    token = get_token()
    return token