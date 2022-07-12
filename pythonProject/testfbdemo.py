from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from time import sleep
# import pydirectinput
# from pynput.keyboard import Key, Controller
import pyautogui
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

edgedriver_path = Service('D:\edgedriver_win64\msedgedriver.exe')
webdriver = webdriver.Edge(service=edgedriver_path)
webdriver.get("https://www.facebook.com")
sleep(10)

username = webdriver.find_element_by_xpath("//*[@id='email']")
username.send_keys("karitodragneel2@gmail.com")
sleep(2)
password = webdriver.find_element_by_xpath("//*[@id='pass']")
password.send_keys("karitodragneel2011")
sleep(2)
submit = webdriver.find_element_by_xpath("//*[@name='login']")
submit.click()
sleep(1)

like = webdriver.find_element_by_xpath("//div[@class = 'tvfksri0 ozuftl9m']//div[@aria-label = 'Thích']")

sleep(2)
pyautogui.FAILSAFE= False
pyautogui.press('j')
for i in range(0,7):
    pyautogui.press('j')
    sleep(2)
    like.click()
    sleep(2)

