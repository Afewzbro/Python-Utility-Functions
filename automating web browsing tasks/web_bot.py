# pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
DOWNLOAD_PATH = "/home/testi/Downloads/chromedriver_linux64/chromedriver"   
bot = webdriver.Chrome(DOWNLOAD_PATH)
bot.get('http://www.google.com')
search = bot.find_element_by_name('q')
search.send_keys("@codedev101")
search.send_keys(Keys.RETURN)
time.sleep(5)
bot.quit()