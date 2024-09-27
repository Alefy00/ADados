
# Projeto de Teste - Automação e API

Este repositório contém dois testes: um teste de **Automação Web** utilizando **Selenium** e um teste de **Integração com API** utilizando **Python**. Ambos os testes demonstram a capacidade de automatizar processos e trabalhar com APIs de maneira eficiente.

## Índice

- [Visão Geral](#visão-geral)
- [Teste de Automação Web](#teste-de-automação-web)
  - [Pré-requisitos](#pré-requisitos)
  - [Instruções de Execução](#instruções-de-execução)
  - [Como Funciona](#como-funciona)
- [Teste de API](#teste-de-api)
  - [Pré-requisitos](#pré-requisitos-api)
  - [Instruções de Execução](#instruções-de-execução-api)
  - [Detalhes do Fluxo](#detalhes-do-fluxo)
- [Conclusão](#conclusão)

## Visão Geral

Este projeto inclui dois scripts principais:
1. **Automação Web**: Automação de navegação e coleta de dados em um site de e-commerce.
2. **Integração com API**: Teste de integração com uma API para envio e recebimento de dados.

---

## Teste de Automação Web

### Objetivo

O objetivo deste teste é automatizar a coleta de informações de produtos (nome, preço e link) de um site de e-commerce (Casas Bahia) utilizando Selenium.

### Pré-requisitos

- Python 3.7 ou superior
- **Selenium** e WebDriver para o navegador (Chrome, Firefox, etc.)
- **Pandas** para manipulação de dados e exportação para CSV

Instalar as bibliotecas necessárias:

```bash
pip install selenium pandas
```

Além disso, é necessário ter o **WebDriver** do navegador instalado e configurado. O WebDriver precisa estar no **PATH** ou o caminho para o WebDriver precisa ser configurado no código.

### Instruções de Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-repositorio/projeto-teste.git
   cd projeto-teste
   ```

2. Execute o script de automação:
   ```bash
   python automacao.py
   ```

### Como Funciona

O script de automação faz o seguinte:
1. Abre o navegador e acessa o site **Casas Bahia**.
2. Realiza uma busca por um produto específico (ex: "Iphone").
3. Coleta o nome, link e preço dos produtos encontrados.
4. Exporta os dados coletados para um arquivo CSV (`precos_produtos_selenium.csv`).

---

## Teste de API

### Objetivo

Este teste envolve a integração com uma API REST, utilizando requisições **POST** e **GET** para realizar operações de leitura e escrita de dados.

### Pré-requisitos

- **Python 3.7** ou superior
- **Requests** para realizar as requisições HTTP
- **Pandas** para manipulação de dados (opcional, se for necessário manipular dados retornados)

Instalar as bibliotecas necessárias:

```bash
pip install requests pandas
```

### Instruções de Execução

1. Clone o repositório (caso ainda não tenha clonado).
   ```bash
   git clone https://github.com/seu-repositorio/projeto-teste.git
   cd projeto-teste
   ```

2. Execute o script de integração com a API:
   ```bash
   python api_integration.py
   ```

### Detalhes do Fluxo

O script de API realiza as seguintes operações:
1. **Requisição POST**: Envia dados para a API. Os dados podem incluir informações como nome, número de telefone, etc.
2. **Requisição GET**: Obtém dados de um endpoint específico e processa a resposta.
3. As respostas são tratadas adequadamente, com validação de erros e confirmação de sucesso.

---

## Conclusão

Este projeto exemplifica dois cenários comuns de automação e integração: a coleta automatizada de dados de um site e a comunicação com uma API REST. Ambos os testes demonstram boas práticas de uso de bibliotecas de Python para automação e manipulação de dados.
