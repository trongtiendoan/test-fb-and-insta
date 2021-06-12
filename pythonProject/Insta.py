from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException


chromedriver_path = r'C:\eclipse\chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

commentsDict = [ "<3","<3"]

username = webdriver.find_element_by_name('username')
username.send_keys('karitodragneel2@gmail.com')
password = webdriver.find_element_by_name('password')
password.send_keys('anhlafaker')
button_login = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
button_login.click()
sleep(2)

try:
    notsave = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    notsave.click()
    sleep(2)
except:
    sleep(2)

try:
    notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click()
    sleep(2)
except:
    sleep(2)

sleep(1)
usernameofperson="sontungmtp/" # enter the other username whose post you want to like and comment
webdriver.get('https://www.instagram.com/' + usernameofperson)
sleep(2)
first_thumbnail = webdriver.find_element_by_xpath("//body//div[@id='react-root']//div[contains(@class,'_2z6nI')]//div//div//div[1]//div[1]//a[1]//div[1]//div[2]")
first_thumbnail.click()
sleep(2)
next_post='1'
null=''
liked,unlike=0,0
while next_post is not null:
    if liked>0 or unlike>0:
        next_post.click()
        sleep(2)
    like = webdriver.find_element_by_xpath("//*[@aria-label='Thích']")
    like.click()
    liked +=1
    sleep(2)
    commentArea = webdriver.find_element_by_class_name('Ypffh')
    commentArea.click()
    sleep(1)
    commentArea = webdriver.find_element_by_class_name('Ypffh')
    commentArea.send_keys(random.choice (commentsDict))
    sleep(1)
    commentArea.send_keys(Keys.ENTER)
    sleep(2)
    try:
        next_post = webdriver.find_element_by_link_text('Tiếp')
    except :
        next_post = null
    if liked==5:
        print(liked)
        break
print(str(liked)+' Posts Liked!')