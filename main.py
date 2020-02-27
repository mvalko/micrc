from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup as bs
from os import listdir
from resources import sitenav

# set working parameters
# url = sitenav.openBox['Computer Parts']
url = 'https://www.microcenter.com/search/search_results.aspx?N=4294966998&prt=clearance'
html = requests.get(url).text

# navigate through location selection 
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath("//select[@name='storeID']/option[@value='075']").click() # <-- navigates drop down and selects NJ
driver.find_element_by_xpath("//input[@name='Change Store']").click() # <-- confirms drop down selection
time.sleep(30) # <-- waits to continue 
page = driver.page_source # <-- passes results to bs
soup = bs(page, 'lxml')

container = soup.findAll()
print(container)

# troubleshooting help
f = open("results.html", "w")
f.write(str(container))
f.close()

driver.close()
driver.quit()