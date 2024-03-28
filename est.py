from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_Xpath(driver, wait_time, xpath):
    """Clicks on an element using its Xpath.

    Args:
        driver: The WebDriver object.
        wait_time: The time in seconds to wait for the element to become clickable.
        xpath: The Xpath of the element to be clicked.
    """
    try:
        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()
    except Exception as e:
        print(f"Error clicking on element with Xpath {xpath}: {e}")

