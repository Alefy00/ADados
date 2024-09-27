from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Configuração do WebDriver 
driver = webdriver.Chrome()

# Acessar o site das Casas Bahia
driver.get("https://www.casasbahia.com.br/iphone/b")

# Espera a página carregar completamente
time.sleep(5)

# Função para encontrar dinamicamente os seletores dos produtos
def encontrar_produtos_dinamico():
    produtos = driver.find_elements(By.CSS_SELECTOR, "div")
    
    # procurar por elementos que tenham títulos e preços dentro deles
    dados = []
    
    for produto in produtos:
        try:
            # Procurando possíveis candidatos para o nome do produto
            nome = produto.find_element(By.XPATH, ".//h2 | .//h3 | .//span").text
            
            # Procurando possíveis candidatos para o link
            link = produto.find_element(By.XPATH, ".//a").get_attribute("href")
            
            # Procurando possíveis candidatos para o preço
            preco = produto.find_element(By.XPATH, ".//span[contains(text(), 'R$')]").text

            if nome and link and preco:
                dados.append({
                    "Nome": nome,
                    "Link": link,
                    "Preço": preco
                })
        except Exception as e:
            # Se não encontrar algum desses elementos, ignora e continua
            continue
    
    return dados

# Coletar os dados da página
dados = encontrar_produtos_dinamico()

# Fechar o navegador
driver.quit()

# Criar um DataFrame com os dados coletados e exportar para CSV
df = pd.DataFrame(dados)
df.to_csv('precos_produtos_selenium.csv', index=False)

print("Dados exportados para 'precos_produtos_selenium.csv'")
