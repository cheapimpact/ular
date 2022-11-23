# https://uangmakan.vercel.app/from
# lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import re

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://uangmakan.vercel.app/")
while True:
    browser.implicitly_wait(5)  # gives an implicit wait for 20 seconds
    question = browser.find_element(By.XPATH, '//*[@class="test"]/h1')
    questionGet = re.split("(\d) \+ (\d)", question.text)
    print((questionGet[1]) + (questionGet[2]))
    answer = (int(questionGet[1]) + int(questionGet[2])) % 2
    print(answer)
    option = browser.find_element(By.XPATH, f'//button[normalize-space()="{answer}"]')
    option.click()
# linkElem = browser.find_element(By.LINK_TEXT, "LOGIN")
# type(linkElem)
# linkElem.click()  # follows the "Read Online for Free" link
# loginUsernameElem = browser.find_element(By.ID, "username")
# loginPasswordElem = browser.find_element(By.ID, "password")
# loginUsernameElem.send_keys("199903112018011001")
# loginPasswordElem.send_keys("J3nni3bp")
# loginButtonElem = browser.find_element(By.XPATH, '//button[normalize-space()="LOGIN"]')
# type(loginButtonElem)
# loginButtonElem.click()
# browser.implicitly_wait(10000)
# browser.get_screenshot_as_png()
