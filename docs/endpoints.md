# Endpoints da API <!-- omnit in toc -->

- [Anos](#anos)
  - `GET /anos/<ano>/paginas/<pagina>`
  - `GET /anos/anteriores/<ano>/paginas/<pagina>`
  - `GET /anos/posteriores/<ano>/paginas/<pagina>`
  - `GET /anos/inicio/<ano_incio>/fim/<ano_fim>/paginas/<pagina>`

- [Conjunto](#conjunto)
  - `GET /dissertacoes/paginas/<pagina>`
  - `GET /repositorios/<sigla>/paginas/<pagina>`
  - `GET /tipos/<tipo_doc>/paginas/<pagina>`

- [Expressões](#expressões)
  - `GET /expressoes/palavraschave/<expressao>/paginas/<pagina>`
  - `GET /expressoes/autores/<expressao>/paginas/<pagina>`
  - `GET /expressoes/titulos/<expressao>/paginas/<pagina>`
  - `GET /expressoes/resumos/<expressao>/paginas/<pagina>`

- [Palavras Chave](#palavras-chave)
  - `GET palavraschave/<palavras>/paginas/<pagina>`

- [Consulta Avançada](#avançada)
  - `GET consultas/repositorio/tipo/palavrachave/anoInicio/anoFim/resumo/titulo/numero_pagina>`

- [Listas](#listas)
  - `GET /listas/anos`
  - `GET /listas/repositorios`
  - `GET /listas/tipos`

- [Contadores](#contadores)
  - `GET /contadores/anos`
  - `GET /contadores/repositorios`
  - `GET /contadores/tipos`

- [Auxílio](#auxílio)
  - `GET api/dissertacoes`
  - `GET api/repositorios`
  - `GET api/tipos`
  - `GET api/consultas`
  - `GET api/anos`
  - `GET api/anos/anteriores`
  - `GET api/anos/posteriores`
  - `GET api/anos`
  - `GET api/expressoes/palavraschave`
  - `GET api/expressoes/titulos`
  - `GET api/expressoes/autores`
  - `GET api/expressoes/resumos`
  - `GET api/palavraschave`
  - `GET api/listas/anos`
  - `GET api/listas/repositorios`
  - `GET api/listas/tipos`
  - `GET api/contadores/anos`
  - `GET api/contadores/repositorios`
  - `GET api/contadores/tipos`


## `Anos`

**Base da URL: `/anos`**

Os recursos de anos retornam documentos no qual o **ano** seja igual ao parâmetro **ano** pequisado. Retornam resultado em 10 documentos, dependendo do tamanho da resposta, há um método de paginação, gerenciado pelo parâmetro **pagina**. Para validar o ano dos documentos é necessário reliazar uma formatação para uma data válida.

Os recursos disponíveis que permitem realizar consultas são:

- `GET /anos/<ano>/paginas/<pagina>`
- `GET /anos/anteriores/<ano>/paginas/<pagina>`
- `GET /anos/posteriores/<ano>/paginas/<pagina>`
- `GET /anos/inicio/<ano_incio>/fim/<ano_fim>/paginas/<pagina>`

Parâmetros utilizados para nas consultas:

| **`Parâmetro`** | **`tipo`** | **`Descrição`** |
| :-------------- | :--------- | :-------------- |
| `ano`           | Int        | Recebe apenas número inteiros, entre o intervalo 1900 e 2100 |
| `ano_inicio`    | Int        | Recebe apenas número inteiros, entre o intervalo 1900 e 2100 |
| `ano_fim`       | Int        | Recebe apenas número inteiros, entre o intervalo 1900 e 2100 |
| `pagina`        | Int        | Recebe apenas número inteiros, maiores que 0 |

O formato de resposta (*response*) de uma requisição (*request*) é no formato JSON

**Exemplo**

```json
[
  {
    "_id": {
      "$oid" "5e48066f98e462a6e03e7376"
    },
    "autores": "autor1", "autor2, ..."
    "data": {
      "$date": 1579219200000
    },
    "palavrachave": ["palavra1", "palavra2", "..."],
    "repositorio": "USP",
    "resumo": "Este trabalho ...",
    "tipo": "mestrado",
    "titulo": "Titulo Do Trabalho",
    "url": "https://teses.usp.br/teses/disponiveis/22/22131/tde-19112019-195052/pt-br.php"
  }
  
]
```

Códigos de retorno:

- **200**: Ok
- **204**: No Content
- **400**: Bad Request
- **404**: Not Found
- **405**: Method Not Allowed

## `Conjuntos`

**Base da URL: `/dissertacoes`**

**Base da URL: `/repositorios`**

**Base da URL: `/tipos`**

Os recursos **`/dissertacoes`**, **`/repositorios`** e **`/tipos`** retornam respectivamente, todos os documentos existentes, todos documentos de um determinado repositório e todos os documentos por tipo. Exceto em **`/dissertacoes`**, as consultas utilizam expressões regulares,interpretando todo tipo de dado inserido como *string*. Retornam resultado em 10 documentos, dependendo do tamanho da resposta, há um método de paginação, gerenciado pelo parâmetro **pagina**.

Os recursos disponíveis que permitem realizar consultas são:

- `GET /dissertacoes/paginas/<pagina>`
- `GET /repositorios/<sigla>/paginas/<pagina>`
- `GET /tipos/<tipo_doc>/paginas/<pagina>`

Parâmetros utilizados para nas consultas:

| **`Parâmetro`** | **`tipo`** | **`Descrição`** |
| :-------------- | :--------- | :-------------- |
| `sigla`         | String     | Recebe todo tipo de dados, porém são interpretados como *string* |
| `tipo_doc`      | String     | Recebe todo tipo de dados, porém são interpretados como *string* |
| `pagina`        | Int        | Recebe apenas número inteiros, maiores que 0 |

O formato de resposta (*response*) de uma requisição (*request*) é no formato JSON

**Exemplo**

```json
[
  {
    "_id": {
      "$oid" "5e48066f98e462a6e03e7376"
    },
    "autores": "autor1", "autor2, ..."
    "data": {
      "$date": 1579219200000
    },
    "palavrachave": ["palavra1", "palavra2", "..."],
    "repositorio": "USP",
    "resumo": "Este trabalho ...",
    "tipo": "mestrado",
    "titulo": "Titulo Do Trabalho",
    "url": "https://teses.usp.br/teses/disponiveis/22/22131/tde-19112019-195052/pt-br.php"
  } 
]
```

Códigos de retorno:

- **200**: Ok
- **204**: No Content
- **400**: Bad Request
- **404**: Not Found
- **405**: Method Not Allowed

## `Expressões`

**Base da URL: `/expressoes`**

Os recursos disponibilizados para expressões realizam consultas utilizando expressoes regulares. Nos recursos as consultas pesquisam por expressões que sejam iguais as **expressões** passadas como parâmetro, desconsiderando o *case sensitive*. Retornam resultado em 10 documentos, dependendo do tamanho da resposta, há um método de paginação, gerenciado pelo parâmetro **pagina**.

Os recursos disponíveis que permitem realizar consultas são:

- `GET /expressoes/palavraschave/<expressao>/paginas/<pagina>`
- `GET /expressoes/autores/<expressao>/paginas/<pagina>`
- `GET /expressoes/titulos/<expressao>/paginas/<pagina>`
- `GET /expressoes/resumos/<expressao>/paginas/<pagina>`

Parâmetros utilizados para nas consultas:

| **`Parâmetro`** | **`tipo`** | **`Descrição`** |
| :-------------- | :--------- | :-------------- |
| `expressao`     | String     | Recebe todo tipo de dados, porém são interpretados como *string* |
| `pagina`        | Int        | Recebe apenas número inteiros, maiores que 0 |

O formato de resposta (*response*) de uma requisição (*request*) é no formato JSON

**Exemplo**

```json
[
  {
    "_id": {
      "$oid" "5e48066f98e462a6e03e7376"
    },
    "autores": "autor1", "autor2, ..."
    "data": {
      "$date": 1579219200000
    },
    "palavrachave": ["palavra1", "palavra2", "..."],
    "repositorio": "USP",
    "resumo": "Este trabalho ...",
    "tipo": "mestrado",
    "titulo": "Titulo Do Trabalho",
    "url": "https://teses.usp.br/teses/disponiveis/22/22131/tde-19112019-195052/pt-br.php"
  }
]
```

Códigos de retorno:

- **200**: Ok
- **204**: No Content
- **400**: Bad Request
- **404**: Not Found
- **405**: Method Not Allowed

## `Palavras-Chave`

**Base da URL: `/palavraschave`**

A consutla por palavra chave é semelhante a consulta por exepressões regulares, contudo a busca é realizada por considerando o parâmetro uma **palavra**, somente os documentos com o parâmetro equivalentes são retornados. Retorna resultado em 10 documentos, dependendo do tamanho da resposta, há um método de paginação, gerenciado pelo parâmetro **pagina**.

O recurso disponível que permite realizar consultas é:

- `GET palavraschave/<palavras>/paginas/<pagina>`

Parâmetros utilizados para nas consultas:

| **`Parâmetro`** | **`tipo`** | **`Descrição`** |
| :-------------- | :--------- | :-------------- |
| `palavras`      | String     | Recebe todo tipo de dados, porém são interpretados como *string*. Recebe uma ou mais palavras seperadas por ponto e vírgula ( ; ) |
| `pagina`        | Int        | Recebe apenas número inteiros, maiores que 0 |

O formato de resposta (*response*) de uma requisição (*request*) é no formato JSON

**Exemplo**

```json
[
  {
    "_id": {
      "$oid" "5e48066f98e462a6e03e7376"
    },
    "autores": "autor1", "autor2, ...",
    "data": {
      "$date": 1579219200000
    },
    "palavrachave": ["palavra1", "palavra2", "..."]
    "repositorio": "USP",
    "resumo": "Este trabalho ...",
    "tipo": "mestrado",
    "titulo": "Titulo Do Trabalho",
    "url": "https://teses.usp.br/teses/disponiveis/22/22131/tde-19112019-195052/pt-br.php"
  }
]
```

Códigos de retorno:

- **200**: Ok
- **204**: No Content
- **400**: Bad Request
- **404**: Not Found
- **405**: Method Not Allowed


## `Avançada`

**Base da URL: `/consultas`**

O recuros de **consulta avançada** recebe vários parâmetros e retorna documentos que atendam a pelo menos um dos parâmetros passado. Retorna resultado em 10 documentos, dependendo do tamanho da resposta, há um método de paginação, gerenciado pelo parâmetro **pagina**.

O recurso disponível que permite realizar consultas é:

- `GET consultas/repositorio/tipo/palavrachave/anoInicio/anoFim/resumo/titulo/numero_pagina>`

Parâmetros utilizados para nas consultas:

| **`Parâmetro`** | **`tipo`** | **`Descrição`** |
| :-------------- | :--------- | :-------------- |
| `repositorio`   | String     | Recebe todo tipo de dados, porém são interpretados como *string* |
| `tipo`          | String     | Recebe todo tipo de dados, porém são interpretados como *string* |
| `palavraschave` | String     | Recebe todo tipo de dados, porém são interpretados como *string* |
| `anoInicio`     | Int        | Recebe apenas número inteiros, entre o intervalo 1900 e 2100 |
| `anoFim`        | Int        | Recebe apenas número inteiros, entre o intervalo 1900 e 2100 |
| `resumo`        | String     | Recebe todo tipo de dados, porém são interpretados como *string* |
| `titulo`        | String     | Recebe todo tipo de dados, porém são interpretados como *string* |
| `pagina`        | Int        | Recebe apenas número inteiros, maiores que 0 |

O formato de resposta (*response*) de uma requisição (*request*) é no formato JSON

**Exemplo**

```json
[
  {
    "_id": {
      "$oid" "5e48066f98e462a6e03e7376"
    },
    "autores": "autor1", "autor2, ...",
    "data": {
      "$date": 1579219200000
    },
    "palavrachave": ["palavra1", "palavra2", "..."]
    "repositorio": "USP",
    "resumo": "Este trabalho ...",
    "tipo": "mestrado",
    "titulo": "Titulo Do Trabalho",
    "url": "https://teses.usp.br/teses/disponiveis/22/22131/tde-19112019-195052/pt-br.php"
  }
]
```

Códigos de retorno:

- **200**: Ok
- **204**: No Content
- **400**: Bad Request
- **404**: Not Found
- **405**: Method Not Allowed

## `Listas`

**Base da URL: `/lista`**

O recurso de lista não realiza nenhum tipo de consulta e não necessita de parâmetros, apenas retona valores, especificamente **lista de anos**, **tipo de documentos** e **lista de repositórios**. Não há sistema de paginação.

Os recursos disponíveis que permitem realizar consultas são:

- `GET /listas/anos`
- `GET /listas/repositorios`
- `GET /listas/tipos`

Exceto em lista de anos, os valores são acessados através da variável:

| **`Variável`** | **`tipo`** | **`Descrição`** |
| :------------- | :--------- | :-------------- |
| `_id`          | String     | Armazena uma *string* contendo uma valor para tipo ou repositório|
| `objeto`       | Int        | Em lista de anos o **ano** é acessado diretamente|

O formato de resposta (*response*) de uma requisição (*request*) é no formato JSON

**Exemplo**

```json
[
  {
    "_id": "tipo de documento 1 / repositorios A"
  },
  {
    "_id": "tipo de documento 2 / repositorios A"
  },
  {
    "_id": "tipo de documento N / repositorios N"
  },
]
```

**Exemplo (`/lista/anos`)**

```json
[
  2000,
  2001,
  2002,
  ...
]
```

Códigos de retorno:

- **200**: Ok
- **204**: No Content
- **404**: Not Found
- **405**: Method Not Allowed

## `Contadores`

Este recurso não exige nenhum parâmetros e não realiza consultas, apenas retorna valores sobre a base de dados, numero de documentos por ano, tipo e repositório. Não utiliza paginação.

Os recursos disponíveis que permitem realizar consultas são:

- `GET /contadores/anos`
- `GET /contadores/repositorios`
- `GET /contadores/tipos`


Os valores são acessados através da variável:

| **`Variável`** | **`tipo`** | **`Descrição`** |
| :------------- | :--------- | :-------------- |
| `_id`          | String     | Armazena uma *string* contendo uma valor para ano, tipo ou repositório|
| `count`       | Int         | Armazena a quantidade de documentos|

O formato de resposta (*response*) de uma requisição (*request*) é no formato JSON

**Exemplo**

```json
[
  {
    "_id": "ano 1 / tipo de documento 1 / repositorio A",
    "count": 1000
  },
  {
    "_id": "ano 2 / tipo de documento 2 / repositorio B",
    "count": 1000
  },
  {
    "_id": "ano n / tipo de documento n / repositorio n",
    "count": 1000
  },
]
```

Códigos de retorno:

- **200**: Ok
- **204**: No Content
- **404**: Not Found
- **405**: Method Not Allowed

## `Auxílio`

Alguams URL's servem como auxílio para consumir os dados da API apresentando um exemplo e um modelo de utilização de uma URL. Não exige nenhuma informação.

Os recursos disponíveis que permitem auxiliar nas consultas são:

- `GET api/dissertacoes`
- `GET api/repositorios`
- `GET api/tipos`
- `GET api/consultas`
- `GET api/anos`
- `GET api/anos/anteriores`
- `GET api/anos/posteriores`
- `GET api/anos`
- `GET api/expressoes/palavraschave`
- `GET api/expressoes/titulos`
- `GET api/expressoes/autores`
- `GET api/expressoes/resumos`
- `GET api/palavraschave`
- `GET api/listas/anos`
- `GET api/listas/repositorios`
- `GET api/listas/tipos`
- `GET api/contadores/anos`
- `GET api/contadores/repositorios`
- `GET api/contadores/tipos`

**Exemplo**

```json
[
  {
    "ano": {
            "modelo" : "api/anos/<int:ano>/paginas/<int:pagina>",
            "exemplo": "api/anos/2020/paginas/1"
        },
        "anos_anteriores": {
            "modelo" : "api/anos/anteriores/<int:ano>/paginas/<int:numero_pagina>",
            "exemplo": "api/anos/anteriores/2005/paginas/1"
        },
        "anos_posteriores": {
            "modelo" : "api/anos/posteriores/<int:ano>/paginas/<int:numero_pagina>",
            "exemplo": "api/anos/posteriores/2000/paginas/1"
        },
        "periodo": {
            "modelo" : "api/anos/inicio/<int:ano_inicio>/fim/<int:ano_fim>/paginas/<int:numero_pagina>",
            "exemplo": "api/anos/inicio/2000/fim/2005/paginas/1"
        }
    }
]
```

Códigos de retorno:

- **200**: Ok
- **404**: Not Found
- **405**: Method Not Allowed