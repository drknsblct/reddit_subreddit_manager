import secrets
from random import randint
from selenium import webdriver
from time import sleep

PATH = './chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F')

# credentials and login
username = driver.find_element_by_id('loginUsername')
password = driver.find_element_by_id('loginPassword')
username.send_keys(secrets.username)
password.send_keys(secrets.password)
driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()

subreddit_xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/button'
user_xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div[2]/div/div[1]/div/div[5]/div[1]/button'

# to bypass chrome popup notification
sleep(5)

with open('subs.txt', 'r') as f:
    for line in f:
        if line == '\n':
            continue

        if line[:2] == 'u/':
            driver.get(f'https://www.reddit.com/{line}')
        else:
            driver.get(f'https://www.reddit.com/r/{line}')

        # you can change the sleep range if you want it to go faster
        # but be careful to not spam the reddit server with too many requests!
        # sleep(randint(5, 20))
        sleep(2)

        if line[:2] == 'u/':
            driver.find_element_by_xpath(user_xpath).click()
        else:
            driver.find_element_by_xpath(subreddit_xpath).click()

    sleep(2)
driver.quit()



