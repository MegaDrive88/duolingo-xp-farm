from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants import *

service = Service(executable_path="chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")

driver = webdriver.Chrome(service = service, options = chrome_options)

driver.get("https://duolingo.com")
driver.maximize_window()
login_btn = driver.find_element(By.CLASS_NAME, "_2V6ug")
login_btn.click()

username_inp = driver.find_element(By.ID, "web-ui1")
username_inp.send_keys(EMAIL)
pwd_inp = driver.find_element(By.ID, "web-ui2")
pwd_inp.send_keys(PWD + Keys.ENTER)

part = "1"

while True:
    try:
        if (not COOKIES_ENABLEd):
            driver.execute_script("""
                let l = document.querySelector(".fc-consent-root");
                l.parentElement.removeChild(l);""")
            COOKIES_ENABLEd = True
        practice_btn = driver.find_element(By.CSS_SELECTOR, r'a[href="/characters"]')
        practice_btn.click()
        break
    except: pass

def element_exist(by, value):
    try:
        _ = driver.find_element(by, value)
        return True
    except:
        return False

def start_lesson():
    start_btn = driver.find_element(By.CSS_SELECTOR, r'a[href="/alphabets/en/pronunciation"]')
    start_btn.click()

def during_lesson(_part):
    skip_btn = driver.find_element(By.CSS_SELECTOR, "button._2V6ug._1ursp._7jW2t._2x7Co._3fo6Q")
    body = driver.find_element(By.CSS_SELECTOR, r'body')
    if(element_exist(By.CSS_SELECTOR, "button._3xDVI._2V6ug._1ursp._7jW2t.YvvwP._3U5_i")):
        skip_btn.click()
        body.send_keys(Keys.ENTER)
    elif (_part == "1" and element_exist(By.CSS_SELECTOR, "button._3fmUm._2V6ug._1ursp._7jW2t.notranslate._3ZtW_._2O7Ua._3U5_i._3Ymqr")):
        for i in range(1, 5):
            for j in range(5, 9):
                body.send_keys(f"{i}{j}")
        body.send_keys("1" + Keys.ENTER)
        return "2"
    else:
        body.send_keys(_part + Keys.ENTER + Keys.ENTER)
    return _part

def after_lesson():
    proceed_btn = None
    if (element_exist(By.CSS_SELECTOR, "button._1rcV8._1VYyp._1ursp._7jW2t._3DbUj._38g3s._2oGJR:not(._2wryV)")): 
        proceed_btn = driver.find_element(By.CSS_SELECTOR, "button._1rcV8._1VYyp._1ursp._7jW2t._3DbUj._38g3s._2oGJR:not(._2wryV)")
    elif (element_exist(By.CSS_SELECTOR, "button._1rcV8._1VYyp._1ursp._7jW2t._5eJl._3DbUj")):
        proceed_btn = driver.find_element(By.CSS_SELECTOR, "button._1rcV8._1VYyp._1ursp._7jW2t._5eJl._3DbUj")
    elif (element_exist(By.CSS_SELECTOR, "button._3xDVI._2V6ug._1ursp._7jW2t._1Z5a5._1CpJa")):
        proceed_btn = driver.find_element(By.CSS_SELECTOR, "button._3xDVI._2V6ug._1ursp._7jW2t._1Z5a5._1CpJa")
    if (proceed_btn == None): raise ValueError
    else: proceed_btn.click()


i = 0
driver.execute_script("document.body.style.zoom='50%'")
while True:
    if(i >= ITERS): break
    try:
        start_lesson()
        part = "1"
    except:pass
    while True:
        try:
            part = during_lesson(part)
        except:
            try:
                after_lesson()
                i+=1
            except: break

driver.quit()