from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Step 1: Open registration page
    driver.get("https://stage.pay.pallawan.com/en/auth/register")

    # Step 2: Wait for and fill email field (placeholder="Email")
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']"))
    )
    email_input.clear()
    email_input.send_keys("kimiyaleto@yahoo.com")

    # Step 3: Fill password field (placeholder="Password")
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_input.clear()
    password_input.send_keys("D@ntejerad3")

    # Step 4: Fill confirm password field (placeholder="Confirm Password")
    confirm_input = driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']")
    confirm_input.clear()
    confirm_input.send_keys("D@ntejerad3")

    # Step 5: Click Terms and Conditions checkbox
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()

    # Step 6: Click Register button
    register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
    register_button.click()

    # Step 7: Wait for redirect or confirmation
    WebDriverWait(driver, 10).until(
        EC.url_changes("https://pay.pallawan.com/en/auth/register")
    )
    print("✅ Registration submitted successfully!")


except Exception as e:
    print("❌ Test failed:", e)

finally:
    driver.quit()




