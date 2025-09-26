from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

expected_title = "ArmSTQB"
expected_url = "https://www.armstqb.org/partners"


def test_title_and_url(driver):
    try:
        driver.get("https://www.armstqb.org")
        driver.maximize_window()
        actual_title = driver.title

        # Verify Title
        assert actual_title == expected_title, f"Expected '{expected_title}' but got '{actual_title} on {driver.name}'"
        print(f"Test Passed: Title matches on {driver.name}")

        driver.switch_to.new_window("tab")
        driver.get("https://www.armstqb.org/partners")
        actual_url = driver.current_url

        # Verify new URL
        assert actual_url == expected_url, f"Expected '{expected_title}' but got '{actual_title} on {driver.name}"
        print(f"Test Passed: URL matches on {driver.name}")

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.minimize_window()

    finally:
        driver.quit()


# Initialize Chrome
chrome_service = ChromeService("../webdrivers/chromedriver.exe")
chrome_driver = webdriver.Chrome(service=chrome_service)
test_title_and_url(chrome_driver)

# # Initialize Edge
edge_service = EdgeService("../webdrivers/msedgedriver.exe")
edge_driver = webdriver.Edge(service=edge_service)
test_title_and_url(edge_driver)

# Initialize Firefox
firefox_service = FirefoxService("../webdrivers/geckodriver.exe")
firefox_driver = webdriver.Firefox(service=firefox_service)
test_title_and_url(firefox_driver)
