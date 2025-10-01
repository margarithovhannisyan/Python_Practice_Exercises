from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialization
service = Service("../webdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Go to Text Box page, Find the element of Full name field. Using parent::, select its parent <div>. Print the class name of that parent.
driver.get("https://demoqa.com/text-box")
parent_class_name = driver.find_element(By.XPATH, "//input[@id='userName']/parent::div")
print(parent_class_name.get_attribute("class"))

# Go to Radio Button page. Locate radio button Yes. Use following-sibling::label to select its label text. Print the label text (Yes).
driver.get("https://demoqa.com/radio-button")
sibling_label = driver.find_element(By.XPATH, "//input[@id='yesRadio']/following-sibling::label")
print(sibling_label.text)

# Go to Check Box page → https://demoqa.com/checkbox. Find the element with text Home. Use following::span to get all nodes after it. Print the count of the following span elements.
driver.get("https://demoqa.com/checkbox")
count_of_following_span = driver.find_elements(By.XPATH, "//span[text()='Home']/following::span")
print(len(count_of_following_span))
