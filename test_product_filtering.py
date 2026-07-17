from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_product_filtering():
    driver.get("https://example.com/products")
    
    # Select category from dropdown
    category_dropdown = Select(driver.find_element(By.ID, "category"))
    category_dropdown.select_by_visible_text("Electronics")
    
    # Enter price range
    driver.find_element(By.ID, "min-price").send_keys("100")
    driver.find_element(By.ID, "max-price").send_keys("500")
    
    # Apply filter
    driver.find_element(By.ID, "filter-btn").click()
    
    # Verify products are listed post-filtering
    filtered_products = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card"))
    )
    assert len(filtered_products) > 0, "No products displayed after applying filter!"
    print("Product filtering test passed!")

test_product_filtering()
driver.quit()
