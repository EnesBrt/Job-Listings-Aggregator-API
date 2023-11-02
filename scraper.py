from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)

# Configure Selenium avec Safari
driver = webdriver.Safari()

# URL de départ
url = 'https://fr.indeed.com/jobs?q=Python&fromage=1&vjk=1b833041c0b8707f'
driver.get(url)

jobs = []

 # Obtient le code source de la page actuelle
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Trouvez toutes les cartes de travail sur la page actuelle
job_cards = soup.find_all('td', class_='resultContent')


# Récolte les informations ce charque card
def extract_jobs(job_cards):

    try:
        for card in job_cards:
            job_title = card.find('h2', {'class': 'jobTitle'}).get_text(strip=True)
            company_name_element = card.find('span', {'data-testid': 'company-name'})
            location_element = card.find('div', {'data-testid': 'text-location'})
            job_type_element = card.find('div', {'data-testid': 'attribute_snippet_testid'})

            jobs.append({
                'Job Title': job_title if job_title else 'Non spécifié',
                'Company Name': company_name_element.get_text(strip=True) if company_name_element else 'Non spécifié',
                'Location': location_element.get_text(strip=True) if location_element else 'Non spécifié',
                'Job Type': job_type_element.get_text(strip=True) if job_type_element else 'Non spécifié'
            })
            
    except NoSuchElementException:
        print('Element not found')

    finally:
        driver.quit()


if __name__ == '__main__':
    
    logging.info('Starting scraper...')
    
    extract_jobs(job_cards)
    
    # Affiche ou traite les emplois extraits
    for job in jobs:
        print(job)
    
    logging.info('Scraper finished.')