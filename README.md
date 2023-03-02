# olx

![Projeto POWER BI]([[https://user-images.githubusercontent.com/64050213/222525970-b661e0e9-528c-4866-8e51-fab6afd432b5.png](https://app.powerbi.com/view?r=eyJrIjoiN2QwNGQ4MzItY2JlYS00MDEwLTgwOWMtNzM4NzRkOTJmMDhiIiwidCI6IjRhZDg5MTMyLWFmZWQtNDdhNC1hZjA3LWE4NDYxZTU0NmQ0NCJ9)])


A ideia desse projeto veio da necessidade de colocar a prova os conhecimentos que venho adquirindo com os meus estudos na área de dados. Foi quando eu pensei em pegar uma vaga no LinkedIn e desenvolver um miniprojeto em cima dela. Procurando vagas na área dados encontrei a seguinte vaga na OLX: 

![Captura de tela de 2023-01-23 11-58-37](https://user-images.githubusercontent.com/64050213/214082540-f101c3e2-fff9-4b2a-9895-97d986fca47e.png)

Pensei vou montar esse miniprojeto em cima dessa vaga, então comecei a fazer uma breve pesquisa sobre a OLX e achei essa apresentação muito bacana (https://www.infoq.com/br/presentations/data-science-na-olx/) onde fala de numero bem expressivos com um total de movimentação de R$ 80 bilhões na economia em 2016, que tem aproximadamente no ano de 2017 uma média de 12,5 milhões de anúncios ativos na plataforma e quase meio milhão de anúncios por dia, com a cada 1 minuto vendendo 50 itens ou seja é uma empresa que gera uma quantidade de dados gigantesca perfeito para criar um projeto. Dentre diversas linhas de produtos (coloca produto nisso!) que são anunciados na OLX escolhi o nicho de mercado de automotivo. A ideia é montar um dashboard no Power BI com alguns KPIs como a quantidade de anúncios, quais estados que geram mais anúncios, fabricante por estado e modelos etc. Fiz um pequeno esboço de como quero que fique o dashboard:

![dashboard](https://user-images.githubusercontent.com/64050213/214081770-0f9aeb50-fad6-4ebd-ad1b-f6d71d9fa616.png)

Com isso vou precisar de dados como não tenho nenhuma base de dados vou precisar extrair do próprio site da OLX, depois vou tratar e depois criar um banco de dados para consumir pelo Power BI, ou seja, vou fazer o famoso ETL.

![etl](https://user-images.githubusercontent.com/64050213/214081760-652cc3b9-80e6-4924-a8e6-0638052b158d.png)

Para o projeto vou criar um pipeline de ETL usando o AIRFLOW e a Dag vai ficar assim :

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
