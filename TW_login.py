from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secrets import pw
import time

browser = webdriver.Firefox()
browser.get("https://twitter.com/login/error?redirect_after_login=%2F")
time.sleep(3)

uname = browser.find_element_by_name("session[username_or_email]")
psword = browser.find_element_by_name("session[password]")
psword = browser.find_element_by_name("session[password]")

time.sleep(1)
uname.send_keys("")
psword.send_keys(pw)
psword.send_keys(Keys.RETURN)
