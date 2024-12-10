import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def jogosFuturo():
    # Configurar o WebDriver
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # URL do site
    url = 'https://www.flashscore.pt/equipa/fc-porto/S2NmScGp/'
    driver.get(url)
    
    # Aumentar o tempo de espera para garantir que todos os elementos sejam carregados
    time.sleep(10)
    
    # Encontrar os elementos de data, equipe da casa, resultado e equipe visitante
    elementos_data = driver.find_elements(By.XPATH, "//div[@class='event__time']")
    elementos_casa = driver.find_elements(By.XPATH, "//div[@class='wcl-participant_KglL4 event__homeParticipant']")
    elementos_fora = driver.find_elements(By.XPATH, "//div[@class='wcl-participant_KglL4 event__awayParticipant']")
    elementos_liga = driver.find_elements(By.XPATH, "//div[@class='wcl-link_bLtj3 wcl-linkBase_CdaEq wcl-primary_C2HA0 wclLeagueHeader__textColor")
    #elementos_classificacao = driver.find_elements(By.XPATH, "//div[@class = 'tableCellParticipant__name']")


    # Imprimir os tamanhos das listas para diagnóstico
    print(f"elementos_data: {len(elementos_data)}")
    print(f"elementos_casa: {len(elementos_casa)}")
    print(f"elementos_fora: {len(elementos_fora)}")
    
    # Verificar se todas as listas têm o mesmo tamanho
    
    # Criar listas para armazenar os dados
    datas = []
    casas = []
    foras = []
    #ligas = []

    # Processar os elementos
    for i in range(len(elementos_data)):
        data = elementos_data[i].text
        casa = elementos_casa[i].text
        fora = elementos_fora[i].text
        #liga = elementos_liga[i].text
        
        datas.append(data)
        casas.append(casa)
        foras.append(fora)
        #ligas.append(liga)
        # classificacao_geral.append(classificacao)
        
    
    # Criar um DataFrame com os dados
    df = pd.DataFrame({
        'Data': datas,
        #'Liga': ligas,
        'Casa': casas,
        'Fora': foras
        #'Classificacao': classificacao_geral
    })
    
    # Exportar para um arquivo Excel
    df.to_excel("jogosFuturo.xlsx", index=False)
    print("Dados exportados com sucesso para jogosFuturo.xlsx!")
    
    # Imprimir os contadores
    #print(f"Contar Equipa: {contarEquipa}")
        

    
    # Fechar o navegador
    driver.quit()

# Executar a função
jogosFuturo()
