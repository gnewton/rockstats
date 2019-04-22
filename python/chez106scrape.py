#!/usr/bin/env python

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Start the WebDriver and load the page
options = Options()
options.add_argument("--headless")
wd = webdriver.Chrome(chrome_options=options, executable_path="/usr/bin/chromedriver")
print("Browser Invoked")
# wd = webdriver.Firefox()
wd.get("https://www.1061chez.ca/recently-played/", )

# Wait for the dynamically loaded elements to show up
WebDriverWait(wd, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "song-title")))

# And grab the page HTML source
html_page = wd.page_source
wd.quit()

# Now you can use html_page as you like
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_page)

hello = soup.find(text='Name: ')

lis = soup.findAll('li')

for li in lis:
    #print li
    if "class" in li.attrs:
        if len(li["class"]) == 2 and li["class"][0]=="row" and li["class"][1]=="decibel-border-bottom-color-first":
            print li

#print(soup)
