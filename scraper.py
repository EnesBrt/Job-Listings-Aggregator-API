import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver
# from webdriver_manager.safari import SafariDriverManager

driver = webdriver.Safari()

url = 'https://fr.indeed.com/jobs?q=Python&l=&from=searchOnHP&vjk=61067fdaf7f84d71'
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

jobs = []

job_cards = soup.find_all('td', class_='resultContent')

    # Iterate through each job card and scrape the required information
for card in job_cards:
    
    job_title = card.find('h2', class_='jobTitle').get_text(strip=True)
    
    company_name_element = card.find('span', {'data-testid': 'company-name'})
    company_name = company_name_element.get_text(strip=True) if company_name_element else 'Non spécifié'
    
    location_element = card.find('div', {'data-testid': 'text-location'})
    location = location_element.get_text(strip=True) if location_element else 'Non spécifié'
    
    job_type_element = card.find('div', {'data-testid': 'attribute_snippet_testid'})
    job_type = job_type_element.get_text(strip=True) if job_type_element else 'Non spécifié'
    jobs.append({
        'Job Title': job_title,
        'Company Name': company_name,
        'Location': location,
        'Job Type': job_type
    })

# Don't forget to close the browser once done
driver.quit()

# At this point, `jobs` is a list of dictionaries with the scraped data from each job card
for job in jobs:
    print(job)