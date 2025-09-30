from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

cidade = str(input(
    'digite a cidade que você deseja ver a previsão do tempo em até 7 dias:'
)).lower().replace(' ','-')

URL = f"https://www.timeanddate.com/weather/brazil/{cidade}/ext"


def coletar_previsao():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_argument("--log-level=3")    
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(URL)

    wait = WebDriverWait(driver, 10)
    tabela = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.zebra.tb-wt.tb-hover"))
    )

    linhas = tabela.find_elements(By.TAG_NAME, "tr")
    previsao = []

    for linha in linhas[1:9]:
        try:
            dia = linha.find_element(By.CSS_SELECTOR, "th").text.strip()
            if dia.lower() == "day" or dia == "":
                continue
        except:
            continue

        try:
            temp_max_and_min = linha.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text.strip()
        except:
            temp_max_and_min = "N/A"

        try:
            condição = linha.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text.strip()
        except:
            condição = "N/A"

        previsao.append([cidade, dia, temp_max_and_min, condição])

    driver.quit()
    return previsao


def salvar_csv(previsao):
    df = pd.DataFrame(previsao, columns=["Cidade", "Dia", "Temperatura Máx e Min", "Condição"])
    df.to_csv("previsao.csv", index=False, encoding="utf-8")
    print("✅ Dados salvos em previsao.csv")


if __name__ == "__main__":
    dados = coletar_previsao()
    salvar_csv(dados)
