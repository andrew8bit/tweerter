
from selenium import webdriver
import time, requests
from keys import username, password
from quotes import quote_picker

driver = webdriver.Chrome('/Users/andrewbith/desktop/chromedriver')
time.sleep(2)

driver.get('https://www.twitter.com')
time.sleep(2)


driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
time.sleep(2)

# Login
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(password)
# Click the sign in button
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
time.sleep(2)

# inserting random quote from API

def tweet():
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys(quote_picker())
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span').click()

# this is tweeting our quote 5 times, once every 6
count = 0
while count < 5:
     tweet()
     count+=1
     time.sleep(6) 
