from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://exams.mlrinstitutions.ac.in/")

first = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.ID, "lnkLogins"))
)
first.click()

first = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.ID, "lnkStudent"))
)
first.click()

driver.find_element(By.ID, "txtUserId").send_keys("18R25A0326")
driver.find_element(By.ID, "txtPwd").send_keys("18R25A0326")

first = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.ID, "btnLogin"))
)
first.click()

# first = WebDriverWait(driver, 60).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[3]/table[4]/tbody/tr/td/table/tbody/tr/td[1]/div/nav/ul/li[7]/ul/li[6]/a"))
# )
# first.click()
first = driver.find_element(By.ID, "LinkButton2")
webdriver.ActionChains(driver).move_to_element(first).perform()

second = driver.find_element_by_id("lnkOverallMarks")
second.click()

# query = "google about dileep".replace("google about", "").strip()

# driver = webdriver.Chrome(path)
# driver.get("https://www.google.com/")
# driver.find_element(By.NAME, "q").send_keys(query)
# driver.find_element_by_name("q").send_keys(Keys.ENTER)