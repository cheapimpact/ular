import time
import webbrowser, pyautogui, sys
import pandas as pd
import pytesseract
import datetime


def clickOnScreen(
    imagePath, tries=10, isRequired=False, xClickPosition=0.5, yClickPosition=0.5
):
    trial = 0
    is_success = False

    while trial < tries:
        try:
            element = pyautogui.locateOnScreen(imagePath)
            print(element)
            if element is None:
                raise Exception(f"Sorry, no image found")
            pyautogui.moveTo(element)
            print(type(element[2]), element[2])
            moveX = (xClickPosition * element[2]) - (0.5 * element[2])
            moveY = (yClickPosition * element[1]) - (0.5 * element[1])
            pyautogui.moveRel(xOffset=moveX, yOffset=moveY)
            time.sleep(1)
            pyautogui.click()
            is_success = True
            break
        except Exception as e:
            trial += 1
            print(e, trial, imagePath)
            time.sleep(1)
            # if isRequired and trial == tries:
        else:
            break
    return is_success


def my_task_auto_gui():
    # global current_time
    url = "https://office.kemenkeu.go.id/"
    sheet_url = "https://docs.google.com/spreadsheets/d/1D9K2A92K3TACVnH4zu0QsiX1trFzAyUQYkjZB2pavaA/edit#gid=0"
    sheet_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
    ssTask = pd.read_csv(sheet_url)
    webbrowser.register(
        "chrome",
        None,
        webbrowser.BackgroundBrowser(
            "C://Program Files//Google//Chrome//Application//chrome.exe"
        ),
    )
    webbrowser.open_new(url)
    clickOnScreen("./assets/login_button_1.png", xClickPosition=0.9)
    clickOnScreen("./assets/login_button_2.png")
    # time.sleep(3)
    webbrowser.open("https://oa.kemenkeu.go.id/task", new=0)

    if (
        datetime.time(hour=7, minute=00, second=00)
        < current_time
        < datetime.time(hour=7, minute=40, second=00)
    ):  # wkatu untuk clock in
        clickOnScreen("./assets/clock_in.png")
        clickOnScreen("./assets/clock_pop_up.png", xClickPosition=0.1)
    if (
        datetime.time(hour=17, minute=30, second=00)
        < current_time
        < datetime.time(hour=18, minute=00, second=00)
    ):  # wkatu untuk clock out
        clickOnScreen("./assets/clock_out.png")
        clickOnScreen("./assets/clock_pop_up.png", xClickPosition=0.1)

    for index, row in ssTask.iterrows():
        add_task_button = clickOnScreen(
            "./assets/tambah_tugas_button.png", isRequired=True
        )
        time.sleep(1)
        print(add_task_button)
        if add_task_button:
            clickOnScreen(
                "./assets/tusi_non_tusi.png", isRequired=True, xClickPosition=0.4
            )
        else:
            print("add task failed")
            continue
        time.sleep(1)
        print(row["Title"], row["Description"], row["Start Time"], row["End Time"])
        pyautogui.press("tab")
        pyautogui.write(row["Title"])
        pyautogui.press("tab")
        pyautogui.write(row["Description"])
        for i in range(5):
            pyautogui.press("tab")
        if True:  # kedinasan
            pyautogui.press("space")
        else:  # kedinasan
            pyautogui.press("up")
            pyautogui.press("space")

        pyautogui.press("tab")
        splitedST = row["Start Time"].split(":")
        splitedET = row["End Time"].split(":")
        pyautogui.write(splitedST[0])
        pyautogui.press("tab")
        pyautogui.write(splitedST[1])
        pyautogui.press("tab")
        pyautogui.write(splitedET[0])
        pyautogui.press("tab")
        pyautogui.write(splitedET[1])
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click()


# main thread
now = datetime.datetime.now()
current_time = datetime.time(now.hour, now.minute, now.second)
while True:
    # updating time every loop
    now = datetime.datetime.now()
    current_time = datetime.time(now.hour, now.minute, now.second)
    print(f"running...({current_time})")

    if current_time > datetime.time(hour=7, minute=10, second=00):
        my_task_auto_gui()
        print("run your app")
    print("sleep...")
    time.sleep(60)
    break
