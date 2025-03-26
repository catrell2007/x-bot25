#! /usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common. by import By
import time 
import vader
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
# options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
# prefs = {"profile.managed_default_content_settings.images": 1}
# options.add_experimental_option("prefs", prefs)
options.headless = True 
options.add_experimental_option("detach", True)

# timeout = time.wait(3)

#added a little bit

# retrieve website
options = options
driver = webdriver.Chrome(options)
driver.get("https://www.x.com/")
time.sleep(25)

user_login = driver.find_element(
    By.XPATH, "//a[@href='/login']"
)
user_login.click()
time.sleep(10)

# fill in username
user_name = driver.find_element(
    By.XPATH, "//input[@autocomplete='username']"
)
user_name.click()
user_name.send_keys("Rbot2024")
time.sleep(5)

# next button
nxt_button = driver.find_element(
    By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']"
)
nxt_button.click()
time.sleep(5)

# fill in password
pw_button = driver.find_element(
    By.XPATH, "//input[@name='password']"
)
pw_button.click()
pw_button.send_keys("$CSC2024")

time.sleep(3)

# login to x!
pw_button = driver.find_element(
    By.XPATH, "//button[@data-testid='LoginForm_Login_Button']"
)
pw_button.click()




com_section = WebDriverWait(driver, 900).until(
    EC.element_to_be_clickable((By.XPATH, "//article[@data-testid='tweet']"))
)


if len(driver.find_elements(By.XPATH, "//div[@data-testid='videoComponent']")) > 0:
    tweet_txt = driver.find_element(
        By.XPATH, "//div[@data-testid='tweetText']")
    tweet_txt.click()
else:
        com_section.click()

def reportCom():
    menu = driver.find_element(By.XPATH, "//button[@data-testid='caret']")
    menu.click()
    time.sleep(5)
    report = driver.find_element(By.XPATH, "//div[@data-testid='report']")
    report.click()
    time.sleep(3)
    bubble = driver.find_element(By.XPATH, "//input[@aria-posinset='1']")
    bubble.click()
    nxt = driver.find_element(By.XPATH, "//button[@data-testid='ChoiceSelectionNextButton']")
    nxt.click()
    bubble2 = driver.find_element(By.XPATH, "//input[@aria-posinset='3']")
    bubble2.click()
    done = driver.find_element(By.XPATH, "//button[@data-testid='ocfSettingsListNextButton']")
    done.click()




    





















