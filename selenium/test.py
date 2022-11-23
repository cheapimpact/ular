from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(
    ChromeDriverManager().install(),
)
# driver = webdriver.Chrome(chrome_options=options)
driver.get("https://office.kemenkeu.go.id/")

# create action chain object
action = ActionChains(driver)

# perform the operation
action.scroll_by_amount(1000, 1000)

# c = driver.find_element(By.TAG_NAME, "window")
# c.send_keys(Keys.Chord)
# c.send_keys(Keys.LEFT_CONTROL + "-")

driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
# driver.find_element(By.TAG_NAME, "html").send_keys(Keys.CONTROL + Keys.ADD)
# driver.find_element(By.TAG_NAME, "html").send_keys(Keys.CONTROL + Keys.ADD)
# driver.find_element(By.TAG_NAME, "html").send_keys(Keys.CONTROL + Keys.ADD)
print("end")
input()
