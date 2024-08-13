from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Configurazione di Selenium con Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Esegui Chrome in modalità headless, senza GUI
chrome_options.add_argument("--disable-gpu")

# Inserisci qui il path al ChromeDriver
chrome_service = Service('C:\\Users\\krist\\OneDrive\\Desktop\\Uni\\Tesi\\chromedriver.exe')

# Inizializza il driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.quit()

df = pd.read_csv('merged.csv', encoding='latin1', low_memory=False)
df_cleaned = df.dropna(subset=['url'])

print(df_cleaned['url'])

'''
try:
    # Vai al sito
    driver.get("https://notegpt.io/youtube-video-summarizer")

    # Trova la casella di testo per l'URL del video di YouTube
    video_url_box = driver.find_element(By.CLASS_NAME, "el-input__inner")

    # Inserisci l'URL del video di YouTube
    video_url = "https://www.youtube.com/watch?v=oKJgWfALwwI&t=1047s"  # Modifica con l'URL del video desiderato
    video_url_box.send_keys(video_url)
    video_url_box.send_keys(Keys.ENTER)

    # Aspetta che il contenuto venga caricato
    time.sleep(15)

    # Trova il pulsante "Copy"
    copy_button = driver.find_element(By.CSS_SELECTOR, ".el-icon-copy-document")

    # Clicca sul pulsante "Copy"
    copy_button.click()

    # Recupera il testo copiato (il contenuto degli appunti)
    transcript = driver.execute_script("return navigator.clipboard.readText();")

    # Stampa il testo o salvalo su file
    print("Transcript copiato:\n", transcript)

finally:
    # Chiudi il browser
    driver.quit()
'''