from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER_PATH = 'chromedriver.exe'

def get_transcript_from_youtube(url):
    if not url.startswith("https://www.youtube.com/watch"):
        raise ValueError("Invalid YouTube URL")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://anthiago.com/transcript/")

        url_input = driver.find_element(By.ID, "url_input")
        url_input.send_keys(url)

        boton_desgrabar = driver.find_element(By.ID, "boton_desgrabar")
        boton_desgrabar.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#result a"))
        )   
        result_div = driver.find_element(By.ID, "result")
        transcript_text = result_div.text

    finally:
        driver.quit()

    return transcript_text