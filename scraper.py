import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver
# from webdriver_manager.safari import SafariDriverManager

driver = webdriver.Safari()

url = 'https://www.welcometothejungle.com/fr/jobs?refinementList%5Boffices.country_code%5D%5B%5D=FR&query=python&page=1'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


job_elements = soup.find('h4', class_="sc-ERObt neOJH sc-6i2fyx-1 ekEFKi wui-text")
if job_elements:
    job_title = job_elements.get_text()
    print(job_title)
else:
    print("No job found.")

driver.quit()