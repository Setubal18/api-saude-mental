# URLs

Na tabela abaixo é apresntado as rotas (*url's*) e as repectivas *views* utilizadas:

| Caminho                                                                                   | view                        |
|:----------------------------------------------------------------------------------------- |:--------------------------- |
|`api/`                                                                                     |`apresentacao`               |
|`api/anos/<ano>/paginas/<pagina>`                                                          |`data_ano`                   |
|`api/anos/anteriores/<ano>/paginas/<pagina>`                                               |`data_anos_ateriores`        |
|`api/anos/posteriores/<ano>/paginas/<pagina>`                                              |`data_anos_posteriores`      |
|`api/anos/inicio/<ano_incio>/fim/<ano_fim>/paginas/<pagina>`                               |`data_anos_periodo`          |
|`api/dissertacoes/paginas/<pagina>`                                                        |`conjunto_todos`             |
|`api/repositorios/<sigla>/paginas/<pagina>`                                                |`conjunto_repositorio`       |
|`api/tipos/<tipo_doc>/paginas/<pagina>`                                                    |`conjunto_tipos`             |
|`api/expressoes/palavraschave/<expressao>/paginas/<pagina>`                                |`expressao_palavrachave`     |
|`api/expressoes/autores/<expressao>/paginas/<pagina>`                                      |`expressao_autores`          |
|`api/expressoes/titulos/<expressao>/paginas/<pagina>`                                      |`expressao_titulo`           |
|`api/expressoes/resumos/<expressao>/paginas/<pagina>`                                      |`expressao_resumo`           |
|`api/palavraschave/<palavras>/paginas/<pagina>`                                            |`palavraschave_palavraschave`|
|`apiconsultas/repositorio/tipo/palavrachave/anoInicio/anoFim/resumo/titulo/numero_pagina>` |`avancado_consulta`          |
|`api/listas/anos`                                                                          |`lista_anos`                 |
|`api/listas/repositorios`                                                                  |`lista_repositorios`         |
|`api/listas/tipos`                                                                         |`lista_tipos`                |
|`api/contadores/anos`                                                                      |`contadores_anos`            |
|`api/contadores/repositorios`                                                              |`contadores_repositorios`    |
|`api/contadores/tipos`                                                                     |`contadores_tipos`           |

Outras rotas disponíveis. Não necessitam de nenhum parâmetro, apenas forncem informações sobre modelo e exemplo de utilização de uma URL. 

|caminho                        |view       | 
|:----------------------------- |:--------- |
|`api/dissertacoes`             |`descricao`|
|`api/repositorios`             |`descricao`|
|`api/tipos`                    |`descricao`|
|`api/consultas`                |`descricao`|
|`api/anos`                     |`descricao`|
|`api/anos/anteriores`          |`descricao`| 
|`api/anos/posteriores`         |`descricao`|
|`api/anos`                     |`descricao`|
|`api/expressoes/palavraschave` |`descricao`|
|`api/expressoes/titulos`       |`descricao`|
|`api/expressoes/autores`       |`descricao`|
|`api/expressoes/resumos`       |`descricao`|
|`api/palavraschave`            |`descricao`|
|`api/listas/anos`              |`descricao`|
|`api/listas/repositorios`      |`descricao`|
|`api/listas/tipos`             |`descricao`|
|`api/contadores/anos`          |`descricao`|
|`api/contadores/repositorios`  |`descricao`|
|`api/contadores/tipos`         |`descricao`|
