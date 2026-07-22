from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_email_validation():
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    
    # Enter a badly formatted email (missing the @ symbol)
    email_field = driver.find_element(By.ID, "email_address")
    email_field.send_keys("invalid_email_format.com")
    
    # Click on the First Name box to trigger the website's live validation check
    driver.find_element(By.ID, "firstname").click()
    
    # Wait for the specific red warning text to appear directly under the email box
    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "email_address-error"))
    )
    
    assert error_msg.is_displayed()
    assert "Please enter a valid email address" in error_msg.text
    print("Q4 Passed: Email format validation caught the bad input.")

test_email_validation()
driver.quit()
