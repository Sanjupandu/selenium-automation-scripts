from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_product_filtering():
    # Go to a broad category page (Men's Tops)
    driver.get("https://magento.softwaretestingboard.com/men/tops-men.html")
    wait = WebDriverWait(driver, 10)
    
    # 1. Filter by Category -> Jackets
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Category']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Jackets')]"))).click()
    
    # Wait for page to reload with filter applied
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='filter-value' and contains(text(), 'Jackets')]")))
    
    # 2. Filter by Price -> $50.00 - $59.99
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Price']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'price=50-60')]"))).click()
    
    # Verify products are shown after applying both filters
    products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))
    assert len(products) > 0, "No products found after filtering!"
    print(f"Q5 Passed: Filtering successful. {len(products)} products found in the $50-$60 Jacket category.")

test_product_filtering()
driver.quit()
