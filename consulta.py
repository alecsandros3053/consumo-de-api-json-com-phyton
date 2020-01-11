import requests
import json
import pandas

url = "http://data.fixer.io/api/latest?access_key=b6fcdabc470da8b76d45bb86012ffca6"
print("Acessando a base de dados da fixer.io...")
resposta = requests.get(url)
#print(resposta)
if resposta.status_code == 200:
    print("Acesso realizado com sucesso!")
    print("Buscando informações...")
    dados = resposta.json()
    dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'],2)
    euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'],2)
    btc_real = round(dados['rates']['BRL']/dados['rates']['BTC'],2)
    print('1 Dollar vale ', dolar_real, 'reais')
    print('1 Euro vale ', euro_real, 'reais')
    print('1 Bitcoin vale ', btc_real, 'reais')
    print("Exportando resultado em tabela Excel...")
    #criando duas listas para exportar os dados do csv, sempre na pasta do projeto
    tela = pandas.DataFrame({'Moedas':['Dolar','Euro','Bitcoin'],'Valores':[dolar_real, euro_real, btc_real]})
    tela.to_csv('valores.csv', index=False, sep=";", decimal=",") 
    #('valores.csv', index=False, sep=";", decimal=",") tratamento realizado para conversao arquivo excel. 
    print("Arquivo gerado com sucesso")
    #print(dados)
    #print(dados['rates'])
    #print(dados['rates']['BRL']/dados['rates']['EUR'])
    #print(dados['rates']['BRL']/dados['rates']['USD'])
    #print(dados['rates']['BRL']/dados['rates']['EUR'])
    #print(dados['rates']['BRL']/dados['rates']['BTC'])
else:
    print("Erro na base de dados")