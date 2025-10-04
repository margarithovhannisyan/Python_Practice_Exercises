from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialization
service = Service("../webdrivers/chromedriver.exe")
send_data = "Maga"
cancel = "Cancel"

# Test case 1
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://demoqa.com/frames")
    frame1 = driver.find_element(By.ID, "frame1")
    driver.switch_to.frame(frame1)
    frame_text = driver.find_element(By.ID, "sampleHeading").text
    print(f"TC1 iFrame text:{frame_text}")
    driver.switch_to.default_content()
    driver.get("https://demoqa.com/alerts")
    timed_alert_button = driver.find_element(By.ID, "timerAlertButton")
    timed_alert_button.click()
    sleep(5)
    alert = driver.switch_to.alert
    alert.accept()
    print("1st Test Case : Success")
finally:
    driver.quit()

# Test case 2
    driver = webdriver.Chrome(service=service)
try:
    driver.get("https://demoqa.com/browser-windows")
    first_tab = driver.current_window_handle
    driver.switch_to.new_window("tab")
    driver.get("https://demoqa.com/alerts")
    alertButton = driver.find_element(By.ID, "alertButton")
    alertButton.click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.switch_to.window(first_tab)
    print("2nd Test Case : Success")
finally:
    driver.quit()

# Test case 3
    driver = webdriver.Chrome(service=service)
try:
    driver.get("https://demoqa.com/browser-windows")
    first_tab = driver.current_window_handle
    new_window = driver.find_element(By.ID, "windowButton")
    new_window.click()
    driver.switch_to.window(driver.window_handles[1])
    new_window_text = driver.find_element(By.ID, "sampleHeading").text
    print(f"TC3 New Window Text: {new_window_text}")
    driver.switch_to.window(first_tab)
    first_tab_title = driver.title
    print(f"TC3 First Tab Title: {first_tab_title}")
    print("3rd Test Case : Success")
finally:
    driver.quit()

# Test case 4
    driver = webdriver.Chrome(service=service)
try:
    driver.get("https://demoqa.com/frames")
    frame1 = driver.find_element(By.ID, "frame1")
    driver.switch_to.frame(frame1)
    frame1_text = driver.find_element(By.ID, "sampleHeading").text
    driver.switch_to.default_content()
    frame2 = driver.find_element(By.ID, "frame2")
    driver.switch_to.frame(frame2)
    frame2_text = driver.find_element(By.ID, "sampleHeading").text
    driver.switch_to.default_content()
    print("TC 4 iframe task completed.")
    print("4th Test Case : Success")
finally:
    driver.quit()

# Test case 5
    driver = webdriver.Chrome(service=service)
try:
    driver.get("https://demoqa.com/alerts")
    alertButton = driver.find_element(By.ID, "alertButton")
    alertButton.click()
    driver.switch_to.alert.accept()
    confirmButton = driver.find_element(By.ID, "confirmButton")
    confirmButton.click()
    driver.switch_to.alert.dismiss()
    dismissed_data = driver.find_element(By.ID, "confirmResult").text
    print(f"TC5 Dismissed Data: {dismissed_data}")
    assert dismissed_data.split()[-1] == cancel, f"Expected '{cancel}' but got '{dismissed_data}'"
    promtButton = driver.find_element(By.ID, "promtButton")
    promtButton.click()
    promtAlert = driver.switch_to.alert
    promtAlert.send_keys(send_data)
    promtAlert.accept()
    received_data = driver.find_element(By.ID, "promptResult").text
    print(f"TC5 Received Data: {received_data}")
    assert received_data.split()[-1] == send_data, f"Expected '{send_data}' but got '{received_data}'"
    print("5th Test Case : Success")
finally:
    driver.quit()
