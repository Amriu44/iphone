from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
load_mrore_buttons_clicked = 0
# === Chrome options ===
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--log-level=3")  # Suppress logs

# === Start WebDriver ===
service = Service(log_path="NUL")
driver = webdriver.Chrome(service=service, options=chrome_options)

# === Open Divar iPhone search page ===
driver.get("https://divar.ir/s/tehran/mobile-phones?q=ایفون")

# === Collect product links where class = 'kt-post-card__action' ===
product_links = set()
last_height = driver.execute_script("return document.body.scrollHeight")
LOAD_MORE_BUTTON_XPATH = '//*[@id="post-list-container-id"]/div[2]/div/button'
while True:
    links = driver.find_elements(By.CSS_SELECTOR, 'a.kt-post-card__action')
    for link in links:
        href = link.get_attribute('href')
        if href:
            product_links.add(href)

    # Scroll down to load more untinl 20 load more buttons are clicked
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height :
        driver.find_element(By.XPATH, LOAD_MORE_BUTTON_XPATH).click() 
        time.sleep(5)
        load_mrore_buttons_clicked = load_mrore_buttons_clicked+1
        if load_mrore_buttons_clicked == 2:
            break
    
    last_height = new_height

driver.quit()
