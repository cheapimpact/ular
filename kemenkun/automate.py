from lib2to3.pgen2 import driver
from pprint import pprint
from re import L
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from threading import Timer
from datetime import date
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

count = 0
task = 0
sheetUrl = "https://docs.google.com/spreadsheets/d/1D9K2A92K3TACVnH4zu0QsiX1trFzAyUQYkjZB2pavaA/edit#gid=0"
sheetUrl = sheetUrl.replace("/edit#gid=", "/export?format=csv&gid=")
ssTask = pd.read_csv(sheetUrl)
# pprint(ssTask)
# for index in range(len(ssTask)):
#     print(ssTask.loc[index, "Description"])
# exit()


def closeModal():
    try:
        browser.find_element(By.XPATH, "//button[@aria-label='Close dialog']").click()
    except:
        print("noModal")


def addTask():
    try:
        time.sleep(1)
        Timer(8, closeModal())
        global count, task
        count += 1

        print(count, "try")
        addTaskButton = browser.find_element(By.CLASS_NAME, "add-todo-button")
        addTaskButton.click()
        print(f"tambah tugas {task}")
        nonTusiButton = browser.find_element(
            By.XPATH, '//mat-radio-button[@value="NonTusi"]'
        )
        nonTusiButton.click()
        time.sleep(1)
        browser.find_element(By.XPATH, "//input[@name='Judul']").send_keys(
            f"coba coba {task}"
        )
        browser.find_element(By.XPATH, "//textarea[@name='Description']").send_keys(
            f"test keterangan{task}"
        )
        time.sleep(1)
        browser.find_element(
            By.XPATH, "//mat-radio-button[@value='TanpaPersetujuan']//label"
        ).click()
        time.sleep(1)
        startTime = browser.find_elements(
            By.XPATH, "//ngx-timepicker-field[@formcontrolname='StartTime']//input"
        )
        # startTime[0].send_keys("08")
        # startTime[1].send_keys("00")
        endTime = browser.find_elements(
            By.XPATH, "//ngx-timepicker-field[@formcontrolname='EndTime']//input"
        )
        # ActionChains(browser).moveToElement(EndTime).perform()
        # endTime[0].click()
        # endTime[0].send_keys("12")

        # endTime[1].send_keys("00")
        # # print(startTime)
        time.sleep(1)

        ActionChains(browser).move_to_element(startTime[0]).click().send_keys(
            "08"
        ).send_keys(Keys.TAB).send_keys("00").send_keys(Keys.TAB).send_keys(
            "12"
        ).send_keys(
            Keys.TAB
        ).send_keys(
            "00"
        ).send_keys(
            Keys.TAB
        ).perform()
        browser.find_element(
            By.XPATH, "//button//span[normalize-space()='Tambah']"
        ).click()
        time.sleep(2)
        if task != 3:
            task += 1
            addTask()
    except:
        addTask()


options = webdriver.ChromeOptions()
options.add_argument = {
    r"--user-data-dir=C:\Users\KEMENKEU\AppData\Local\Google\Chrome\User Data\Default"
}
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
# browser = webdriver.Chrome(chrome_options=options)

browser.get("https://office.kemenkeu.go.id/")
linkElem = browser.find_element(By.LINK_TEXT, "LOGIN")
linkElem.click()
loginUsernameElem = browser.find_element(By.ID, "username")
loginPasswordElem = browser.find_element(By.ID, "password")
loginUsernameElem.send_keys("199903112018011001")
loginPasswordElem.send_keys("J3nni3bp")
loginButtonElem = browser.find_element(By.XPATH, '//button[normalize-space()="LOGIN"]')
type(loginButtonElem)
loginButtonElem.click()
print("Auth Code :")
auth_code = input()
codeElem = browser.find_element(By.ID, "code")
codeElem.send_keys(auth_code)

verificationButtonElem = browser.find_element(
    By.XPATH, '//button[normalize-space()="Verifikasi"]'
)
verificationButtonElem.click()
try:
    closeButton = browser.find_element(By.XPATH, '//span[contains(text(),"TUTUP")]')
    closeButton.click()
    print("banner   ")
except:
    print("noBanner")
time.sleep(1)
browser.get("https://oa.kemenkeu.go.id/task")
browser.fullscreen_window()
time.sleep(1)
# // To zoom in 3 times
# for(int i=0; i<3; i++){
# driver.findElement(By.tagName("html")).sendKeys(Keys.chord(Keys.CONTROL,Keys.ADD));
# }
# // To zoom out 3 times
for i in range(4):
    browser.find_element(By.TAG_NAME, "html").send_keys(Keys.CONTROL, Keys.SUBTRACT)
# //To set the browser to default zoom level ie., 100%
# driver.findElement(By.tagName("html")).sendKeys(Keys.chord(Keys.CONTROL, "0"));
# }
time.sleep(3)

addTask()


browser.implicitly_wait(10000)
# browser.get_screenshot_as_png()
