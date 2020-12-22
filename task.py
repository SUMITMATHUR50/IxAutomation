from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from datetime import date,timedelta


driver=webdriver.Chrome()

driver.get("https://www.ixigo.com")
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[6]/div/nav/span[2]/span").click()
elem=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[6]/div/div/div[1]/div/div[1]/input").click()
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("enter")
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/button").click()
# dep=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[6]/div/div/div[4]/div/div[1]/div/input").click()

# driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/table/tbody/tr[5]/td[4]").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/table/tbody/tr[2]/td[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[6]/div/div/div[5]/div/div[2]/div[1]/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[6]/div/div/div[6]/button/div").click()





