from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

def open_registration():
    driver.get("https://stage.pay.pallawan.com/en/auth/register")

def fill_form(email="", password="", confirm="", check_terms=True):
    if email:
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(email)
    if password:
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    if confirm:
        driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(confirm)
    if check_terms:
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//button[text()='Register']").click()

def expect_error(message):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(),'{message}')]"))
        )
        print(f"✅ Error detected: {message}")
    except:
        print(f"❌ Error not found: {message}")

# Test 1: Empty email
open_registration()
fill_form(password="D@ntejerad3", confirm="D@ntejerad3")
expect_error("Please enter a valid email address")

# Test 2: Invalid email format
open_registration()
fill_form(email="invalid@", password="D@ntejerad3", confirm="D@ntejerad3")
expect_error("Invalid email address")

# Test 3: Email too long
open_registration()
long_email = "a" * 300 + "@example.com"
fill_form(email=long_email, password="D@ntejerad3", confirm="D@ntejerad3")
expect_error("Email is too long!")

# Test 4: Empty password
open_registration()
fill_form(email="test@example.com", confirm="D@ntejerad3")
expect_error("Please enter your password")

# Test 5: Short password
open_registration()
fill_form(email="test@example.com", password="123", confirm="123")
expect_error("Must have al least 8 characters including numbers and symbols")

# Test 6: Empty confirm password
open_registration()
fill_form(email="test@example.com", password="D@ntejerad3")
expect_error("Please enter password confirmation")

# Test 7: Mismatched passwords
open_registration()
fill_form(email="test@example.com", password="D@ntejerad3", confirm="WrongPass456!")
expect_error("Password not match!")

# Test 8: Checkbox not selected
open_registration()
fill_form(email="test@example.com", password="D@ntejerad3", confirm="D@ntejerad3", check_terms=False)
expect_error("Please agree to the MiroPay's Terms and Conditions")

driver.quit()
