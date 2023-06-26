from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
import time
from get_web import *

driver = get_web_driver()
url  = "https://ctf.bugku.com/login.html"
driver.get(url)

def login(user,pwd,tav):
    username = driver.find_element(By.NAME, "username")
    username.send_keys(user)
    password = driver.find_element(By.NAME, "password")
    password.send_keys(pwd)
    test = driver.find_element(By.NAME, "vcode")
    test.send_keys(tav)

def get_img():
    img = driver.find_element(By.ID,'vcode')
    file_name = 'captcha.jpg'
    img.screenshot('./' + file_name)
    
def tav_read():
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open('./captcha.jpg','rb') as f:
        img_tav = f.read()
    tav = ocr.classification(img_tav)
    # print(tav)
    return tav

def login_click():
    login_ck = driver.find_element(By.ID, 'login')
    login_ck.click()

def SignIn():
    o = driver.find_element(By.XPATH, '//*[@id="checkin-status"]/button')
    if o.text == "签到":
        o.click()
        print("签到")
    else:
        print(o.text)

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    get_img()
    login(user,pwd,tav_read())
    time.sleep(3)
    login_click()
    time.sleep(5)
    SignIn()


