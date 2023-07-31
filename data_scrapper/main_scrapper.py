from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Replace 'url_here' with the URL of the webpage you want to scrape
url = 'https://www.babycenter.com/baby-names'

# Set up ChromeOptions to run the browser in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Start the WebDriver and load the page
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Function to click "See More" for a given letter
def click_see_more(letter):
    xpath = f'//div[@class="seeMoreWrapper" and text()="{letter}"]'
    see_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    see_more_button.click()

# Function to extract href attributes from the divs
def extract_hrefs(names_list):
    hrefs = []
    for name_div in names_list:
        divs_with_href = name_div.find_all('div', class_='name textLinks')
        hrefs.extend([div.a['href'] for div in divs_with_href if div.a and div.a.has_attr('href')])
    return hrefs

# Extract hrefs for girl names and boy names from 'a' to 'z'
all_hrefs_girls = []
all_hrefs_boys = []

for letter in "abcdefghijklmnopqrstuvwxyz":
    click_see_more(letter)
    soup
