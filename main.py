from random import randint

import secrets
from selenium import webdriver
from time import sleep
from generate_urls import subs_with_urls

PATH = '/Users/blackout/reddit_subreddit_manager/chromedriver'  # Change this to your chromedriver path
driver = webdriver.Chrome(PATH)

driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F')

# Credentials and Login
username = driver.find_element_by_id('loginUsername')
password = driver.find_element_by_id('loginPassword')
username.send_keys(secrets.username)
password.send_keys(secrets.password)
driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()

# to bypass chrome popup notification
sleep(5)

for line in subs_with_urls:
    driver.get(line)
    # you can change the range if you want it to go faster
    # but be careful to not spam the reddit server with too many requests!
    # sleep(2)
    sleep(randint(5, 20))

    if line[23] == 'r':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/button').click()
    else:
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div[2]/div/div[1]/div/div[5]/div[1]/button').click()
    sleep(2)
driver.quit()
