from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secrets import pw
import time


class TwiterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.TwiterBot = webdriver.Firefox()

    def login(self):
        bot = self.TwiterBot
        bot.get("https://twitter.com/login/error?redirect_after_login=%2F")
        time.sleep(1)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(1)

    def like_tweet(self, hashtag):
        bot = self.TwiterBot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(1)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('twitterEntities')
                for elem in tweets]
            print(links)


ed = TwiterBot('name', pw)
ed.login()
ed.like_tweet('hastag')
