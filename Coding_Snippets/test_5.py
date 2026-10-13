from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Safari()

driver.get("https://smelk.dev/account/")
driver.set_window_size(1400,800)
time.sleep(1)
count = 0

while count < 50:
    pyautogui.leftClick(700, 700)
    time.sleep(1)
    Username = driver.find_element(By.NAME, "username")
    Username.send_keys("Kim")
    time.sleep(0.8)
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("a")
    Password.send_keys(Keys.RETURN)
    time.sleep(3)
    Username = driver.find_element(By.NAME, "username")
    Username.send_keys("Kim")
    time.sleep(0.8)
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("a")
    Password.send_keys(Keys.RETURN)
    time.sleep(1.3)
    driver.get("https://www.smelk.dev/account/bank/?")
    time.sleep(1)
    pyautogui.moveTo(700, 495)
    time.sleep(0.125)
    pyautogui.leftClick()
    pyautogui.press("down", 4, 0.1) # 4 for John Smelk, 11 for Jack Smelk
    time.sleep(0.125)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.leftClick(700, 380)
    Input = driver.find_element(By.ID, "amount")
    Input.send_keys("1")
    Input.send_keys(Keys.ENTER)
    time.sleep(0.5)
    driver.get("https://www.smelk.dev/account/")
    time.sleep(0.5)
    pyautogui.leftClick(700, 600)
    time.sleep(0.5)
    driver.get("https://www.smelk.dev/account/")
    time.sleep(0.5)
    count += 1


driver.close()