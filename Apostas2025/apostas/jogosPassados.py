import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def jogosPassado():
    # Configurar o WebDriver com as opções e o serviço
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())

    # Inicializar o primeiro driver
    driver = webdriver.Chrome(service=service, options=options)

    # Inicializar o segundo driver (reutilizando as opções e serviço)
    driverClassificacoes = webdriver.Chrome(service=service, options=options)

    # URL do site
    url = 'https://www.flashscore.pt/equipa/fc-porto/S2NmScGp/resultados/'
    driver.get(url)

    # URL da página de classificações (não utilizada no momento)
    # urlClassificacoes = 'https://www.flashscore.pt/futebol/portugal/liga-portugal/classificacoes/#/0d7EBBWo/live'
    # driverClassificacoes.get(urlClassificacoes)

    # Aumentar o tempo de espera para garantir que todos os elementos sejam carregados
    time.sleep(10)

    # Encontrar os elementos de data, equipe da casa, resultado e equipe visitante
    elementos_data = driver.find_elements(By.XPATH, "//div[@class='event__time']")
    #elementos_casa = driver.find_elements(By.XPATH, "//div[@class='wcl-simpleText_Asp-0 wcl-scores-simpleText-01_pV2Wk wcl-name_N76Hr")
    elementos_casa = driver.find_elements(By.XPATH, "//div[@class='wcl-participant_KglL4 event__homeParticipant']")
    resultados_casa = driver.find_elements(By.XPATH, "//div[@class='event__score event__score--home']")
    resultados_fora = driver.find_elements(By.XPATH, "//div[@class='event__score event__score--away']")
    elementos_fora = driver.find_elements(By.XPATH, "//div[@class='wcl-participant_KglL4 event__awayParticipant']")

    # Imprimir os tamanhos das listas para diagnóstico
    print(f"elementos_data: {len(elementos_data)}")
    print(f"elementos_casa: {len(elementos_casa)}")
    print(f"resultados_casa: {len(resultados_casa)}")
    print(f"resultados_fora: {len(resultados_fora)}")
    print(f"elementos_fora: {len(elementos_fora)}")

    # Verificar se todas as listas têm o mesmo tamanho
    #if len(elementos_data) == len(elementos_casa) == len(resultados_casa) == len(resultados_fora) == len(elementos_fora):
    print("As listas têm todas o mesmo tamanho")
    contarEquipa = 0
    contarGolosCasa = 0
    contarGolosFora = 0

    # Criar listas para armazenar os dados
    datas = []
    casas = []
    resultados_casas = []
    foras = []
    resultados_foras = []

    # Processar os elementos
    for i in range(len(elementos_data)):
        data = elementos_data[i].text
        casa = elementos_casa[i].text
        resultado_casa = int(resultados_casa[i].text) if resultados_casa[i].text.isdigit() else 0
        resultado_fora = int(resultados_fora[i].text) if resultados_fora[i].text.isdigit() else 0
        fora = elementos_fora[i].text

        datas.append(data)
        casas.append(casa)
        resultados_casas.append(resultado_casa)
        foras.append(fora)
        resultados_foras.append(resultado_fora)
        print("Processou os elementos")

        if casa == "FC Porto" or casa == "FC Porto (Por)":
            contarEquipa += 1
            contarGolosCasa += resultado_casa
        if fora == "FC Porto" or fora == "FC Porto (Por)":
            contarGolosFora += resultado_fora

        # Criar um DataFrame
        df = pd.DataFrame({
            'Data': datas,
            'Casa': casas,
            'Resultado Casa': resultados_casas,
            'Resultado Fora': resultados_foras,
            'Fora': foras
        })

        # Exportar para um arquivo Excel
        df.to_excel("jogosPassado.xlsx", index=False)
        print("Dados exportados com sucesso para dados_jogos.xlsx!")

        # Imprimir os contadores
        print(f"Contar Equipa: {contarEquipa}")
        print(f"Contar Golos Casa: {contarGolosCasa}")
        print(f"Contar Golos Fora: {contarGolosFora}")
    else:
        print("Erro: Número de elementos não coincide.")

    # Fechar o navegador
    driver.quit()


# Executar a função
jogosPassado()
