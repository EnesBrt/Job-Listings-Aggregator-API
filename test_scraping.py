from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import json
import time

# Configuration du logging pour le débogage
logging.basicConfig(level=logging.INFO)

# Fonction pour extraire les données
def scraping(driver, base_url):
    jobs = []

    for page_number in range(1, 11):
        try:
            url = f'{base_url}{page_number}'
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.sc-bXCLTC.iiwBSR")))
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
            time.sleep(2)
        except TimeoutException as e:
            logging.error(f"Timeout Error: {e}")
        except NoSuchElementException as e:
            logging.error(f"Element Not Found: {e}")
        except Exception as e:
            logging.error(f"General Error: {e}")

    # Sauvegarde dans un fichier JSON
    with open('jobs.json', 'w') as outfile:
        json.dump(jobs, outfile)

    return jobs  # Retourne les jobs collectés

if __name__ == '__main__':
    logging.info("Début du scraping des annonces d'emploi")
    
    driver = webdriver.Safari()
    driver.implicitly_wait(10)
    base_url = 'https://www.welcometothejungle.com/fr/jobs?query=python&refinementList%5Boffices.country_code%5D%5B%5D=FR&page='
    scraping(driver, base_url) 
    driver.quit()
    logging.info("Fin du programme")
