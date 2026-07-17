from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_email_format_validation():
    driver.get("https://example.com/register")
    
    email_field = driver.find_element(By.NAME, "email")
    
    # Input invalid email format
    email_field.send_keys("invalidemailformat.com")
    driver.find_element(By.NAME, "password").click()  # Click away to trigger validation
    
    # Check for validation error message
    validation_error = driver.find_element(By.ID, "email-error-msg")
    assert validation_error.is_displayed(), "Email format validation failed to trigger!"
    
    print("Email format validation test passed!")

test_email_format_validation()
driver.quit()
