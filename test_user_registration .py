from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_user_registration():
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    
    # Use a random email so the script doesn't fail if you run it multiple times
    random_email = f"student_tester_{random.randint(1000, 99999)}@example.com"
    
    # Fill registration fields
    driver.find_element(By.ID, "firstname").send_keys("Jane")
    driver.find_element(By.ID, "lastname").send_keys("Smith")
    driver.find_element(By.ID, "email_address").send_keys(random_email)
    driver.find_element(By.ID, "password").send_keys("StrongLabPass123!")
    driver.find_element(By.ID, "password-confirmation").send_keys("StrongLabPass123!")
    
    # Click Create Account
    driver.find_element(By.CSS_SELECTOR, "button[title='Create an Account']").click()
    
    # Verify successful registration message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-bind*='message.text']"))
    )
    assert "Thank you for registering" in success_message.text
    print(f"Q3 Passed: Registration successful with email {random_email}")

test_user_registration()
driver.quit()
