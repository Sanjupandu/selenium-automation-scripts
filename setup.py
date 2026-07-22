from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_contact_form():
    driver.get("https://magento.softwaretestingboard.com/contact/")
    
    # Fill out the contact form
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
    driver.find_element(By.ID, "telephone").send_keys("555-123-4567")
    driver.find_element(By.ID, "comment").send_keys("Hello, this is a test message for the lab.")
    
    # Submit the form
    driver.find_element(By.CSS_SELECTOR, "button[title='Submit']").click()
    
    # Verify the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-bind*='message.text']"))
    )
    assert "Thanks for contacting us" in success_message.text
    print("Q1 Passed: Contact form submitted successfully.")

test_contact_form()
driver.quit()
