from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

# Configuration du logging pour le débogage
logging.basicConfig(level=logging.INFO)

# Configurez Safari pour qu'il soit utilisé avec le WebDriver
driver = webdriver.Safari()
driver.implicitly_wait(10)  # Attend jusqu'à 10 secondes pour que les éléments soient trouvés


url = 'https://www.welcometothejungle.com/fr/jobs?query=Python'
driver.get(url)

# Attendez que les cartes d'emploi soient chargées
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.sc-bXCLTC.iiwBSR"))
)

# Utilisez Selenium pour obtenir les informations plutôt que BeautifulSoup
job_cards = driver.find_elements(By.CSS_SELECTOR, "div.sc-bXCLTC.iiwBSR")

jobs = []
    

def scraping(job_cards):
    
    try:
        for card in job_cards:
            company_name = card.find_element(By.CSS_SELECTOR, 'span.sc-ERObt.gTCEVh').text
            job_title = card.find_element(By.CSS_SELECTOR, 'div[role="mark"]').text
            job_location = card.find_element(By.CSS_SELECTOR, 'span.sc-68sumg-0').text
            job_type = card.find_element(By.CSS_SELECTOR, 'div.sc-dQEtJz').text
            
            jobs.append({
                'Company Name': company_name if company_name else 'Unspecified',
                'Job Title': job_title if job_title else 'Unspecified',
                'Job Location': job_location if job_location else 'Unspecified',
                'Job Type': job_type if job_type else 'Unspecified'
            })

    except TimeoutException:
        logging.info("Le délai d'attente pour charger la page ou les éléments a été dépassé")
    except NoSuchElementException:
        logging.info("Un élément n'a pas été trouvé sur la page")
    finally:
        driver.quit()


if __name__ == '__main__':
    
    logging.info("Scraping des annonces d'emploi")
    
    scraping(job_cards)

    if jobs:
        for job in jobs:
            print(job)
    else:
        logging.info("Aucune annonce d'emploi n'a été trouvée")
    
    logging.info("Fin du programme")
