from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_shopping_cart_operations():
    driver.get("https://example.com/products")
    
    # Add Product 1 & Product 2 to shopping cart
    driver.find_element(By.XPATH, "(//button[text()='Add to Cart'])[1]").click()
    driver.find_element(By.XPATH, "(//button[text()='Add to Cart'])[2]").click()
    
    # Go to Shopping Cart page
    driver.find_element(By.ID, "cart-icon").click()
    
    # Verify total cart calculation
    price_1 = float(driver.find_element(By.ID, "item-1-price").text.replace("$", ""))
    price_2 = float(driver.find_element(By.ID, "item-2-price").text.replace("$", ""))
    expected_total = price_1 + price_2
    
    actual_total = float(driver.find_element(By.ID, "cart-total").text.replace("$", ""))
    assert actual_total == expected_total, "Cart total calculation is inaccurate!"
    
    # Update Product 1 Quantity to 2
    qty_input = driver.find_element(By.ID, "item-1-qty")
    qty_input.clear()
    qty_input.send_keys("2")
    driver.find_element(By.ID, "update-cart-btn").click()
    
    # Verify updated quantity & new total calculation
    new_expected_total = (price_1 * 2) + price_2
    new_actual_total = float(driver.find_element(By.ID, "cart-total").text.replace("$", ""))
    assert new_actual_total == new_expected_total, "Cart total failed to recalculate!"
    
    print("Shopping cart operations test passed!")

test_shopping_cart_operations()
driver.quit()
