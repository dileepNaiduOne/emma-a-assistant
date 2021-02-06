from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(path, chrome_options=chrome_options)


driver.get("https://pypi.org/project/pyttsx3/")

a = driver.find_element_by_class_name("horizontal-menu__link")
a.click()