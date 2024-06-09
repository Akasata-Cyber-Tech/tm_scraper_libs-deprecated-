from modules.custom_modules_import import *
from modules.requirements_modulees import *
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
    try:
        input_user = WebDriverWait(driver, 70).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="username"]'))
        )
        # print(input_user)
        input_user.send_keys(username)
        input_user.send_keys(Keys.ENTER)
    except Exception as err:
        print(err)
        driver.quit()
        sys.exit('[!] Failed get element input username')

    try:
        input_password = WebDriverWait(driver, 70).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]'))
        )
        input_password.send_keys(password)
        input_password.send_keys(Keys.ENTER)
    except Exception as err:
        print(err)
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
