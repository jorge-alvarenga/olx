# Importando bibliotecas
from unidecode import unidecode
from urllib.request import urlopen, urlretrieve, Request
from bs4 import BeautifulSoup
import pandas as pd
import math
import requests
from urllib.error import HTTPError
import sqlalchemy
from sqlalchemy import create_engine

def limpar_modelo_por_marca(marca,modelo):
  # Foi identificado que os separadores dos modelos que tem mais de uma palavra não são padronizados por isso que criamos essa função para colocar de forma correto para cada modelo.
  modelo = modelo.lower()
  marca = marca.lower()
  if marca == 'hitech-eletric':
    modelo = modelo.replace(' ','-')
    modelo = modelo.replace('.','-')
  elif marca == 'bmw':
    modelo = modelo.replace('.','-')
    modelo = modelo.replace('/','-')
    modelo = modelo.replace(' ','-')
  elif marca == 'mercedes-benz':
    modelo = modelo.replace('.','-')
    modelo = modelo.replace('/','-')
    modelo = modelo.replace(' ','-')
  elif marca == 'toyota':
    modelo = modelo.replace('.','')
    modelo = modelo.replace(' ','-')
  elif marca == 'jaguar':
    if modelo == 'e-pace':
      modelo = modelo.replace('-','')
  elif marca == 'iveco':
    if modelo == 'daily city':
      modelo = modelo.replace(' ','')
    else:
      modelo = modelo.replace(' ','-')
  elif marca == 'vw-volkswagen':
    modelo = modelo.replace(' ','-') 
    modelo = modelo.replace('!','') 
  elif marca == 'citroen':
    if modelo == 'c4 cactus':
      modelo = modelo.replace(' ','_')
    else:
      modelo = modelo.replace(' ','-')
  elif marca == 'ford':
    modelo = modelo.replace(' ','-')
    modelo = modelo.replace('+','-mais')
  elif marca == 'hyundai':
    modelo = modelo.replace(' ','-')
  elif marca == 'jac':
    modelo = modelo.replace(' ','-')
    modelo = modelo.replace('.','-')
  elif marca == 'cadillac':
    modelo = modelo.replace(' ','-')
    modelo = modelo.replace('/','-')
  elif marca == 'chery':
    if modelo == 'tiggo 2':
      modelo = modelo.replace(' ','')
    modelo = modelo.replace(' ','-')
  elif marca == 'chrysler':
    modelo = modelo.replace(' & ','-')
    modelo = modelo.replace(' ','-')
  else:
    modelo = modelo.replace(' ','-')
  
  return modelo
# Obtendo o HTML

def web_scraping_OLX():
  url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios'

  headers = {'User-Agent': 'Mozilla/5.0'}

  try:
      req = Request(url, headers = headers)
      response = urlopen(req)
      
  except HTTPError as e:
      print(e.status, e.reason)
      
  except URLError as e:
      print(e.reason)

  html = response.read().decode('utf-8')
  soup = BeautifulSoup(html, 'html.parser')

  # Aqui vamos buscar e raspar para criar uma lista de marcar para que possamos correr por essa lista

  marcas =[]
  for marca in soup.find('select', {"class": "g98wuw-1 hpeKug"}).findAll('option'):
      marca = marca.text
      marca = marca.replace(' ','-') #Algumas marcar tinha espaço e esse espaço é substituído por "-"" quando vai para url
      marca = marca.replace('---','-')
      marca = marca.lower()
      marcas.append(marca)
  marcas.remove('marca')


  ### Aqui vamos percorrer todas as marcas, buscar todos os modelos daquela marcar e ir por um para pegar a quantidade de anúncios por estado ###
  dataset = [] # Onde vai ficar todos os dados de todos os modelos
  dataset_erro = [] # Lista de site que entrou e deu erro
  dataset_zero = [] # Lista de sites de modelos que deu erro por não ter nenhum anúncio

  for marca in marcas:# Vai pecorrer a lista de marca por marca
    url = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/'+marca # Vai modificar a URL para a marca da lista atual
    try:
      req = Request(url, headers = headers)
      response = urlopen(req)
      
    except HTTPError as e:
      print(e.status, e.reason)
      dataset_erro.append(url)
      continue
    except URLError as e:
      print(e.reason)
      dataset_erro.append(url)
      continue
    except :
      print("erro erro"+url)
      dataset_erro.append(url)
      continue
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    lista_modelos = soup.findAll('select', {"class": "g98wuw-1 hpeKug"})[1].findAll('option') # Vai gerar a lista de modelo da marca atual
    
    for modelo in lista_modelos: # Vai pecorrer a lista de modelos da marca atual
      modelo = modelo.text
      modelo_uni = limpar_modelo_por_marca(marca, modelo)

      modelo_uni = unidecode(modelo_uni)
      if modelo_uni == "modelo":
        continue
      url_modelo = url+'/'+modelo_uni
              
      try:
        req_modelo = Request(url_modelo, headers = headers)
        response_modelo = urlopen(req_modelo)

      except HTTPError as e:
        print(e.status, e.reason)
        continue 
      except URLError as e:
        print(e.reason)
        continue
      except :
        print("erro erro"+url)
        continue
      html_modelo = response_modelo.read().decode('utf-8')
      soup_modelo = BeautifulSoup(html_modelo, 'html.parser')
      if int(soup_modelo.find('span', {"class": "sc-1mi5vq6-0 dQbOE sc-ifAKCX lgjPoE"}).text[0]) > 0: # Verifica se o modelo tem algum anúncio, caso não tenha ele 
        #não consegue  localizar os estados e vai gerar um erro #
        for estado in soup_modelo.find('div', {"class": "sc-EHOje sc-1a202fr-0 dpPMei"}).findAll('div', {"class": "sc-EHOje loNQmp"}):
          # Localiza todos os estados e vai um por um para pegar a sua quantidade de anuncios
          modelos = {} # Variável que vai ser adicionada ao dataset
          modelos['Marca'] = marca
          modelos['Modelo'] = modelo
          modelos['Estado'] = estado.find('a',{'class':'sc-1l6qrj6-0 hSmLZl sc-gzVnrw KJfcY'}).text # Pega o nome do estado
          modelos['Qt Anuncio'] =  estado.find('span',{'class':'sc-1l6qrj6-1 bcgvPM sc-ifAKCX iOyFmS'}).text # Pega a quantidade de anúncios daquele estado
          dataset.append(modelos) # Adiciona aquele modelo com todos os estado
            
        print(url_modelo)
          
        
        
      else: # Caso não tenha anúncio daquele modelo o site é diferente por is vamos simplesmente acionar ele no dataset
        print('zero')
        modelos = {} # Variável que vai ser adicionada ao dataset
        modelos['Marca'] = marca
        modelos['Modelo'] = modelo
        dataset.append(modelos)
        dataset_zero.append(modelos)
        continue

      dataset_olx = pd.DataFrame(dataset)
      dataset_olx.to_csv('dataset.csv')

def Limpar():
  dataset_OLX = pd.read_csv('./dataset.csv')
  apagar = dataset_OLX[dataset_OLX['Modelo']=='Modelo'].index
  dataset_OLX.drop(apagar, inplace = True)
  def limpar(x):
    x = str(x)
    x = x.replace(', ','')
    x = x.replace('.','')
    return float(x)
  dataset_OLX['Qt Anuncio']= dataset_OLX['Qt Anuncio'].apply(limpar)
  dataset_OLX.to_csv('./dataset_OLX.csv')

def subir_banco_de_dados():
  dataset_OLX = pd.read_csv('./dataset_OLX.csv')
  conexao_pg = create_engine('postgresql://postgres:xxxxx@olx.c8demqn6blrs.us-east-1.rds.amazonaws.com/postgres').connect()
  dataset_OLX.to_sql( 
    name = 'olx',
    con = conexao_pg,
    index = False,
    if_exists = 'replace',
    method='multi')
