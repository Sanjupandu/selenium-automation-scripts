from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window() # Maximizing helps prevent elements from overlapping
driver.implicitly_wait(10)

def test_shopping_cart():
    # Go to Bags category (no size/color selection needed)
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    wait = WebDriverWait(driver, 15)
    actions = ActionChains(driver)
    
    # Add Item 1 to cart (Hover over item, then click Add to Cart)
    item_1 = driver.find_element(By.XPATH, "(//li[@class='item product product-item'])[1]")
    actions.move_to_element(item_1).perform()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@title='Add to Cart'])[1]"))).click()
    
    # Wait for success message before adding the next one
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-bind*='message.text']")))
    
    # Add Item 2 to cart
    item_2 = driver.find_element(By.XPATH, "(//li[@class='item product product-item'])[2]")
    actions.move_to_element(item_2).perform()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@title='Add to Cart'])[2]"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-bind*='message.text']")))
    
    # Go to Shopping Cart
    driver.get("https://magento.softwaretestingboard.com/checkout/cart/")
    
    # Read initial prices
    price_1 = float(driver.find_element(By.XPATH, "(//td[@class='col price']//span[@class='price'])[1]").text.replace("$", ""))
    price_2 = float(driver.find_element(By.XPATH, "(//td[@class='col price']//span[@class='price'])[2]").text.replace("$", ""))
    
    # Update Quantity of Item 1 to '2'
    qty_box = driver.find_element(By.XPATH, "(//input[@title='Qty'])[1]")
    qty_box.clear()
    qty_box.send_keys("2")
    driver.find_element(By.CSS_SELECTOR, "button[title='Update Shopping Cart']").click()
    
    # Wait a moment for the site's background math (Ajax) to update the subtotal
    time.sleep(3) 
    
    # Verify the new total calculation
    expected_total = (price_1 * 2) + price_2
    
    # Extract the new subtotal from the summary box
    subtotal_text = driver.find_element(By.XPATH, "//td[@data-th='Subtotal']//span[@class='price']").text
    actual_total = float(subtotal_text.replace("$", ""))
    
    assert actual_total == expected_total, f"Math failed! Expected {expected_total}, got {actual_total}"
    print(f"Q6 Passed: Cart updated successfully. New total verified as ${actual_total}")

test_shopping_cart()
driver.quit()
