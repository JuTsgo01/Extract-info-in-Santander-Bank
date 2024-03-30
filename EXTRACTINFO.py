from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import random
import os


CAMINHO_DOS_CODIGOS_DAS_LOJAS = 'file.txt'
DATA_DE_HOJE = datetime.now()
CALCULANDO_UM_MES_PARA_TRAS = DATA_DE_HOJE - timedelta(days=29)
CALCULANDO_TRES_MESES_PARA_FRENTE = DATA_DE_HOJE + timedelta(days=92)
FORMATANDO_DATA_UM_MES_ATRAS = CALCULANDO_UM_MES_PARA_TRAS.strftime("%d%m%Y")
FORMATANDO_DATA_TRES_MESES_PARA_FRENTE = CALCULANDO_TRES_MESES_PARA_FRENTE.strftime("%d%m%Y")


# Configurações do Chrome e camuflar a automação 
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# WebDriver para o chorme
driver = webdriver.Chrome(options=options)

try:
    # Acessar o site do Santander
    driver.get("https://www.santander.com.br/")

    input("Faça o login manualmente e pressione Enter.") #Input para colocar informações de Login

    # Colocando informações de XPATH para extrair os arquivos
    # For para informar a loja 

    with open(CAMINHO_DOS_CODIGOS_DAS_LOJAS, 'r') as arquivo:
        for linha in arquivo:
            t_conta = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="j_id_4y:iconeTrocaConta"]'))
                    )
            t_conta.click()


            informar_loja = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="j_id_4y:tabelaPerfisConta:globalFilter"]'))
                    )
            informar_loja.click()
            informar_loja.clear()
            informar_loja.send_keys(linha.strip())

            sleep(2)

            selecionar_loja = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="j_id_4y:tabelaPerfisConta_data"]'))
                    )
            
            sleep(4)

            selecionar_loja.click()

            sleep(5)

        #     # Dentro da Loja selecionada, selecionando pagamentos no menu rápido
            
            move_consultar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="formGeral:j_id_5f_7r:1:j_id_5f_7x"]'))
                    )
            ActionChains(driver)\
            .move_to_element(move_consultar)\
            .click(move_consultar)\
            .perform()

            sleep(5)     

            scroll = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="dda-boletos-eletronicos-consultar"]/div/ibe-title-filter-component/section/form/div[1]/div[2]/dss-datepicker/div/div[1]/span'))
                    )
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", scroll)

            data_inicial_consultar_pagamento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/form/div[3]/div/ibe-dda-boletos-eletronicos-consultar-element/div/ibe-title-filter-component/section/form/div[1]/div[2]/dss-datepicker/div/div[1]/input'))
                    )
            
            ActionChains(driver)\
            .move_to_element(data_inicial_consultar_pagamento)\
            .click(data_inicial_consultar_pagamento)\
            .perform()
            data_inicial_consultar_pagamento.send_keys(FORMATANDO_DATA_UM_MES_ATRAS)

            sleep(1)    

            data_final_consultar_pagamento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/form/div[3]/div/ibe-dda-boletos-eletronicos-consultar-element/div/ibe-title-filter-component/section/form/div[1]/div[3]/dss-datepicker/div/div[1]/input'))
                    )
            ActionChains(driver)\
            .move_to_element(data_final_consultar_pagamento)\
            .click(data_final_consultar_pagamento)\
            .perform()
            data_final_consultar_pagamento.send_keys(FORMATANDO_DATA_TRES_MESES_PARA_FRENTE)

            sleep(2)

            botao_confirmar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/form/div[3]/div/ibe-dda-boletos-eletronicos-consultar-element/div/ibe-title-filter-component/section/form/div[4]/div[2]/button'))
                    )
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", botao_confirmar)
            
            ActionChains(driver)\
            .move_to_element(botao_confirmar)\
            .click(botao_confirmar)\
            .perform()

            botao_confirmar.click()

            sleep(40)


except Exception as e:
    print(f"Erro durante a automação: {e}")

finally:
    # Feche o navegador ao finalizar
    driver.quit()
