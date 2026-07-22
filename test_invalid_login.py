from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_invalid_login():
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    
    # Enter incorrect credentials
    driver.find_element(By.ID, "email").send_keys("wronguser@example.com")
    driver.find_element(By.ID, "pass").send_keys("BadPassword123!")
    driver.find_element(By.ID, "send2").click()
    
    # Wait for the red error alert to appear at the top of the page
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-bind*='message.text']"))
    )
    
    assert error_message.is_displayed()
    assert "The account sign-in was incorrect" in error_message.text
    print("Q2 Passed: Invalid login error displayed correctly.")

test_invalid_login()
driver.quit()
