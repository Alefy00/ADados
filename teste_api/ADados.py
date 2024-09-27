import requests
import pandas as pd
import sqlite3
import time
import re
import logging

# Função para carregar a planilha de CNPJs
def carregar_cnpjs(caminho_planilha):
    df = pd.read_excel(caminho_planilha)
    lista_cnpjs = df['CNPJ'].astype(str).tolist()
    return lista_cnpjs

# Função para limpar o CNPJ (remover pontos, barras, traços)
def limpar_cnpj(cnpj):
    return re.sub(r'\D', '', cnpj)

# Função para fazer requisições à API de consulta de CNPJ
def consultar_cnpj(cnpj):
    url = f"https://publica.cnpj.ws/cnpj/{cnpj}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro ao consultar CNPJ {cnpj}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Erro ao conectar à API: {e}")
        return None

# Função para criar e inserir dados no banco SQLite
def criar_e_inserir_banco(cnpj, inscricao_estadual, razao_social, nome_fantasia, logradouro, cep, uf):
    conn = sqlite3.connect('cnpj_consulta.db')
    cursor = conn.cursor()

    # Criação da tabela (se não existir)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_cnpj (
            cnpj TEXT,
            inscricao_estadual TEXT,
            razao_social TEXT,
            nome_fantasia TEXT,
            logradouro TEXT,
            cep TEXT,
            uf TEXT
        )
    ''')

    # Inserção dos dados
    cursor.execute('''
        INSERT INTO dados_cnpj (cnpj, inscricao_estadual, razao_social, nome_fantasia, logradouro, cep, uf)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (cnpj, inscricao_estadual, razao_social, nome_fantasia, logradouro, cep, uf))

    conn.commit()
    conn.close()

# Função para pausar o script conforme limite de requisições (3 requisições por minuto)
def pausar_requisicoes():
    time.sleep(20)  # Pausa por 20 segundos após cada requisição para respeitar o limite

# Carregar os CNPJs
caminho_planilha = "./CNPJ_busca.xlsx"
cnpjs = carregar_cnpjs(caminho_planilha)

# Limpar e processar cada CNPJ
cnpjs = [limpar_cnpj(cnpj) for cnpj in cnpjs]

# Fazer a consulta para cada CNPJ e extrair os campos necessários
for cnpj in cnpjs:
    dados_cnpj = consultar_cnpj(cnpj)
    if dados_cnpj:
        try:
            # Extração dos dados
            inscricao_estadual = dados_cnpj['estabelecimento']['inscricoes_estaduais'][0]['inscricao_estadual'] if dados_cnpj['estabelecimento']['inscricoes_estaduais'] else None
            razao_social = dados_cnpj.get('razao_social', None)
            nome_fantasia = dados_cnpj['estabelecimento'].get('nome_fantasia', None)
            logradouro = dados_cnpj['estabelecimento'].get('logradouro', None)
            cep = dados_cnpj['estabelecimento'].get('cep', None)
            uf = dados_cnpj.get('estabelecimento', {}).get('estado', {}).get('sigla', None)


            # Inserir no banco de dados
            criar_e_inserir_banco(cnpj, inscricao_estadual, razao_social, nome_fantasia, logradouro, cep, uf)
            print(f"Dados para CNPJ {cnpj} inseridos no banco de dados.")
        except Exception as e:
            registrar_erro(cnpj, f"Erro ao inserir no banco: {e}")
    else:
        registrar_erro(cnpj, "Erro ao consultar API")
    
    pausar_requisicoes()

# Função para verificar e listar todos os registros no banco de dados
def listar_dados_banco():
    conn = sqlite3.connect('cnpj_consulta.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM dados_cnpj")
    registros = cursor.fetchall()
    
    for registro in registros:
        print(registro)
    
    conn.close()

# Listar os registros inseridos
listar_dados_banco()

# Configuração do logger
logging.basicConfig(filename='cnpj_consulta.log', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s:%(message)s')

# Função para registrar erros
def registrar_erro(cnpj, mensagem):
    logging.error(f"Erro com CNPJ {cnpj}: {mensagem}")


# Limpar a tabela antes de reinserir os dados (opcional)
def limpar_tabela():
    conn = sqlite3.connect('cnpj_consulta.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dados_cnpj")
    conn.commit()
    conn.close()

# Chamando a função para limpar a tabela
limpar_tabela()


