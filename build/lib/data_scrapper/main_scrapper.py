
from time import sleep 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path='chrome_driver\chromedriver.exe')

# Navigate to the website you want to scrape
url = 'https://www.babycenter.com/baby-names/list/baby-girl-names-that-start-with-a'
driver.get(url)

sleep(5)