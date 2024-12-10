import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def classificacao():
    # Configurar o WebDriver
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # URL do site da classificação da Liga Portugal
    url = 'https://www.flashscore.pt/futebol/portugal/liga-portugal/classificacoes/#/0d7EBBWo/live'
    driver.get(url)

    # Aumentar o tempo de espera para garantir que todos os elementos sejam carregados
    time.sleep(10)
    
    # Capturar os nomes das equipas
    #elementos_classificacao = driver.find_elements(By.XPATH, "//div[@class = 'tableCellParticipant__name']")
    elementos_classificacao = driver.find_elements(By.XPATH, "//div[@class = 'tableCellParticipant']")
    classificacao = []
    
    for i in range(len(elementos_classificacao)):
        classificacoes = elementos_classificacao[i].text
        classificacao.append(classificacoes)
    
    # Criar um DataFrame com os dados
    df = pd.DataFrame({
        'Equipa': classificacao,
        #'Pontos': pontos_equipas
    })
   
    print(len(classificacao))


    # Exportar para um arquivo Excel
    df.to_excel("classificacao_liga_portugal.xlsx", index=False)

# Executar a função
#classificacao()
