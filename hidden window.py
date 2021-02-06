from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
#chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver.get("https://www.youtube.com/")
driver.get_screenshot_as_file("capture.png")
driver.close()