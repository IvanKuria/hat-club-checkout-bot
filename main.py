import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Client information(ALL FAKE)
EMAIL = "johndoe@gmail.com"
FIRST_NAME = "John"
LAST_NAME = "Doe"
ADDRESS = "1234 John Doe Rd"
CARD_NUMBER = "4263982640269299"
CARD_EXPIRATION_DATE = "1226"
SECURITY_CODE = "887"

# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.hatclub.com/products/5950-yankees-asg42-blk-ivy-mcp")

# Initialize ActionChains for typing actions
actions = ActionChains(driver)


# Function for clicking with explicit wait and visibility condition
def smart_click(xpath: str, timeout: int = 10):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.click()


# Function for sending keys normally
def smart_send(xpath: str, key: str, timeout: int = 4):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.send_keys(key)


# Function to type each character using ActionChains
def type_with_action_chains(xpath: str, value: str):
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.click()  # Focus on the element first
    for char in value:
        actions.send_keys(char)
        actions.perform()
        time.sleep(0.3)  # Delay between characters to simulate natural typing


# Clicks on the size
smart_click('//*[@id="ProductForm-template--15628437094475__main7195794341963"]/product-options/div[2]/div/div/div[10]')

# Clicks on the "no, thanks" pop-up(realized if I'm fast enough it doesn't have time to pop up :)
# smart_click('//*[@id="ltkpopup-content"]/div[1]/div[2]/div/div[2]/div/div[2]/div/button', timeout=10)

# Clicks on the "add to cart" button
smart_click('//*[@id="ProductForm-template--15628437094475__main7195794341963"]/div[2]/button', timeout=1)

# Clicks on the "checkout" button
smart_click('//*[@id="AjaxCartTemplate"]/form/footer/button', timeout=1)

# Fills in the credit card info using ActionChains for expiration date and security code
smart_send(xpath='//*[@id="number"]', key=CARD_NUMBER)
type_with_action_chains(xpath='//*[@id="expiry"]', value=CARD_EXPIRATION_DATE)
type_with_action_chains(xpath='//*[@id="verification_value"]',
                        value=SECURITY_CODE)

# Fills in the contact info
smart_send(xpath='//*[@id="email"]', key=EMAIL)

# Fills in the address info
smart_send(xpath='//*[@id="TextField0"]', key=FIRST_NAME)
smart_send(xpath='//*[@id="TextField1"]', key=LAST_NAME)
smart_send(xpath='//*[@id="shipping-address1"]', key=ADDRESS)
smart_click(xpath='//*[@id="shipping-address1-option-0"]', timeout=10)  # Google auto-generated address
