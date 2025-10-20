import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://stage.pay.pallawan.com/en/auth/login")

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Email']"))
    ).send_keys("kimiyaleto@gmail.com")

    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("D@ntejerad3")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    # Optional: handle 2FA if needed
    try:
        code_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder,'code')]"))
        )
        code_input.send_keys("YOUR_CODE_HERE")  # Replace with actual code or pyotp
        driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
    except:
        pass

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Account Summary')]"))
    )
    assert "dashboard" in driver.current_url

def test_user_identity(driver):
    assert driver.find_element(By.XPATH, "//div[contains(text(),'Naein Mahmoudi')]")
    assert driver.find_element(By.XPATH, "//div[contains(text(),'pmdevinfo@gmail.com')]")

def test_sidebar_menu(driver):
    items = ["Home", "Payment Links", "Payments", "Withdrawal", "Products", "Account"]
    for item in items:
        assert driver.find_element(By.XPATH, f"//span[contains(text(),'{item}')]")

def test_account_summary(driver):
    assert driver.find_element(By.XPATH, "//div[contains(text(),'2 Payment Links')]")
    assert driver.find_element(By.XPATH, "//div[contains(text(),'27 Payments')]")
    assert driver.find_element(By.XPATH, "//div[contains(text(),'1 Withdrawal')]")

def test_contract_warning(driver):
    assert driver.find_element(By.XPATH, "//div[contains(text(),'You Have No Active Contract')]")

def test_payment_link_button(driver):
    assert driver.find_element(By.XPATH, "//button[contains(text(),'Create Payment Link +')]")

def test_recommendations(driver):
    assert driver.find_element(By.XPATH, "//div[contains(text(),'Recommendations')]")
    assert driver.find_element(By.XPATH, "//div[contains(text(),'Embed a payment link')]")

def test_activity_timeline(driver):
    entries = driver.find_elements(By.XPATH, "//div[contains(text(),'Windows, Chrome, desktop')]")
    assert len(entries) >= 1
