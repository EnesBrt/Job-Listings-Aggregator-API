from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import json
import time

# Configuration du logging pour le débogage
logging.basicConfig(level=logging.INFO)

# Initialisation du navigateur
driver = webdriver.Safari()
driver.implicitly_wait(10)  # Attend jusqu'à 10 secondes pour que les éléments soient trouvés

# Ouverture de la page
base_url = 'https://www.welcometothejungle.com/fr/jobs?query=python&refinementList%5Boffices.country_code%5D%5B%5D=FR&page='

jobs = []
    

# Fonction pour extraire les données
def scraping():
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.sc-bXCLTC.iiwBSR"))) 
    job_cards = driver.find_elements(By.CSS_SELECTOR, "div.sc-bXCLTC.iiwBSR")
    
    try:
        
        job_cards = driver.find_elements(By.CSS_SELECTOR, "div.sc-bXCLTC.iiwBSR")
        
        for card in job_cards:
            company_name = card.find_element(By.CSS_SELECTOR, 'span.sc-ERObt.gTCEVh').text
            job_title = card.find_element(By.CSS_SELECTOR, 'div[role="mark"]').text
            job_location = card.find_element(By.CSS_SELECTOR, 'span.sc-68sumg-0').text
            job_type = card.find_element(By.CSS_SELECTOR, 'div.sc-dQEtJz').text
            
            jobs.append({
                'Job Title': job_title if job_title else 'Unspecified',
                'Job Location': job_location if job_location else 'Unspecified',
                'Company Name': company_name if company_name else 'Unspecified',
                'Job Type': job_type if job_type else 'Unspecified'
            })
        
    except:
        logging.info("Aucune annonce d'emploi n'a été trouvée")
      

if __name__ == '__main__':
    
    logging.info("Début du scraping des annonces d'emploi")
    
    for page_number in range(1, 11):
        
        try:
            url = f'{base_url}{page_number}'
            driver.get(url)
            time.sleep(2)
            scraping()
        except TimeoutException as e:
            logging.error(f"Erreur de délai d'attente : {e}")
        except NoSuchElementException as e:
            logging.error(f"Élément non trouvé : {e}")
    
    # Sauvegarde dans un fichier JSON
    with open('jobs.json', 'w') as outfile:
        json.dump(jobs, outfile)
        
    logging.info("Fin du programme")