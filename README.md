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

Após analisar o site da OLX, decidi criar um web scraping que percorrerá cada fabricante de carros e, em seguida, acessará cada modelo individualmente para obter a quantidade de anúncios por estado para cada modelo. Esses dados serão armazenados em um DataFrame do pandas e, posteriormente, serão salvos em formato CSV, seguindo a seguinte estrutura:

Coluna 1: Fabricante (manufacturer)
Coluna 2: Modelo (model)
Coluna 3: Estado (state)
Coluna 4: Quantidade de anúncios (ad_count)
Essa estrutura permitirá a análise e manipulação dos dados de forma conveniente e flexível. Com o DataFrame do pandas preenchido com os dados extraídos do web scraping, será possível realizar diversas operações e análises, como agrupamentos por fabricante, contagens de anúncios por modelo e estados, entre outras análises exploratórias.

Após a manipulação dos dados, o DataFrame poderá ser salvo em um arquivo CSV, garantindo que as informações coletadas sejam preservadas e possam ser facilmente compartilhadas ou utilizadas posteriormente em outras etapas do projeto, como a criação do dashboard no Power BI.

Dessa forma, o web scraping, a estrutura do DataFrame e a exportação em formato CSV fornecerão os dados necessários para alimentar o pipeline de ETL e, posteriormente, criar o dashboard com os KPIs desejados para a análise dos anúncios de carros na OLX.

Seguindo os seguintes de passos:

![raspagem2](https://user-images.githubusercontent.com/64050213/214081731-a4d34fed-054a-4a3b-ae7a-0db9d2baf85d.png)

![limpar](https://user-images.githubusercontent.com/64050213/214081757-427c351e-db38-4f11-bbed-0eb7298ba921.png) 2° Etapa – Transforma / Tratar


Nesta etapa do projeto, faremos uma análise dos dados extraídos para verificar se há alguma informação faltando, duplicatas ou inconsistências. O objetivo é garantir a qualidade dos dados antes de inseri-los no banco de dados.

Usando as funcionalidades do pandas, faremos as seguintes verificações e ajustes:

Verificar Dados Faltantes: Faremos uma verificação para identificar se há valores nulos ou ausentes em alguma coluna do DataFrame. Caso existam, poderemos decidir a melhor abordagem para lidar com esses dados, como preencher os valores faltantes com estimativas ou remover as linhas correspondentes, dependendo do contexto e do impacto nos resultados.

Remover Duplicatas: Verificaremos se há registros duplicados no DataFrame com base nas colunas relevantes. Caso encontremos duplicatas, removeremos essas entradas para evitar distorções nos resultados e garantir a integridade dos dados.

Corrigir Inconsistências: Realizaremos uma análise mais detalhada dos dados em busca de possíveis inconsistências ou erros, como valores inválidos ou discrepantes. Faremos as correções necessárias, seja excluindo esses registros ou aplicando transformações adequadas para garantir a consistência dos dados.

Após a análise e os ajustes, os dados estarão prontos para serem inseridos no banco de dados. É importante ressaltar que essa etapa de limpeza e preparação dos dados é crucial para garantir resultados confiáveis e precisos nas análises subsequentes.

Com os dados devidamente tratados, podemos prosseguir para a próxima etapa do projeto, que é a inserção dos dados no banco de dados para alimentar o dashboard no Power BI.


![banco_de_dados](https://user-images.githubusercontent.com/64050213/214081771-4cc89a06-3475-40a4-b1b1-22e515fcaa3f.png) 3° Etapa – Carregar

Nesta fase do projeto, vamos criar um banco de dados na AWS RDS (Relational Database Service), estabelecer a conexão com o banco de dados e criar uma tabela para armazenar todos os dados coletados.

Passos a seguir:

Criar o banco de dados na AWS RDS: Vamos acessar a AWS Console e criar uma instância de banco de dados na AWS RDS. Faremos as configurações necessárias, como tipo de instância, capacidade de armazenamento e credenciais de acesso. Escolheremos um banco de dados relacional adequado para armazenar nossos dados, como MySQL, PostgreSQL ou outro compatível.

Estabelecer a conexão com o banco de dados: Após criar o banco de dados na AWS RDS, utilizaremos as informações de conexão fornecidas pela AWS para nos conectarmos à instância do banco de dados. Utilizaremos uma biblioteca de conexão de banco de dados compatível com a linguagem de programação escolhida para o projeto.

Criar a tabela: Com a conexão estabelecida, executaremos as consultas SQL necessárias para criar uma tabela no banco de dados. A estrutura da tabela será definida com base nos dados coletados, incluindo as colunas e os tipos de dados apropriados para cada uma delas. Certificaremos de mapear corretamente as colunas do DataFrame para as colunas da tabela do banco de dados.

Inserir dados na tabela: Com a tabela criada, faremos a inserção dos dados coletados no banco de dados. Utilizaremos as funcionalidades adequadas da biblioteca de conexão de banco de dados para executar as instruções SQL necessárias e inserir cada linha do DataFrame na tabela.

Após concluirmos esses passos, teremos nosso banco de dados na AWS RDS criado e uma tabela com todos os dados coletados devidamente inseridos. Isso nos permitirá utilizar esses dados como fonte para alimentar o dashboard no Power BI e realizar análises mais aprofundadas dos anúncios de carros na OLX.





