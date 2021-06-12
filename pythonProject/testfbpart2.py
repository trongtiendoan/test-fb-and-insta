from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pydirectinput
from pynput.keyboard import Key, Controller
import pyautogui
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path="C:\eclipse\chromedriver.exe")
driver.get("https://www.facebook.com")
username = driver.find_element_by_xpath("//*[@id='email']")
username.send_keys("karitodragneel2@gmail.com")
time.sleep(2)
password = driver.find_element_by_xpath("//*[@id='pass']")
password.send_keys("anhlakarito123")
time.sleep(2)
submit = driver.find_element_by_xpath("//*[@name='login']")
submit.click()
time.sleep(1)
driver.get("https://www.facebook.com/ShadyVocalFacts")
keyboard = Controller()
time.sleep(2)
pyautogui.FAILSAFE= False
pyautogui.press('j')
for j in range(0,1):
    pyautogui.press('j')
    time.sleep(2)
for i in range(0,7):
    pyautogui.press('j')
    time.sleep(2)
    pyautogui.press('l')
    time.sleep(2)
    pyautogui.press('enter')

