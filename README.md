# API Saúde Mental

---

Esta API é parte do projeto Engenharia Inteligente de Dados do CEULP/ULBRA. A aplicação oferece métodos de consultas personalizadas em uma base de dados MongoDB, além de outras informações como listas e dados númericos.

## Dependências

Para a construção da aplicação foram utilizados os seguintes itens: 

* Flask
* Flask-Cors
* Python
* Pymongo
* Dnspython
* Jsonify
* Json_utils

As especificações sobre a versão do framework, linguagem de programação e dos pacotes estão detalhados no arquivo `requirements.txt`

Para consumir as informações forneceidas pela API basta acessar o link: [api-saude-mental](https://api-saude-mental.herokuapp.com).

## Documentação

A [documentação](docs/readme.md) apresenta de forma detalhada a arquitetura e estrutura utilizada na aplicação.

Outra alternativa é executar a aplicação localmente, instalando as dependências:

```shell
pip3 install -r requirements.txt
```

E executando os seguinte comandos:

```shell
export FLASK_APP=app
```

```shell
export FLASK_ENV=production 
```

```shell
flask run
```

Caso utilize um ambiente virtual, lembrar de ativá-lo.

## Base de Dados

A base de dados utilizada para a construção da API também é parte do projeto de Engenharia. Em uma etapa anterior, utilizou-se a técnica  *Crawlers* na busca por trabalhos acadêmicos com a temática **"Saúde Mental"**, gerando como resutaldo uma base,com mais de cinquenta mil documentos. A base utiliza estrutra NoSql, especificamente o SGBD MongoDB. Os documentos na base possuem as seguintes informações:

* Id
* Data de publicação  
* Autores
* Palavras chave
* Repositórios
* Tipos de trabalho
* Resumos
* Títulos de trabalhos
* Url

Somente Id e Url não estão disponíves nas consultas fornecidas pela API. 