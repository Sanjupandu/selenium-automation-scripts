from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_user_registration():
    driver.get("https://example.com/register")
    
    # Fill in valid user details
    driver.find_element(By.NAME, "first_name").send_keys("John")
    driver.find_element(By.NAME, "last_name").send_keys("Doe")
    driver.find_element(By.NAME, "email").send_keys("johndoe@example.com")
    driver.find_element(By.NAME, "password").send_keys("SecurePass123!")
    driver.find_element(By.NAME, "confirm_password").send_keys("SecurePass123!")
    
    # Submit registration form
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Verify registration confirmation
    success_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    assert "Registration successful" in success_msg.text
    print("User registration test passed!")

test_user_registration()
driver.quit()