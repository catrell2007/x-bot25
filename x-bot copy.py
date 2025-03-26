#!/usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--disable-logging")
options.add_experimental_option("detach", True)
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
options.page_load_strategy = 'eager'  # The 'eager' strategy loads DOM first, not waiting for all resources (images, CSS).


# Retrieve website
driver = webdriver.Chrome(options=options)
driver.get("https://www.x.com/")

# Wait for the login button and click
user_login = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
)
user_login.click()

# Wait for username input field to appear and fill it in
user_name = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@autocomplete='username']"))
)
user_name.send_keys("Rbot2024")

# Wait for the next button and click
nxt_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']"))
)
nxt_button.click()

# Wait for password input field to appear and fill it in
pw_button = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
)
pw_button.send_keys("$CSC2024")

# Wait for the login button and click
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='LoginForm_Login_Button']"))
)
login_button.click()

# Wait for the tweet section to become clickable
com_section = WebDriverWait(driver, 900).until(
    EC.element_to_be_clickable((By.XPATH, "//article[@data-testid='tweet']"))
)

# Check for a video component and either click the tweet text or the comment section
if len(driver.find_elements(By.XPATH, "//div[@data-testid='videoComponent']")) > 0:
    tweet_txt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetText']"))
    )
    tweet_txt.click()
else:
    com_section.click()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")






