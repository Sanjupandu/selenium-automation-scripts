from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_invalid_login():
    driver.get("https://example.com/login")
    
    # Enter invalid login credentials
    driver.find_element(By.ID, "username").send_keys("invaliduser")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "login-btn").click()
    
    # Verify the error message is displayed
    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error-message"))
    )
    
    assert error_element.is_displayed(), "Error message was not displayed!"
    print("Invalid login test passed!")

test_invalid_login()
driver.quit()
