from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import os
import time


def import_cookies(driver, cookie_file):
    with open(cookie_file, 'r') as cookies:
        for line in cookies:
            if not line.startswith('#') and line.strip():
                domain, _, path, secure, expiry, name, value = line.strip().split('\t')
                secure = True if secure == "TRUE" else False
                cookie_dict = {
                    'domain': domain,
                    'name': name,
                    'value': value,
                    'secure': secure,
                    'path': path
                }
                driver.add_cookie(cookie_dict)


def upload_instagram_post(file_path, description):
    chrome_options = Options()

    # WebDriver inicializálása a headless beállításokkal
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3")
    chrome_options.add_argument("--lang=hu")

    # Itt beállítod a Chrome opciókat, ha szükséges

    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.get("https://www.instagram.com/accounts/login/")
    driver.get("https://instagram.com")
    import_cookies(driver, "cookies_insta.txt")
    driver.get("https://www.instagram.com")

    wait = WebDriverWait(driver, 2)

    try:
        notifications_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Bekapcsolás")]')))
        notifications_button.click()
    except:
        print("Notifications button not found")

    wait = WebDriverWait(driver, 3)

    svg_xpath = '//*[@fill="none"][@stroke="currentColor"][@stroke-linecap="round"][@stroke-linejoin="round"][@stroke-width="2"][@x1="6.545"][@x2="17.455"][@y1="12.001"][@y2="12.001"]'
    svg_element = wait.until(EC.presence_of_element_located((By.XPATH, svg_xpath)))
    ActionChains(driver).move_to_element(svg_element).click().perform()
    print("kész")

    try:
        # Megvárja, míg az elem kattinthatóvá válik
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Bejegyzés')]")))

        # Kattintás az elemen az ActionChains használatával
        ActionChains(driver).move_to_element(element).click().perform()

    except Exception as e:
        print(f"An exception occurred: {str(e)}")

    try:
        button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Kiválasztás a számítógépről")]')))
        button.click()
    except Exception as e:
        print(f"An exception occurred: {str(e)}")

    try:
        upload_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
        video_file_path = os.path.abspath(file_path)
        upload_input.send_keys(video_file_path)
    except Exception as e:
        print(f"An exception occurred while locating file input: {str(e)}")

    time.sleep(1)

    try:
        ok_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="OK"]')))
        ok_button.click()
    except Exception as e:
        print(f"An exception occurred while clicking Ok button: {str(e)}")

    time.sleep(1)

    try:
        next_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Tovább"]')))
        next_button.click()
    except Exception as e:
        print(f"An exception occurred while clicking Next button: {str(e)}")

    time.sleep(1)

    try:
        next_button2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Tovább"]')))
        next_button2.click()
    except Exception as e:
        print(f"An exception occurred while clicking the second Next button: {str(e)}")

    time.sleep(2)

    try:
        content_editable_div = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
        content_editable_div.click()
        content_editable_div.clear()
        content_editable_div.send_keys(description)
    except Exception as e:
        print(f"An exception occurred while handling content editable div: {str(e)}")

    try:
        next_button3 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Megosztás"]')))
        next_button3.click()
    except Exception as e:
        print(f"An exception occurred while clicking the Share button: {str(e)}")

    time.sleep(2)

    try:
        WebDriverWait(driver, 200).until(EC.invisibility_of_element_located((By.XPATH, '//img[@alt="Kör helyőrzője"]')))
        time.sleep(5)
        print("Upload finished")
    except Exception as e:
        print(f"An exception occurred while waiting for the placeholder image to disappear: {str(e)}")

# upload_instagram_post(f"your_video.mp4", "insta_description")
