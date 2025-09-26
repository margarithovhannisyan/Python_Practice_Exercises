from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

click_me_success_message = "You have done a dynamic click"
impressive_success_message = "Impressive"

# Initialization
service = Service("../webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open demoqa.com and Choose Elements category
driver.get("https://demoqa.com")
driver.maximize_window()
elements_category = driver.find_elements(By.XPATH, "//div[@class='card-up']")[0]
elements_category.click()

# Navigate to Buttons
elements_category_button_group = driver.find_element(By.XPATH, "//span[text()='Buttons']")
elements_category_button_group.click()

# Click on Click Me and Verify that it is clicked
button_group_click_me = driver.find_element(By.XPATH, "//button[text()='Click Me']")
button_group_click_me.click()
dynamic_click_message = driver.find_element(By.ID, "dynamicClickMessage").text
assert click_me_success_message == dynamic_click_message, f"Expected '{click_me_success_message}' but got '{dynamic_click_message}'"

# Open a new Tab and click on Impressive radio button and Verify the result
driver.switch_to.new_window("tab")
driver.get("https://demoqa.com/radio-button")
driver.switch_to.window(driver.window_handles[1])
impressive_radio_button = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
impressive_radio_button.click()
impressive_click_message = driver.find_element(By.XPATH, "//span[text()='Impressive']").text
assert impressive_success_message == impressive_click_message, f"Expected '{impressive_success_message}' but got '{impressive_click_message}'"

# Close 2nd tab
driver.close()
driver.switch_to.window(driver.window_handles[0])

# Navigate to Links
elements_category_link_group = driver.find_element(By.XPATH, "//span[text()='Links']")
elements_category_link_group.click()

#  Find all links and print the texts
all_links = driver.find_elements(By.TAG_NAME, "a")
for a in all_links:
    print(a.text)
