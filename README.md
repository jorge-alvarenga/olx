# olx

[Link Dashboard Power BI](https://app.powerbi.com/view?r=eyJrIjoiN2QwNGQ4MzItY2JlYS00MDEwLTgwOWMtNzM4NzRkOTJmMDhiIiwidCI6IjRhZDg5MTMyLWFmZWQtNDdhNC1hZjA3LWE4NDYxZTU0NmQ0NCJ9)

A motivação por trás desse projeto surgiu da minha vontade de colocar em prática os conhecimentos que venho adquirindo nos meus estudos na área de dados. Foi nesse contexto que decidi buscar uma vaga no LinkedIn e desenvolver um miniprojeto relacionado a ela. Durante minha busca por oportunidades na área de dados, encontrei uma vaga na OLX que despertou meu interesse. A descrição da vaga é a seguinte:

![Captura de tela de 2023-01-23 11-58-37](https://user-images.githubusercontent.com/64050213/214082540-f101c3e2-fff9-4b2a-9895-97d986fca47e.png)


Decidi criar esse miniprojeto com base na vaga mencionada e comecei fazendo uma breve pesquisa sobre a OLX. Durante essa pesquisa, encontrei uma apresentação muito interessante (https://www.infoq.com/br/presentations/data-science-na-olx/) que destacava números impressionantes, como um total de movimentação de R$ 80 bilhões na economia em 2016. Além disso, a plataforma contava com uma média de 12,5 milhões de anúncios ativos em 2017, com quase meio milhão de anúncios por dia. A cada minuto, eram vendidos 50 itens na OLX. Esses dados mostram claramente que a empresa gera uma quantidade enorme de informações, o que a torna perfeita para o desenvolvimento desse projeto.

Dentro da variedade de produtos anunciados na OLX, decidi focar no nicho automotivo. A ideia é criar um dashboard no Power BI com alguns KPIs específicos, como a quantidade de anúncios, os estados que geram mais anúncios, a distribuição de fabricantes por estado, modelos mais populares, entre outros. Já fiz um pequeno esboço de como gostaria que o dashboard ficasse: 
![dashboard](https://user-images.githubusercontent.com/64050213/214081770-0f9aeb50-fad6-4ebd-ad1b-f6d71d9fa616.png)

Espero que essa iniciativa demonstre minha habilidade e interesse na área de dados, além de proporcionar uma análise valiosa para a OLX. Estou ansioso para compartilhar o resultado final com vocês.


Para este projeto, será necessário obter os dados da própria plataforma da OLX, uma vez que não possuo uma base de dados prévia. Após a extração dos dados, farei o processo de tratamento para garantir a qualidade e consistência das informações. Em seguida, criarei um banco de dados para armazenar esses dados tratados, a fim de serem consumidos pelo Power BI.

Essa sequência de etapas é conhecida como ETL (Extração, Transformação e Carregamento). É um processo essencial para garantir que os dados sejam adequadamente coletados, preparados e disponibilizados para análise no Power BI.

Dessa forma, meu projeto envolverá a extração dos dados do site da OLX, o tratamento desses dados e a criação de um banco de dados para alimentar o Power BI. Esse fluxo ETL garantirá que eu tenha acesso a informações relevantes para construir o dashboard proposto.

![etl](https://user-images.githubusercontent.com/64050213/214081760-652cc3b9-80e6-4924-a8e6-0638052b158d.png)


Para este projeto, pretendo implementar um pipeline de ETL utilizando o Airflow. A DAG (Directed Acyclic Graph) do pipeline ficará configurada da seguinte forma:

Extrair Dados da OLX: Esta etapa consiste em utilizar as ferramentas e técnicas apropriadas para extrair os dados necessários diretamente do site da OLX. Isso pode envolver web scraping ou o uso de APIs disponibilizadas pela própria plataforma.

Transformar e Limpar Dados: Após a extração, os dados obtidos precisarão passar por um processo de transformação e limpeza. Isso pode incluir a remoção de dados duplicados, a padronização de formatos, a conversão de tipos de dados, entre outros ajustes necessários para garantir a qualidade e a consistência dos dados.

Carregar Dados no Banco de Dados: Nesta etapa, os dados tratados serão carregados em um banco de dados adequado para o armazenamento e consumo posterior. Isso pode ser um banco de dados relacional como MySQL ou PostgreSQL, ou até mesmo um banco de dados NoSQL, dependendo da natureza dos dados e dos requisitos do projeto.

Executar Análises e Criar o Dashboard: Com os dados devidamente armazenados no banco de dados, será possível executar análises e criar o dashboard no Power BI. Utilizando as funcionalidades do Power BI, serão implementados os KPIs desejados, como a quantidade de anúncios, a distribuição geográfica e outras métricas relevantes.

Ao implementar esse pipeline de ETL usando o Airflow, será possível automatizar o fluxo de trabalho, agendar as execuções das tarefas e monitorar o processo de forma eficiente. Isso garantirá a consistência dos dados e a atualização contínua do dashboard com as informações mais recentes da OLX.

![Captura de tela de 2023-01-23 12-58-38](https://user-images.githubusercontent.com/64050213/214086646-add4e0ad-eefd-4091-b639-b39f9fe8d8bb.png)


![raspagem](https://user-images.githubusercontent.com/64050213/214081756-f168b009-d3db-41a1-9424-985b73eb8409.png) 1° Etapa – Web Scraping

Ferramentas Utilizadas:



*   Python
*   Biblioteca beautifulsoup
*   Biblioteca Pandas


Depois de estudar o site da OLX decidi criar um web scraping que vai ir em cada fabricante de carro, depois vai em modelo por modelo e pegar a quantidade de anúncios por estado de cada modelo e colocar em um Dataframe do pandas e depois salvar em CSV, seguindo a seguinte estrutura:

![raspagem2](https://user-images.githubusercontent.com/64050213/214081731-a4d34fed-054a-4a3b-ae7a-0db9d2baf85d.png)

![limpar](https://user-images.githubusercontent.com/64050213/214081757-427c351e-db38-4f11-bbed-0eb7298ba921.png) 2° Etapa – Transforma / Tratar

Aqui vamos analisar os dados, verificar se tem algum dado faltando, se tem duplicata ,se tem algumas inconsistência, arrumar os dados para depois jogar no banco de dados.

![banco_de_dados](https://user-images.githubusercontent.com/64050213/214081771-4cc89a06-3475-40a4-b1b1-22e515fcaa3f.png) 3° Etapa – Carregar

Aqui vamos criar um banco de dados na AWS RDS, se conectar na base de dados e criar uma tabela com todos os dados coletados.
