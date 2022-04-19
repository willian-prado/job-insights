## Projeto Job Insights

> Primeiro projeto do módulo de Ciência da Computação do curso de desenvolvimento web da Trybe.

**Contexto**

No bloco desse projeto damos nossos primeiros passos com a linguagem de programação Python. Começando por sua instalação e configuração do ambiente de desenvolvimento, seguido por sua sintaxe, diferentes tipos de variáveis, métodos e principais funções. Entre as funções vistas, estão as utilizadas para leitura e manipulação de arquivos JSON e CSV que serão necessárias nesse projeto.

**Objetivo do projeto**

Implementar funções para analisar um conjunto de dados sobre empregos. Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

**Principais habilidades desenvolvidas nesse trabalho**

- Utilizar o terminal interativo do Python.
- Utilizar estruturas condicionais e de repetição.
- Utilizar funções built-in do Python.
- Utilizar tratamento de exceções.
- Realizar a manipulação de arquivos.
- Escrever funções.
- Escrever testes com Pytest.
- Escrever seus próprios módulos e importá-los em outros códigos.

**Tecnologia utilizada**

<a href="https://www.python.org"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" title="Python" height="35" align="center"/> - Python</a> 

---

### Lista de requisitos propostos pela Trybe:

#### Obrigatórios

#### 1 - Implemente a função `read`
local: `src/jobs.py`

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. Esta função será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

- A função deve receber um _path_ (uma string com o caminho para um arquivo).
- A função deve abrir o arquivo e ler seus conteúdos.
- A função deve tratar o arquivo como CSV.
- A função deve retornar uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.

✍️ Teste manual: abra um terminal Python importando estas funções através do comando `python3 -i src/jobs.py` e invoque a função utilizando diferentes _paths_.

#### 2 - Implemente a função `get_unique_job_types`
local: `src/insights.py`

Agora que temos como carregar os dados, podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.

- A função deve receber o _path_ do arquivo csv com os dados.
- A função deve invocar a função `jobs.read` com o _path_ recebido para obter os dados.
- A função deve retornar uma lista de valores únicos presentes na coluna `job_type`.

#### 3 - Implemente a função `get_unique_industries`
local: `src/insights.py`

Da mesma forma, agora iremos identificar quais indústrias estão representadas nesse conjunto de dados.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve retornar uma lista de valores únicos presentes na coluna `industry`.
- A função desconsidera valores vazios

#### 4 - Implemente a função `get_max_salary`
local: `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar *um valor inteiro* com o maior salário presente na coluna `max_salary`.

#### 5 - Implemente a função `get_min_salary`
local: `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar *um valor inteiro* com o menor salário presente na coluna `min_salary`.

#### 6 - Implemente a função `filter_by_job_type`
local: `src/insights.py`

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar esse filtro.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `job_type` como segundo parâmetro.
- A função deve retornar uma lista com todos os empregos onde a coluna `job_type` corresponde ao parâmetro `job_type`.

#### 7 - Implemente a função `filter_by_industry`
local: `src/insights.py`

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria. Vamos precisar implementar esse filtro também.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `industry` como segundo parâmetro.
- A função deve retornar uma lista de dicionários com todos os empregos onde a coluna `industry` corresponde ao parâmetro `industry`.

#### 8 - Implemente a função `matches_salary_range`
local: `src/insights.py`

O aplicativo vai precisar filtrar os empregos por salário também. Como uma função auxiliar, implemente `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

- A função deve receber um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`.
- A função deve receber um inteiro `salary` como segundo parâmetro.
- A função deve lançar um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não-numéricos;
- A função deve retornar `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.

#### 9 - Implemente a função `filter_by_salary_range`
local: `src/insights.py`

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a função auxiliar implementada no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber um inteiro `salary` como segundo parâmetro.
- A função deve ignorar os empregos com valores inválidos para `min_salary` ou `max_salary`.
- A função deve retornar uma lista com todos os empregos onde o salário `salary` estiver entre os valores da coluna `min_salary` e `max_salary`.

##### 10 - Implemente um teste para a função `sort_by`
local: `tests/sorting/test_sorting.py`

Por fim, espera-se que a pessoa usuária possa escolher um critério de ordenação para exibir os empregos. Já temos uma implementação para essa ordenação em `src/sorting.py`, mas queremos ter certeza de que ela funciona e, principalmente, que não deixará de funcionar conforme vamos implementando novos recursos. Precisamos então escrever um *teste*!

Esse teste deve se chamar `test_sort_by_criteria` e garantir que a função funciona segundo esta especificação:

- A função `sort_by` recebe dois parâmetros:
  - `jobs` uma lista de dicionários com os detalhes de cada emprego;
  - `criteria` uma string com uma chave para ser usada como critério de ordenação.
- O parâmetro `criteria` deve ter um destes valores: `min_salary`, `max_salary`, `date_posted`
- A ordenação para `min_salary` deve ser crescente, mas para `max_salary` ou `date_posted` devem ser decrescentes.
- Os empregos que não apresentarem um valor válido no campo escolhido para ordenação devem aparecer no final da lista.

> 📌 O **teste da Trybe** espera que o **seu teste** falhe em alguns casos. Nesse caso, o teste terá a saída `XFAIL` (ao invés de `PASS` ou `FAIL`), e isso significa que o requisito foi atendido ✔️

#### Bônus

##### 11 - Implemente a página de um job
local: `src/routes_and_views.py`

Para fechar com chave de ouro, que tal testar o quanto você aprendeu de Flask apenas vendo como fizemos as páginas de `index` e de `jobs`, e tentar criar uma página que irá exibir todas as informações de um job em específico?

- A função deve ser decorada com a rota `/job/<index>`.
- A função deve receber um parâmetro `index`.
- A função deve chamar a `read` para ter uma lista com todos os jobs.
- A função deve chamar a `get_job`, declarada no arquivo `src/more_insights.py`, para selecionar um job específico pelo `index`.
- A função deve renderizar o template `job.jinja2`, passando um parâmetro `job` contendo o job retornado pela `get_job`.

✍️ Teste manual: após criar a view, cheque se, na página que lista os jobs, aparecem links para jobs específicos nos números que identificam cada job. Ao clicar em um destes links, você deve ser levado a uma página que lista todas as informações do job.
