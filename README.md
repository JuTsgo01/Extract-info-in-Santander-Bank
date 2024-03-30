
# Automação de Extração de Relatórios do Santander

## Descrição:


Este script Python automatiza o processo de extração de relatórios de  pagamentos no website do Santander. Ele foi projetado para acessar a página do banco, fazer login manualmente, e em seguida, consultar e extrair os relatórios de pagamentos de algumas lojas. Os números de indentificação das lojas são obtidos através de uma lista de lojas fornecida em um arquivo de texto.


## Requisitos:

- **Python 3.x**
- **Selenium**
- **WebDriver para o Chrome**

## Funcionalidades:

1. **Configuração do Driver:** Configuração do WebDriver para o navegador Chrome, com camuflagem de automação para evitar detecção.

2. **Login Manual:** O usuário é solicitado a fazer login manualmente no site do Santander.

3. **Consulta de Pagamentos:** O script consulta os pagamentos para cada loja listada no arquivo de texto, definindo um intervalo de datas para a consulta.

## Como Usar:

**1-** Clone este repositório em sua máquina local.

**2-** Instale as dependências necessárias executando pip install -r requirements.txt.

**3-** Edite o arquivo COD MOM.txt para incluir os códigos das lojas que deseja consultar.

**4-** Execute o script Python santander_payment_automation.py.

**5-** Siga as instruções para fazer login manualmente no site do Santander quando solicitado.

## *Observação*

Certifique-se de ter o WebDriver adequado para o Chrome configurado e acessível no seu sistema.

# Santander Report Extraction Automation

## Description:

This Python script automates the process of extracting payment reports from the Santander website. It was designed to access the bank page, log in manually, and then consult and extract payment reports from some stores. Store identification numbers are obtained from a list of stores provided in a text file.

## Requirements:

- **Python 3.x**

- **Selenium**

- **Chrome WebDriver**

## Features:

1- **Driver Configuration:** Configuration of the WebDriver for the Chrome browser, with automation evasion to avoid detection.

2- **Manual Login:** User prompted to manually log in to the Santander website.

3- **Payment Query:** The script queries payments for each store listed in the text file, setting a date range for the query.

## How to Use:

**1-** Clone this repository to your local machine.

**2-** Install the necessary dependencies by running pip install -r requirements.txt.

**3-** Edit the COD MOM.txt file to include the codes of the stores you want to query.

**4-** Run the santander_payment_automation.py Python script.

**5-** Follow the instructions to manually log in to the Santander website when prompted.

## *Notes:*

Ensure you have the appropriate Chrome WebDriver configured and accessible on your system.


