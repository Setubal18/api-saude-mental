# Views <!-- omit in toc -->

- [`apresentacao`](#apresentação)
- [`data_ano`](#ano)
- [`data_anos_ateriores`](#anos_anteriores)
- [`data_anos_posteriores`](#anos_posteriores)
- [`data_anos_periodo`](#anos_posteriores)
- [`avancado_consulta`](#avancado_consulta)
- [`conjunto_todos`](#conjunto_todos)
- [`conjunto_repositorio`](#conjunto_repositorio)
- [`palavraschave_palavraschave`](#palavraschave_palavraschave)
- [`expressao_resumo`](#expressao_resumo)
- [`expressao_titulo`](#expressao_titulos)
- [`expressao_palavrachave`](#expressao_palavrachave)
- [`expressao_autores`](#expressao_autores)
- [`contadores_repositorios`](#contadores_repositorios)
- [`contadores_anos`](#contadores_anos)
- [`contadores_tipos`](#contadores_tipos)
- [`lista_repositorios`](#lista_repositorios)
- [`lista_anos`](#lista_anos)
- [`lista_tipos`](#lista_tipos)
- [`descricao`](#descricao)

## `apresentacao`

A *view* retorna apenas um conjunto de *ULR's* disponíveis na API. Não exige nenhum parâmetro.  

## `descricao`

A *view* `descricao` não exige nenhum parâmetro, retorna um conjunto de informações, apresentado um modelo e um exemplo de utilização de uma URL.

## `data_ano`

A *view* `data_ano` recebe parâmetros para consultar documentos por ano. Recebe dois parâmetros:

- `ano`: aceita somente números inteiros e valores entre 1900 e 2100.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `data_anos_anteriores`

A *view* `data_anos_anteriores` recebe parâmetros para consultar documentos anterioes a um determinado ano. Recebe dois parâmetros:

- `ano_ant`: aceita somente números inteiros e valores entre 1900 e 2100.

_ `numero_pagina`: aceita somente números inteiros acima de zero.

## `data_anos_posteriores`

A *view* `data_anos_posteriores` recebe parâmetros para consultar documentos posteriores a um determinado ano. Recebe dois parâmetros:

- `ano_pos`: aceita somente números inteiros e valores entre 1900 e 2100.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `data_anos_períodos`

A *view* `data_anos_período` recebe parâmetros para consultar documentos dentro de um período de anos. Recebe três parâmetros:

- `ano_incio`: aceita somente números inteiros e valores entre 1900 e 2100.

- `ano_fim`: aceita somente números inteiros e valores entre 1900 e 2100.

## `avancado_consulta`

A *view* `avancado_consulta` recebe parâmetros para consultar documentos que atendam a pelo menos um parâmetro. Recebe oito parâmetros:

- `repositorio`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `tipo`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `palavrachave`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `anoIncio`: aceita somente números inteiros e valores entre 1900 e 2100.

- `anoFim`: aceita somente números inteiros e valores entre 1900 e 2100.

- `resumo`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `titulo`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `conjunto_todos`

A *view* `conjunto_todos` retorna todos os documentos existentes na base de dados. Recebe apenas um parâmetro:

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `conjunto_repositorio`

A *view* `conjunto_repositorio` recebe parâmetros para consultar documentos por repositório (universidade). Recebe os seguintes parâmetros:

- `sigla`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `conjunto_tipo`

A *view* `conjunto_tipo` recebe parâmetros para consultar documentos por tipo de trabalho (mestrado, doutorado, etc). Recebe os seguintes parâmetros:

- `tipo`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `palavraschave_palavraschave`

A *view* `palavraschave_palavraschave` recebe parâmetros para consultar documentos por palavras chave. Recebe os parâmetros:

- `palavras`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `expressao_resumo`

A *view* `expressao_resumo`recebe parâmetros para consultar documentos por exepressões em resumos. Recebe os parâmetros:

- `expressao`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `expressao_titulo`

A *view* `expressao_titulo`recebe parâmetros para consultar documentos por exepressões em títulos. Recebe os parâmetros:

- `expressao`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `expressao_palavrachave`

A *view* `expressao_palavrachave`recebe parâmetros para consultar documentos por exepressões em palavrachave. Recebe os parâmetros:

- `expressao`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `expressao_autores`

A *view* `expressao_autores`recebe parâmetros para consultar documentos por exepressões em autores. Recebe os parâmetros:

- `expressao`: todos os dados (caracter, letras, ou mesmo números) inseridos neste parâmetros será interpretado como uma *string*.

- `numero_pagina`: aceita somente números inteiros acima de zero.

## `contadores_repositorios`

A *view* `contadores_repositorios` não recebe nenhum parâmetro. Retorna um lista com informações sobre o número de trabalhos por repositório. Retorna as seguinte variáveis:

- `_id`: informa a sigla da universidade.

- `count`: informa o número de trabalhos. 

## `contadores_anos`

A *view* `contadores_anos` não recebe nenhum parâmetro. Retorna um lista com informações sobre o número de trabalhos por ano. Retorna as seguinte variáveis:

- `_id`: informa o ano.

- `count`: informa o número de trabalhos. 

## `contadores_tipos`

A *view* `contadores_tipos` não recebe nenhum parâmetro. Retorna um lista com informações sobre o número de trabalhos por tipo de trabalho. Retorna as seguinte variáveis:

- `_id`: informa o tipo de trabalho.

- `count`: informa o número de trabalhos. 

## `lista_repositorios`

A *view* `lista_repositorios` não recebe nenhum parâmetro. Retorna um lista de repositórios existentes na base de dados. Retorna as seguinte variáveis:

- `_id`: informa a sigla da universidade.

## `lista_anos`

A *view* `lista_repositorios` não recebe nenhum parâmetro. Retorna um lista de anos existentes na base de dados. Não retorna nenhuma variável, os valores da lista são acessados diretamente:


## `lista_tipos`

A *view* `lista_repositorios` não recebe nenhum parâmetro. Retorna um lista de tipos existentes na base de dados. Retorna as seguinte variáveis:

- `_id`: informa o tipo de trabalho.