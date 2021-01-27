#Selenium Webdriver must be installed for this to work

import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 3 #(3 seconds)

#youtube link
link = https://youtu.be/9YFDtiibCQc
#number of views
views = 4000

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
